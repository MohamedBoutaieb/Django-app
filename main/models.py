from django.db import models


# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todoist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    compete = models.BooleanField()

class BankAccount(models.Model):
    balance = models.FloatField(default=0)
    negative = models.BooleanField(default=False)
    def getBalance(self):
        return self.balance
