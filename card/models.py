from django.db import models
from django.utils import timezone


class Teams(models.Model):
    class Meta:
        verbose_name = "Hold"
        verbose_name_plural = "Hold"
    name = models.CharField("Navn", max_length=200)


class Cards(models.Model):
    class Meta:
        verbose_name = "Kort"
        verbose_name_plural = "Kort"
    card_no = models.CharField("Kortnummer", max_length=10, unique=True,
                               blank=True, null=True)
    team_id = models.ForeignKey(Teams, on_delete=models.CASCADE)


class Posts(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Poster"
    team_id = models.ForeignKey(Teams, on_delete=models.CASCADE)
    time = models.DateTimeField("Besøgt post", blank=False, null=False,
                                default=timezone.now)
    pi = models.CharField("Raspberry Pi besøgt", max_length=99, blank=False,
                          null=False)


# Nice to have
class Persons(models.Model):
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Personer"
    name = models.CharField("Navn", max_length=200)


class PersonOnTeam(models.Model):
    class Meta:
        verbose_name = "Person på hold"
        verbose_name_plural = "Personer på hold"
    person_id = models.ForeignKey(Persons, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Teams, on_delete=models.CASCADE)
