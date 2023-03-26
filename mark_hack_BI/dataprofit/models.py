from django.db import models


class Defect(models.Model):
    gtin = models.CharField(max_length=200)
    defect_lvl = models.FloatField()

    def __str__(self):
        return self.gtin

class ABC(models.Model):
    gtin = models.CharField(max_length=200)
    revenue = models.DecimalField(max_digits=12, decimal_places=2)
    share = models.FloatField()
    ABC = models.CharField(max_length=1)
    share_cum = models.DecimalField(max_digits=12, decimal_places=5)
    
    def __str__(self) -> str:
        return f'{self.gtin} : {str(self.revenue)} категория {self.ABC}'
    
class ABC_NEW(models.Model):
    gtin = models.CharField(max_length=200)
    revenue = models.DecimalField(max_digits=12, decimal_places=2)
    share = models.FloatField()
    ABC = models.CharField(max_length=1)
    share_cum = models.DecimalField(max_digits=12, decimal_places=5)
    
    def __str__(self) -> str:
        return f'{self.gtin} : {str(self.revenue)} категория {self.ABC}'
    

class Price_min_max(models.Model):
    gtin = models.CharField(max_length=200)
    price_min = models.DecimalField(max_digits=12, decimal_places=2)
    price_max = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.gtin} : минимальная цена{str(self.price_min)} максимальная цена{self.price_max}'