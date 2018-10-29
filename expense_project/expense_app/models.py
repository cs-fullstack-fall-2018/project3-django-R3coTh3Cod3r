from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class ExpenseModel(models.Model):
    username=models.CharField(max_length=300)
    foreign_expense_user=models.ForeignKey(User,on_delete=models.CASCADE)
    balance =models.IntegerField()
    emergency_fund_status=models.IntegerField()
    withdrawls=models.IntegerField()
    deposit=models.IntegerField()
    amount=models.IntegerField()
    statedDate=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.username + "" + self.foreign_expense_user+ ""+ self.balance+ "" + self.emergency_fund_status+ ""+self.withdrawls+ ""+ self.deposit+ ""+ self.amount+""+ self.statedDate

class setupUser(models.Model):
    name = models.CharField(max_length=300)
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.name