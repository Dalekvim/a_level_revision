from tinymce.models import HTMLField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Proof(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  date_created = models.DateTimeField(default=timezone.now)
  content = HTMLField()
