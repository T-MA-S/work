from django.db import models


class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=50)
    city_id = models.ForeignKey('City', on_delete=models.PROTECT, null=True)
    street_id = models.ForeignKey('Street', on_delete=models.PROTECT, null=True)
    house_number = models.IntegerField("Номер дома")
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Street(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=50)
    city_id = models.ForeignKey('City', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Улица"
        verbose_name_plural = "Улицы"
