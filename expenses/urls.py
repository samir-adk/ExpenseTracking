from django.urls import path
from expenses.views import *

app_name='expenses'

urlpatterns=[
path('',index,name='index'),
path('create_income_category',create_income_category.as_view(),name='create_income_category'),
path('list_income_category',list_income_category.as_view(),name='list_income_category'),
path('delete_income_category/<int:id>',delete_income_category,name='delete_income_category'),
path('edit_income_category/<int:pk>',edit_income_category.as_view(),name='edit_income_category'),
path('create_income',create_income.as_view(),name='create_income'),
path('list_income',list_income,name='list_income'),
path('edit_income/<int:pk>',edit_income.as_view(),name='edit_income'),
path('delete_income/<int:id>',delete_income,name='delete_income'),
path('create_expense_category',create_expense_category.as_view(),name='create_expense_category'),
path('edit_expense_category/<int:pk>',edit_expense_category.as_view(),name='edit_expense_category'),
path('list_expense_category',list_expense_category,name='list_expense_category'),
path('delete_expense_category/<int:id>',delete_expense_category,name='delete_expense_category'),
path('create_expense',create_expense.as_view(),name='create_expense'),
path('edit_expense/<int:pk>',edit_expense.as_view(),name='edit_expense'),
path('list_expense',list_expense,name='list_expense'),
path('delete_expense/<int:id>',delete_expense,name='delete_expense'),
path('create_saving_category',create_saving_category.as_view(),name='create_saving_category'),
path('list_saving_category',list_saving_category.as_view(),name='list_saving_category'),
path('edit_saving_category/<int:pk>',edit_saving_category.as_view(),name='edit_saving_category'),
path('delete_saving_category/<int:id>',delete_saving_category,name='delete_saving_category'),
path('create_saving',create_saving.as_view(),name='create_saving'),
path('list_saving',list_saving.as_view(),name='list_saving'),
path('edit_saving/<int:pk>',edit_saving.as_view(),name='edit_saving'),
path('delete_saving/<int:id>',delete_saving,name='delete_saving'),
path('calculate',calculate,name='calculate'),
path('chart',chart,name='chart'),

]