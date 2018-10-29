from django.contrib import admin
from .models import ExpenseModel, setupUser
# Register your models here.
admin.site.register(ExpenseModel)
admin.site.register(setupUser)