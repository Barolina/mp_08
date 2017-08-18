import os
from django.db import models
# Create your models here.
from django.urls import reverse
from filer.models.filemodels import File
from django_extensions.db.fields import AutoSlugField

class DraftPlan(models.Model):
    name = models.CharField(max_length=255)

# Corresponds to XSD type[s]: tCadastralEngineer
class CadastralEngineer(models.Model):
    FamilyName = models.CharField(max_length=100, verbose_name="Фамилия")
    FirstName = models.CharField( max_length=100, verbose_name= "Имя")
    Patronymic = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отчество")
    CadastralEngineerRegistryNumber = models.CharField(max_length=50, verbose_name="Номер квалификационного аттестата кадастрового инженера")
    Telephone = models.CharField(max_length=50, verbose_name="Контактный телефон")
    Address = models.TextField(max_length=4000, verbose_name= "Почтовый адрес для связи с кадастровым инженером")
    Email = models.EmailField(verbose_name="Адрес электронной почты")
    slug = AutoSlugField(
        max_length=255,
        null=False,
        blank=False,
        populate_from='engineer',
        editable=True,
        unique=True,
        db_index=True
    )

    class Meta:
        verbose_name = "Сведения о кадастровом инженере"

    def __str__(self):
        return  '{0} {1}'.format(self.FamilyName, self.FirstName)

    @models.permalink
    def get_absolute_url(self):
        return reverse('cadastral_engineer_detail', args=[self.slug])
