from django.shortcuts import render,redirect
from django.contrib import messages
from tracker.models import Transaction
from django.db.models import Sum


def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        if description is None:
            messages.error(request, ' Description cannot be blank')
            return redirect('/')
        try:
            amount = float(amount)
        except Exception as e:
            messages.info(request, "Should be a Number")
            return redirect('/')
        Transaction.objects.create(
            description=description,
            amount=amount
            )
    context = {
        'transactions': Transaction.objects.all(),
        'balance': Transaction.objects.all().aggregate(total_balance=Sum('amount'))['total_balance'] or 0,
        'income': Transaction.objects.filter(amount__gte=0).aggregate(income=Sum('amount'))['income'] or 0,
        'expense': Transaction.objects.filter(amount__lt=0).aggregate(expense=Sum('amount'))['expense'] or 0
    } 
    return render(request, 'index.html',context)
def deleteTransaction(request,uuid):
    Transaction.objects.get(uuid=uuid).delete()
    return redirect('/')
    