from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item, BankAccount
from .forms import CreateNewList, Bank


# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("delete"):
            ls.item_set.get(id=response.POST.get("delete")).delete()
        elif response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.compete = True
                else:
                    item.compete = False
                item.text = response.POST.get("txt" + str(item.id))
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                ls.item_set.create(text=txt, compete=False)
            else:
                print("invalid")

    return render(response, "main/list.html", {"ls": ls})


def home(response):
    return render(response, "main/home.html", {})


def create(response):
    ls =  ToDoList.objects.all()
    if (response.method == "POST"):
        form = CreateNewList(response.POST)
        if response.POST.get("del"):
            ToDoList.objects.get(id=response.POST.get("del")).delete()
            return HttpResponseRedirect("create")
        elif form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" % t.id)
    form = CreateNewList
    return render(response, "main/create.html", {"form": form,"todos":ls})


def bank(response):
    acc = BankAccount.objects.get(id=1)
    if acc.getBalance() < 0 :
        blc="rouge"
    else:
        blc="vert"
    if (response.method == "POST"):
        if acc.getBalance() < 0:
            blc = "rouge"
        else:
            blc = "vert"
        form = Bank(response.POST)
        if response.POST.get("add"):
            if form.is_valid():
                acc.balance+= form.cleaned_data["balance"]
                acc.save()
        if response.POST.get("withdraw"):
            if form.is_valid():
                acc.balance-= form.cleaned_data["balance"]
                acc.save()
        return HttpResponseRedirect("bank")
    form = Bank
    return render(response, "main/bank.html", {"bank": form, "account": acc,"blc":blc})
