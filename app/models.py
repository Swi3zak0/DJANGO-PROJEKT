from django.db import models


# Create your models here.
class ShoeCategory(models.Model):
    name_category = models.CharField(max_length=100, unique=True)
    # url = models.URLField(default='/default-url/')

    class Meta:
        ordering = ('name_category',)

    def __str__(self):
        return self.name_category


class Shoe(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'),)
    name = models.CharField(max_length=64, blank=False)
    shoe_category = models.ForeignKey(ShoeCategory, related_name='shoes', on_delete=models.CASCADE)
    producer = models.CharField(max_length=32)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE)
    color = models.CharField(max_length=16, default="Czarny")
    price = models.DecimalField(max_digits=14, decimal_places=2)
    description = models.TextField(default="")
    image = models.ImageField(upload_to="zdjecia", null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    # def category_with_name(self):
    #     return "{} ({})".format(self.category, self.name)


class Client(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'),)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE)
    address = models.CharField(max_length=300)
    birthdate = models.DateField()
    added_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name+' '+self.last_name


class Order(models.Model):
    client = models.ForeignKey(Client, related_name='orders', on_delete=models.CASCADE)
    shoe = models.ForeignKey(Shoe, related_name='orders', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    quantity = models.IntegerField()
