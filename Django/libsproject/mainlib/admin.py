from django.contrib import admin
from .models import Books, UserBooks

admin.site.register(Books)
admin.site.register(UserBooks)
#admin.site.register(Books.book_cover)
# Register your models here.
