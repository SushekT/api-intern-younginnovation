from django.db import models

# Create your models here.


class Main(models.Model):
    year = models.ForeignKey('Year', on_delete=models.CASCADE, null=True)
    petroleum = models.ForeignKey('Petroleum', on_delete=models.CASCADE, null=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, null=True)
    sale = models.IntegerField()


    def __str__(self):
        return self.country.name


class Year(models.Model):
    number = models.IntegerField()



class Petroleum(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class AverageSale(models.Model):
    product = models.ForeignKey('Petroleum', on_delete=models.CASCADE)
    countr = models.ForeignKey('Country', on_delete=models.CASCADE)
    average = models.IntegerField()

    def __str__(self):
        return self.product.name

class TwoYearInterval(models.Model):
    product = models.ForeignKey('Petroleum', on_delete=models.CASCADE)
    average = models.IntegerField()
    date = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.product.name

class Leastyear(models.Model):
    product = models.ForeignKey('Petroleum', on_delete=models.CASCADE)
    year = models.ForeignKey('Year', on_delete=models.CASCADE, null=True)
    leastsale = models.IntegerField()

    def __str__(self):
        return self.product