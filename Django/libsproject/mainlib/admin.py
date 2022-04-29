from django.contrib import admin
from .models import Books, UserBook, BookReview

admin.site.register(Books)
admin.site.register(UserBook)
admin.site.register(BookReview)
#admin.site.register(Books.book_cover)
# Register your models here.
