from django.shortcuts import render
from django.http import JsonResponse
from notifications.models import Message
from expenses.models import Saving,Expenses,Income
from datetime import datetime,timedelta
from django.db.models import Sum
# Create your views here.
def messages(request):
    #doing queries for notifications
    today_date=datetime.now()
    month_period=today_date-timedelta(days=30)
    monthly_income_sum=Income.objects.all().filter(created_date__gte=month_period).filter(created_date__lte=today_date).aggregate(Sum('income_amount'))
    monthly_expense_sum=Expenses.objects.all().filter(Expend_date__gte=month_period).filter(Expend_date__lte=today_date).aggregate(Sum('Expnese_amount'))
    #subtract income and expenses for finding value
    net_balance=(monthly_income_sum['income_amount__sum'])-(monthly_expense_sum['Expnese_amount__sum'])
    if net_balance < 1:
        display_message='Alert !expenses is high'
        existing_message=Message.objects.filter(message=display_message).filter(created_at__gte=month_period)
        if not existing_message:
            print('not existed so creating new')
            Message.objects.create(message=display_message,created_at=datetime.now(),important=True)
    lists=[]
    messages=Message.objects.all().order_by('-created_at')
    messages_count=Message.objects.all().count()
    for data in messages:
        temp={
        'message':data.message,
        'created_at':data.created_at,
        'important':data. important,
        'count':messages_count,
        }
        lists.append(temp)
    context={
    'lists':lists,
    'messages_count':messages_count

    }
    return JsonResponse(context,safe=False)