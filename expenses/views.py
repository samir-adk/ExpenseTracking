from django.shortcuts import render
from expenses.forms import IncomeCategoryForm,IncomeForm,ExpensesCategoryForm,ExpensesForm,SavingCategoryForm,SavingForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect
from datetime import timedelta,datetime
from django.db.models.functions import TruncWeek
from django.db.models import Sum
from django.utils import timezone

from expenses.models import Company,WeeklyExpense,IncomeCategory,Income,ExpenseCategory,Expenses,SavingCategory,Saving
# Create your views here.

def index(request):
    logged_user=request.user
    today_time=datetime.now()
    previous_day=today_time-timedelta(days=7)
    month_date=today_time-timedelta(days=30)
    monthly_income=Income.objects.values('income_category__income_category').filter(created_date__gte=month_date).filter(created_date__lte=today_time).filter(created_user__username=logged_user).annotate(sum_amount=Sum('income_amount'))
    chart_data=Expenses.objects.values('Expenses_category__category_name').filter(Expend_date__gte=previous_day).filter(created_user__username=logged_user).filter(Expend_date__lte=today_time).annotate(sum_amount=Sum('Expnese_amount'))
    saving_data=Saving.objects.values('Saving_category__Saving_Category').filter(created_at__gte=previous_day).filter(created_at__lte=today_time).filter(created_user__username=logged_user).annotate(sum_amount=Sum('saving_amount'))
    # company_profile=Company.objects.filter().first()
    return render(request,'index.html',{'company_profile':'','chart_data':chart_data,'saving_data':saving_data,'monthly_income':monthly_income})
    
class create_income_category(CreateView):
    model=IncomeCategory
    template_name='income/create_income_category.html'
    form_class=IncomeCategoryForm
    success_url=reverse_lazy('expenses:create_income_category')

    def form_valid(self,form):
        form.instance.created_user=self.request.user
        return super().form_valid(form)

def list_income_category(request):
    logged_user=request.user
    if request.POST.get('start_date'):
        if request.method=='POST':
            start_date=request.POST.get('start_date')
            end_date=request.POST.get('end_date')
            data_list=IncomeCategory.objects.filter(created_at__gte=start_date).filter(created_at__lte=end_date).filter(created_user__username=logged_user)
            return render(request,'income/list_income_category.html',{'data':data_list})
    data_list=IncomeCategory.objects.all().filter(created_user__username=logged_user) 
    return render(request,'income/list_income_category.html',{'data':data_list})
    

def delete_income_category(request,id):
    find_data=IncomeCategory.objects.get(id=id)
    if request.method == 'POST':
        get_data=IncomeCategory.objects.filter(id=id).delete()
        return redirect('expenses:list_income_category')
    return render(request,'income/delete_income_category.html',{'data':find_data})

class edit_income_category(UpdateView):
    model =IncomeCategory
    template_name='income/edit_income_category.html'
    form_class=IncomeCategoryForm
    success_url=reverse_lazy('expenses:list_income_category')
    


class create_income(CreateView):
    model= Income
    template_name='income/create_income.html'
    form_class=IncomeForm
    success_url=reverse_lazy('expenses:create_income')

    def form_valid(self,form):
        form.instance.created_user=self.request.user
        return super().form_valid(form)


def list_income(request):
    logged_user=request.user
    if request.POST.get('start_date'):
        if request.method=='POST':
            start_date=request.POST.get('start_date')
            end_date=request.POST.get('end_date')
            data_list=Income.objects.filter(created_date__gte=start_date).filter(created_date__lte=end_date).filter(created_user__username=logged_user)
            return render(request,'income/list_income.html',{'data':data_list})
    data_list=Income.objects.all().filter(created_user__username=logged_user)
    return render(request,'income/list_income.html',{'data':data_list})
    


class edit_income(UpdateView):
    model= Income
    template_name='income/edit_income.html'
    form_class=IncomeForm
    success_url=reverse_lazy('expenses:list_income')


def delete_income(request,id):
    find_data=Income.objects.get(id=id)
    if request.method == 'POST':
        get_data=Income.objects.get(id=id).delete()
        return redirect('expenses:list_income')
    return render(request,'income/delete_income.html',{'data':find_data})

class create_expense_category(CreateView):
    model= ExpenseCategory
    template_name='expenses/create_expense_category.html'
    form_class=ExpensesCategoryForm
    success_url=reverse_lazy('expenses:create_expense_category')
    def form_valid(self,form):
        form.instance.created_user=self.request.user
        return super().form_valid(form)

def  list_expense_category(request):
    logged_user=request.user
    data_list=ExpenseCategory.objects.all().filter(created_user__username=logged_user)
    return render(request,'expenses/list_expenses_category.html',{'data':data_list})

class edit_expense_category(UpdateView):
    model= ExpenseCategory
    template_name='expenses/edit_expenses_category.html'
    form_class=ExpensesCategoryForm
    success_url=reverse_lazy('expenses:list_expense_category')


def delete_expense_category(request,id):
    find_data=ExpenseCategory.objects.get(id=id)
    if request.method == 'POST':
        get_data=ExpenseCategory.objects.get(id=id).delete()
        return redirect('expenses:list_expense_category')
    return render(request,'expenses/delete_expenses_category.html',{'data':find_data})

class create_expense(CreateView):
    model= Expenses
    template_name='expenses/create_expense.html'
    form_class=ExpensesForm
    success_url=reverse_lazy('expenses:create_expense')
    def form_valid(self,form):
        form.instance.created_user=self.request.user
        return super().form_valid(form)

def  list_expense(request):
    logged_user=request.user
    if request.POST.get('start_date'):
        if request.method=='POST':
            start_date=request.POST.get('start_date')
            end_date=request.POST.get('end_date')
            data_list=Expenses.objects.filter(Expend_date__gte=start_date).filter(Expend_date__lte=end_date).filter(created_user__username=logged_user)
            return render(request,'expenses/list_expenses.html',{'data':data_list})
    data_list=Expenses.objects.all().filter(created_user__username=logged_user)
    return render(request,'expenses/list_expenses.html',{'data':data_list})

class edit_expense(UpdateView):
    model= Expenses
    template_name='expenses/edit_expenses.html'
    form_class=ExpensesForm
    success_url=reverse_lazy('expenses:list_expense')


def delete_expense(request,id):
    find_data=Expenses.objects.get(id=id)
    if request.method == 'POST':
        get_data=Expenses.objects.get(id=id).delete()
        return redirect('expenses:list_expense')
    return render(request,'expenses/delete_expenses.html',{'data':find_data})

class create_saving_category(CreateView):
    model = SavingCategory
    form_class=SavingCategoryForm
    template_name='saving/create_saving_category.html'

    success_url=reverse_lazy('expenses:create_saving_category')
    def form_valid(self,form):
        form.instance.created_user=self.request.user
        return super().form_valid(form)

class edit_saving_category(UpdateView):
    model = SavingCategory
    form_class=SavingCategoryForm
    template_name='saving/create_saving_category.html'
  
    success_url=reverse_lazy('expenses:create_saving_category')

class list_saving_category(ListView):
    model = SavingCategory
    template_name='saving/list_saving_category.html'

def delete_saving_category(request,id):
    find_data=SavingCategory.objects.get(id=id)
    if request.method == 'POST':
        get_data=SavingCategory.objects.get(id=id).delete()
        return redirect('expenses:list_saving_category')
    return render(request,'saving/delete_saving_category.html',{'data':find_data})


class create_saving(CreateView):
    model = Saving
    form_class=SavingForm
    template_name='saving/create_saving.html'
    success_url=reverse_lazy('expenses:create_saving')

    def form_valid(self,form):
        form.instance.created_user=self.request.user
        return super().form_valid(form)

class edit_saving(UpdateView):
    model = Saving
    form_class=SavingForm
    template_name='saving/create_saving.html'
    success_url=reverse_lazy('expenses:create_saving')

def list_saving(request):
    logged_user=request.user
    if request.POST.get('start_date'):    
        if request.method=='POST':
            start_date=request.POST.get('start_date')
            end_date=request.POST.get('end_date')
            data_list=Saving.objects.filter(created_at__gte=start_date).filter(created_at__lte=end_date).filter(created_user__username=logged_user)
            return render(request,'saving/list_saving.html',{'data':data_list})
    data_list=Saving.objects.all().filter(created_user__username=logged_user)
    return render(request,'saving/list_saving.html',{'data':data_list})


def delete_saving(request,id):
    find_data=Saving.objects.get(id=id)
    if request.method == 'POST':
        get_data=Saving.objects.get(id=id).delete()
        return redirect('expenses:list_saving')
    return render(request,'saving/delete_saving.html',{'data':find_data})


def calculate(request):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)

    # Group the expenses by the week and calculate the sum of the expenses for each week
    weekly_expenses = Expenses.objects.filter(
        Expend_date__gte=start_date,
        Expend_date__lte=end_date,
    ).filter(created_user__username=logged_user).annotate(
        week=TruncWeek('Expend_date')
    ).values(
        'week'
    ).annotate(
        total_expenses=Sum('Expnese_amount')
    )
    week_expend = weekly_expenses[0]['total_expenses'] if weekly_expenses else 0
    week = start_date
    WeeklyExpense.objects.update_or_create(
        week_date=week,
        defaults={'total_expenses': week_expend}
    )
    weekly_expenses = WeeklyExpense.objects.all().filter(created_user__username=logged_user)
    return render(request,'calculate.html',{'weekly_expenses':weekly_expenses})

def chart(request):
    chart_data=Expenses.objects.filter(created_user__username=logged_user).values('Expenses_category__category_name').annotate(sum_amount=Sum('Expnese_amount'))
    return render(request,'chart.html',{'chart_data':chart_data})

