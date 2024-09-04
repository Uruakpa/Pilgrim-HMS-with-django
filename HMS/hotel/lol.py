from django.db.models import Sum

# get today's date
total_amount = Payment.objects.filter(date=today).aggregate(total=Sum("amount"))['total']