# -*- coding: utf-8 -*-

from django.db import models
import datetime

class Cultivar(models.Model):
    name = models.CharField(u"品種", max_length=255)
	
    def __unicode__(self):
        return self.name

class Impression(models.Model):
    registration_date = models.DateField(u"登録日", default=datetime.date.today())
    cultivar = models.ForeignKey(Cultivar, verbose_name=u"品種", null=True)
    comment = models.CharField(u"感想", max_length=255, blank=True)
	