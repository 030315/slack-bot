from django.db import models

class Members(models.Model):
  name1 = models.CharField(max_length=10)
  name2 = models.CharField(max_length=10)
  slack_user_name = models.CharField(max_length=50)
  clean_group_id = models.IntegerField()

