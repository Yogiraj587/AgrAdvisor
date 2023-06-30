from django.shortcuts import render
import joblib

model = joblib.load("C:/Users/Yogiraj/VSCode/FullStackML/Harvestify/agroadvisor/cropmodel_joblib")
def home(request):
    return render(request,'home.html')

def cropprediction(request):
    if request.method=='POST':
        n_soil = request.POST.get("n_soil")
        p_soil = request.POST.get("p_soil")
        k_soil = request.POST.get("k_soil")
        temp = request.POST.get("temp")
        humidity = request.POST.get("humidity")
        ph = request.POST.get("ph")
        rainfall = request.POST.get("rainfall")

        # print(n_soil)
        # print(p_soil)
        # print(k_soil)
        # print(temp)
        # print(humidity)
        # print(ph)
        # print(rainfall)

        prediction = model.predict([[n_soil,p_soil,k_soil,temp,humidity,ph,rainfall]])
        print("The Best Crop is: ")

        if prediction[0] == 0:
            prediction = "Apple"
        elif prediction[0] == 1:
            prediction = "Banana"
        elif prediction[0] == 2:
            prediction  = "Blackgram"
        elif prediction[0] == 3:
            prediction  = "ChickPea"
        elif prediction[0] == 4:
            prediction  = "Coconut"
        elif prediction[0] == 5:
            prediction  = "Coffee"
        elif prediction[0] == 6:
            prediction  = "Cotton"
        elif prediction[0] == 7:
            prediction  = "Grapes"
        elif prediction[0] == 8:
            prediction  = "Jute"
        elif prediction[0] == 9:
            prediction  = "KidneyBeans"
        elif prediction[0] == 10:
            prediction  = "Lentil"
        elif prediction[0] == 11:
            prediction  = "Maize"
        elif prediction[0] == 12:
            prediction  = "Mango"
        elif prediction[0] == 13:
            prediction  = "MothBeans"
        elif prediction[0] == 14:
            prediction  = "MungBean"
        elif prediction[0] == 15:
            prediction  = "Muskmelon"
        elif prediction[0] == 16:
            prediction  = "Orange"
        elif prediction[0] == 17:
            prediction  = "Papaya"
        elif prediction[0] == 18:
            prediction  = "PigeonPeas"
        elif prediction[0] == 19:
            prediction  = "Pomegranate"
        elif prediction[0] == 20:
            prediction  = "Rice"
        elif prediction[0] == 21:
            prediction  = "Watermelon"
        else:
            prediction = "Not Found"

        context = {
            "prediction": str(prediction),
        }

        return render(request,"cropprediction.html",context)

    return render(request,'cropprediction.html')
