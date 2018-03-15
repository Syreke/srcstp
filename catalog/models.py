from django.db import models
# Create your models here.

from django.urls import reverse


class Player(models.Model):
    first_name = models.CharField(max_length=200, help_text="Есімін енгізініз")
    last_name = models.CharField(max_length=200, help_text="Тегін енгізініз")
    team = models.CharField(max_length=200, help_text="Команда атын енгізініз")
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]


    def get_absolute_url(self):
        return reverse('player-detail', args=[str(self.id)])

    def __str__(self):
        return '{0},{1}'.format(self.last_name, self.first_name)


class Team(models.Model):
    name = models.CharField(max_length=200, help_text="Атын енгізініз")
    awards = models.CharField(max_length=200, help_text="Марапаттарды енгізініз")
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["name","awards"]

    def get_absolute_url(self):
        return reverse('team-detail', args=[str(self.id)])

    def __str__(self):
        return '{0},{1}'.format(self.name,self.awards)


