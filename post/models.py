from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import utc
import datetime

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_created= models.DateTimeField(auto_now_add=True)

    @property
    def get_last_hour(self):
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        timediff = now - self.date_created
        return round(timediff.total_seconds() / 3600)

