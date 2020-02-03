from django.db import models
from django.urls import reverse

# Create your models here.

class Vehicles(models.Model):
    NUMBER_CHOICES = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )
    model = models.CharField(max_length=20)
    license_plate = models.CharField(max_length=20)
    tags = models.CharField(max_length=20, choices=[
        ('','No Choices To Show...')
    ], blank=True)
    driver = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    chasis_number = models.CharField(max_length=20)
    model_year = models.IntegerField(null=True)

    number_of_seats = models.CharField(max_length=20, default=4, choices=NUMBER_CHOICES)
    number_of_doors = models.CharField(max_length=20, default=4, choices=NUMBER_CHOICES)
    color = models.CharField(max_length=20)
    last_odometer = models.IntegerField(null=True)
    first_contract_date = models.DateField(null=True)
    residual_value = models.IntegerField(null=True)
    transmission = models.CharField(max_length=20, null=True, choices=[
        ('Manual','Manual'),
        ('Automatic','Automatic'),
    ])
    fuel_type = models.CharField(max_length=20, choices=[
        ('Petrol','Petrol'),
        ('Diesel','Diesel'),
    ])
    horsepower = models.IntegerField(null=True)
    power = models.IntegerField(null=True)

    def __str__(self):
        return "%s: %s" % (self.model, self.license_plate)
    
    def get_absolute_url(self):
        return reverse("vehicleapp:vehicledetail", kwargs={"pk": self.pk})
    

class OdometerReading(models.Model):
    vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    odometer_value = models.FloatField(default=0.0)
    unit = models.CharField(max_length=2, choices=[('mi', 'Miles'), ('km', 'Kilometers')], default='km')
    date = models.DateField(null=True)

    def get_absolute_url(self):
        return reverse("vehicleapp:odo-detail", kwargs={"pk": self.pk})

class FuelLog(models.Model):
    vehicle = models.ForeignKey('vehicleapp.Vehicles', on_delete=models.CASCADE)
    liter = models.IntegerField(null=True)
    Price_per_litre = models.IntegerField(null=True)
    total_price = models.IntegerField(null=True)
    odometer_Value = models.IntegerField(null=True)
    date = models.DateField()
    purchaser = models.CharField(max_length=20)
    invoice_reference = models.CharField(max_length=20)
    vendor = models.CharField(max_length=32)

    def get_absolute_url(self):
        return reverse("vehicleapp:fueldetail", kwargs={"pk": self.pk})

class ServiceLog(models.Model):
    vehicle = models.ForeignKey('vehicleapp.Vehicles', on_delete=models.CASCADE)
    service_type = models.CharField(max_length=32)
    total_price = models.IntegerField(null=True)
    odometer_Value = models.IntegerField(null=True)
    date = models.DateField()
    purchaser = models.CharField(max_length=20)
    vendor = models.CharField(max_length=20, choices=[])
    invoice_reference = models.CharField(max_length=20)
    
    def get_absolute_url(self):
        return reverse("vehicleapp:servicedetail", kwargs={"pk": self.pk})


