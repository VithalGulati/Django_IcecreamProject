from typing import ContextManager
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact

from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from sklearn.svm import SVR

# Create your views here.

import joblib

reloadModel=joblib.load("Icecream_Revenue_Prediction.pkl")
import pickle

# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("This is Homepage")
def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is about page")       
def services(request):
    return render(request,'services.html')
    # return HttpResponse("This is services page")
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
    return render(request,'contact.html')
    # return HttpResponse("This is contact page")         
def prediction(request):
        return render(request,'prediction.html')
def revenue(request):
        context={"scoreval":""}
        return render(request,'revenue.html',context) 
def revenueprediction(request):
    print(request)
    if request.method == 'POST':
        temp={}
        temp[0]=request.POST.get('temperature')
        testdata=pd.DataFrame({1:temp}).transpose()
        clf = SVR(kernel = 'rbf' ,C=20, gamma="auto")
        icecream=pd.read_csv("icecream.csv")
        y=icecream['Revenue']
        x=icecream[['Temperature']]
        clf.fit(x,y)
        scoreval=clf.predict(testdata)[0]
        # loaded_model = pickle.load(open('Icecream_Revenue_Prediction.pkl', 'rb'))
        # scoreval=loaded_model.predict(testdata)[0]
    context={"scoreval":scoreval}
    return render(request,'revenue.html',context)               