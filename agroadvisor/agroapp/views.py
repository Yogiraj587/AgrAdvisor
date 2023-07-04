from django.shortcuts import render,redirect,get_object_or_404
import pandas as pd
import joblib
from .models import todo
from utils.fertiliser import fertiliser_info
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

def signup(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if username and password1 and password2:
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username Taken')
                    print('Username taken')
                    return render(request,'signup.html')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Taken')
                    print('Email taken')
                    return render(request,'signup.html')
                else:
                    user = User.objects.create_user(username = username,email = email)
                    user.set_password(password1)
                    user.save()
                    messages.info(request, 'User Created')
                    print('user created')
                    return render(request,'login.html')
            else:
                print('Password not matching')
                messages.info(request,'Passwords not matching')
        else:
            print('username or password missing')
            messages.info(request,'Passwords not matching')
            return render(request,'signup.html')
        
        return render(request,'signup.html')
    else:
        return render(request,'signup.html')
    
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

@never_cache
@login_required(login_url='login')
def logout(request):
    if request.user.is_authenticated:
        messages.info(request, 'Successfully logged out')
        auth.logout(request)
    
    response = redirect("/")
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    return response


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def tasks(request):
    if request.method=='POST':
        task = request.POST.get('task')
        new_todo = todo(user=request.user, todo_name=task)
        new_todo.save()
    all_todos = todo.objects.filter(user=request.user)
    context = {
        'todos': all_todos
    }
    return render(request,'tasks.html',context)

@login_required(login_url='login')
def Delete(request,name):
    get_todo = todo.objects.get(user=request.user, todo_name=name)
    get_todo.delete()
    return render(request,'tasks.html')

@login_required(login_url='login')
def Update(request, name):
    get_todo = todo.objects.get(user=request.user, todo_name=name)
    get_todo.status = True
    get_todo.save()
    return render(request,'tasks.html')


@login_required(login_url='login')
def cropprediction(request):
    if request.method == 'POST':
        n_soil = request.POST.get("n_soil")
        p_soil = request.POST.get("p_soil")
        k_soil = request.POST.get("k_soil")
        temp = request.POST.get("temp")
        humidity = request.POST.get("humidity")
        ph = request.POST.get("ph")
        rainfall = request.POST.get("rainfall")

        model = joblib.load("C:/Users/Yogiraj/VSCode/FullStackML/Harvestify/agroadvisor/cropmodel_joblib")

        prediction = model.predict([[n_soil, p_soil, k_soil, temp, humidity, ph, rainfall]])
        print("The Best Crop is: ")

        crop_names = [
            "Apple", "Banana", "Blackgram", "ChickPea", "Coconut", "Coffee", "Cotton", "Grapes",
            "Jute", "KidneyBeans", "Lentil", "Maize", "Mango", "MothBeans", "MungBean", "Muskmelon",
            "Orange", "Papaya", "PigeonPeas", "Pomegranate", "Rice", "Watermelon"
        ]

        if prediction[0] in range(len(crop_names)):
            predicted_crop = crop_names[prediction[0]]
        else:
            predicted_crop = "Not Found"

        context = {
            "prediction": predicted_crop,
        }

        return render(request, "cropprediction.html", context)

    return render(request, 'cropprediction.html')

@login_required(login_url='login')
def fertiliser(request):
    if request.method=='POST':
        N = int(request.POST.get("nitrogen"))
        K = int(request.POST.get("potassium"))
        P = int(request.POST.get("phosphorus"))
        crop = str(request.POST.get("crop"))

        
        df = pd.read_csv("C:/Users/Yogiraj/VSCode/FullStackML/Harvestify/agroadvisor/fertilizer.csv")
        nitrogen = df[df['Crop']==crop]['N'].iloc[0]
        potassium = df[df['Crop']==crop]['K'].iloc[0]
        phosphorus = df[df['Crop']==crop]['P'].iloc[0]

        n_eff = nitrogen - N
        k_eff = potassium - K
        p_eff = phosphorus - P

        temp = {abs(n_eff): "N",abs(k_eff):"K",abs(p_eff):"P"}
        maximum = temp[max(temp.keys())]

        if maximum == "N":
            if n_eff < 0:
                key = "NHigh"
            else:
                key = "Nlow"
        elif maximum == "K":
            if k_eff < 0:
                key = "KHigh"
            else:
                key = "Klow"
        else:
            if p_eff < 0:
                key ="PHigh"
            else:
                key = "Plow"
        
        result = str(fertiliser_info[key])
        print(result)
        context = {
            "result":result,
        }

        return render(request,"fertiliser.html",context)

    return render(request,"fertiliser.html")