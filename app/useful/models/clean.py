from django.db import models

class Clean(models.Model):
  updated = models.DateTimeField()
  clean_group_id = models.IntegerField()
