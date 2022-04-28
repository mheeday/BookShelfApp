from distutils import archive_util
import imp
from pyexpat import model
from django.db import models
import datetime
from django.utils import timezone
import uuid
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Books(models.Model):
    BOOK_CATEGORIES = [
        ('CO', 'COMIC'),
        ('FA', 'FANTASY'),
        ('AC', 'ACTION'),
        ('TH', 'THRILLER'),
        ('CN', 'CONTEMPORARY'),
    ]
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)
    book_cat = models.CharField(max_length=2, choices=BOOK_CATEGORIES)
    book_cover = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    book_desc = models.CharField(max_length=200, )
    book_pubd = models.DateField()
    

class UserBooks(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    book_uuid = models.UUIDField(unique=True, editable=False)
    last_viewed = models.DateTimeField()
    archived = models.BooleanField(default=False)