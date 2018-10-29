from django.urls import path, include

from . import views

urlpatterns= [
    path('',views.index, name='index'),
    path('add/', views.create, name='create'),
    path('expenselist/', views.expenseList, name='expense_list'),
    path('createUser/', views.makeUser, name='makeUser'),
    path('database/', views.database,name='database')

]