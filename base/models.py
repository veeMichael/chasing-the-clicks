from django.db import models


class ClickCount(models.Model):
    count = models.IntegerField(default=0)
