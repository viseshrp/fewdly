from django.contrib import admin
from .models import Review, Reviewer, Restaurant
# Register your models here.
admin.site.register(Review)
admin.site.register(Reviewer)
admin.site.register(Restaurant)
