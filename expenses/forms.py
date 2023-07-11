from django import forms

from expenses.models import  IncomeCategory,Income,ExpenseCategory,Expenses,SavingCategory,Saving

class DateInput(forms.DateInput):
    input_type = 'date'

class IncomeCategoryForm(forms.ModelForm):
    class Meta:
        model = IncomeCategory
        fields='__all__'
        widgets = {
        'created_at': DateInput(),
        }

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields='__all__'
        widgets = {
        'created_date': DateInput(),
        }


class ExpensesCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields='__all__'
        widgets = {
        'created_at': DateInput(),
        }

class ExpensesForm(forms.ModelForm):
    class Meta:
        model=Expenses
        fields='__all__'
        widgets = {
        'Expend_date': DateInput(),
        }

class SavingCategoryForm(forms.ModelForm):
    class Meta:
        model=SavingCategory
        fields='__all__'
        widgets = {
        'created_date': DateInput(),
        }

class SavingForm(forms.ModelForm):
    class Meta:
        model =Saving
        fields='__all__'
        widgets={
        'created_at':DateInput()
        }