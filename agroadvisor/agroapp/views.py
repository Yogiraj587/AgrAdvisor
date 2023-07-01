from django.shortcuts import render
import pandas as pd
import math
import joblib
from utils.fertiliser import fertiliser_info

model = joblib.load("C:/Users/Yogiraj/VSCode/FullStackML/Harvestify/agroadvisor/cropmodel_joblib")

def home(request):
    return render(request, 'home.html')

def cropprediction(request):
    if request.method == 'POST':
        n_soil = request.POST.get("n_soil")
        p_soil = request.POST.get("p_soil")
        k_soil = request.POST.get("k_soil")
        temp = request.POST.get("temp")
        humidity = request.POST.get("humidity")
        ph = request.POST.get("ph")
        rainfall = request.POST.get("rainfall")

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

def fertiliser(request):
    if request.method=='POST':
        N = int(request.POST.get("nitrogen"))
        K = int(request.POST.get("potassium"))
        P = int(request.POST.get("phosphorus"))
        crop = str(request.POST.get("crop"))

        print(N)
        print(K)
        print(P)
        print(crop)
        
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
