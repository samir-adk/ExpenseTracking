from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=100)
    image=models.FileField(upload_to='company_image')

class IncomeCategory(models.Model):
    income_category=models.CharField(max_length=100)
    is_important=models.BooleanField(default=True)
    created_at=models.DateTimeField()

    def __str__(self):
        return self.income_category

class Income(models.Model):
    income_category=models.ForeignKey(IncomeCategory,on_delete=models.SET_NULL,null=True)
    income_amount=models.IntegerField()
    created_date=models.DateTimeField()
    def __str__(self):
        return str(self.income_amount)




class ExpenseCategory(models.Model):
    category_name=models.CharField(max_length=100)
    is_important=models.BooleanField(default=True)
    created_at=models.DateTimeField()

    def __str__(self):
        return self.category_name

class Expenses(models.Model):
    Expenses_category=models.ForeignKey(ExpenseCategory,on_delete=models.SET_NULL,null=True)
    Expenses_name=models.CharField(max_length=200)
    Expnese_amount=models.IntegerField()
    Expenses_important=models.BooleanField(default=True)
    Expend_date=models.DateTimeField()

    def __str__(self):
        return self.Expenses_name

class WeeklyExpense(models.Model):
    week_date=models.DateField()
    total_expenses = models.IntegerField()

class SavingCategory(models.Model):
    Saving_Category=models.CharField(max_length=250)
    created_date=models.DateTimeField()

    def __str__(self):
        return self.Saving_Category

class Saving(models.Model):
    Saving_category=models.ForeignKey(SavingCategory,on_delete=models.SET_NULL,null=True)
    saving_amount=models.IntegerField()
    created_at=models.DateField()

    def __str__(self):
        return str(self.saving_amount)



