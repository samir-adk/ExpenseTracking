from django.contrib import admin
from expenses.models import  Company,WeeklyExpense,IncomeCategory,Income,ExpenseCategory,Expenses,SavingCategory,Saving
# Register your models here.
admin.site.register(IncomeCategory)
admin.site.register(Expenses)
admin.site.register(WeeklyExpense)
admin.site.register(Company)
admin.site.register(Saving)