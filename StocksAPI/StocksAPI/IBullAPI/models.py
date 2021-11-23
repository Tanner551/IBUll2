from django.db import models

# Create your models here.
class Trade(models.Model):
    Trade_id=models.IntegerField()
    type=models.CharField(max_length = 4)
    user_id=models.IntegerField()
    symobl=models.CharField(max_length=3)
    shares=models.IntegerField()
    price=models.IntegerField()
    timestamp=models.IntegerField()