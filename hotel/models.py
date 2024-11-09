from django.db import models
from django.utils.text import slugify



def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return f"hotels/{instance.id}.{extension}"

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    map_link = models.URLField(verbose_name="Map Link")
    description = models.TextField()
    
    included = models.TextField(help_text="Services included in the package")
    excluded = models.TextField(help_text="Services not included in the package")
    program = models.TextField(help_text="Hotel program or itinerary")
    
    ROOM_TYPES = [
        ('single', 'Single'),
        ('duo', 'Duo'),
        ('family', 'Family'),
        ('luxury', 'Luxury'),
        ('deluxe', 'Deluxe'),
    ]
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    
    # Hotel Amenities (Checkbox fields in HTML)
    airport_transfer = models.BooleanField(default=False)
    safety_box = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    spa_sauna = models.BooleanField(default=False)
    pet_allowed = models.BooleanField(default=False)
    free_wifi = models.BooleanField(default=False)
    air_dryer = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    laundry_service = models.BooleanField(default=False)
    king_size_bed = models.BooleanField(default=False)
    front_desk = models.BooleanField(default=False)
    living_area = models.BooleanField(default=False)
    
    rating = models.DecimalField(max_digits=3, decimal_places=1, help_text="Rating out of 10")
    stars = models.PositiveSmallIntegerField(choices=[(i, f"{i} Stars") for i in range(1, 7)], default=1)
    
    # Images
    image1 = models.ImageField(upload_to=image_upload)
    image2 = models.ImageField(upload_to=image_upload, blank=True, null=True)
    image3 = models.ImageField(upload_to=image_upload, blank=True, null=True)
    
    # Category (display with color on the template)
    CATEGORY_CHOICES = [
        ('best_sale', 'Best Sale'),
        ('promotion', 'Promotion'),
        ('top', 'Top'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)
    
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class HotelBooking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="bookings")
    order_number = models.CharField(max_length=20, unique=True)
    check_in = models.DateField(blank=True, null=True)
    check_out = models.DateField(blank=True, null=True)
    
    number_of_adults = models.PositiveSmallIntegerField(default=1, verbose_name="Number of Adults (18+)")
    amount_per_adult = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount_adult = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    
    number_of_children = models.PositiveSmallIntegerField(default=0, verbose_name="Number of Children (Under 18)")
    amount_per_child = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_amount_children = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        # Calcul des montants totaux
        self.total_amount_adult = self.amount_per_adult * self.number_of_adults
        self.total_amount_children = self.amount_per_child * self.number_of_children
        self.total_amount = self.total_amount_adult + self.total_amount_children
        
        # Générer un numéro de commande unique si ce n'est pas défini
        if not self.order_number:
            self.order_number = f"ORD-{self.hotel.id}-{self.pk or 'NEW'}"
            
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking {self.order_number} for {self.hotel.name}"


