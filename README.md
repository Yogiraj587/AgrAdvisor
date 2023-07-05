# AgroAdvisor

## Inspiration

Farmers face several challenges in agriculture related to crop selection, fertilizer selection, and disease management. Farmers must navigate these complexities to make informed choices for optimal yields and profitability. Crop selection involves factors such as market demand, climate suitability, and disease resistance. Similarly, selecting the right fertilizers requires knowledge of soil nutrient deficiencies and crop nutrient requirements. Over or under-fertilization can lead to imbalances, affecting plant health and productivity.

![Kaia-Personal-Trainer-1024x636](https://user-images.githubusercontent.com/84268500/215325986-379b1ee0-2dfe-409f-a04f-24cfffebda45.jpg)

## About it 

Agroadvisor is an innovative project aimed at addressing the challenges faced by farmers in agriculture. It provides valuable assistance in crop selection, fertilizer recommendation, and disease detection, empowering farmers with informed decision-making.

## What it does

### Crop Recommender
1. Best crop will be suggested after entering the Nitrogen, Potassium, Phosphorus content in the soil, along with the rainfall. Temperature, Humidity will be fetched using OpenWeather API.

![image](https://github.com/Yogiraj587/AgroAdvisor/assets/84268500/451fc40e-0f9a-47c4-8fbd-d0a07a7dea4e)


## How we built it

1. The Crop Recommendation and Fertiliser Recommendation models were trained using Random Forest Classifier model.
2. The Leaf Disease Detector was trained using Resnet-50 deep learning model.
3. HTML, CSS, and Bootstrap were used to create the user interface.
4. We used Django as our backend to integrate our Deep learning model with the UI.
5. We have also added User Authentication and Task Management using Django.

## Challenges we ran into

1. Performing EDA, Feature Engineering on the Indian crop dataset was a bit difficult.
2. Deep learning model training required a significant amount of time and computation power.
3. It was difficult to integrate our deep learning model with the user interface.
4. Improving the model's accuracy was an aesthetic taste.

## Accomplishments we are proud of 

1. We were able to create a model that can recommend crops, fertilisers based on the user's input.
2. Developing a full stack web application and incorporating this model was incredible.

## What we Learned
We have discovered a lot about Data Cleaning, Feature Engineering, Machine Learning, Deep Learning. Gained hands on experience with MLOps. We have worked on with Django for interacting with the web application.

## What's next for FitGenie
 
1. Implementing Face recognition for user authentication and authorisation.
2. Working to improve the accuracy of the models.
3. Should include more features like weather prediction etc.
