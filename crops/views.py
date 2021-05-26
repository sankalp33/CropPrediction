from django.shortcuts import render, HttpResponse
from .models import  Contribute
import pickle
import numpy as np


# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    if request.method == 'POST':
        postdata = request.POST
        N = postdata.get('n')
        P = postdata.get('p')
        K = postdata.get('k')
        T = postdata.get('t')
        H = postdata.get('h')
        PH = postdata.get('ph')
        R = postdata.get('r')
        val = [N,P,K,T,H,PH,R]
        model = pickle.load(open('finalized_model.sav','rb'))
        features = [float(x) for x in val]
        final = [np.array(features)]
        prediction = model.predict(final)
        output = prediction[0]
        context = {
            "output" : output
        }
        return render(request, 'home.html' , context)


def contribute(request):
    if request.method == 'GET':
         return render(request, 'contribute.html')
    if request.method == 'POST':
        postdata = request.POST
        N = postdata.get('n')
        P = postdata.get('p')
        K = postdata.get('k')
        T = postdata.get('t')
        H = postdata.get('h')
        PH = postdata.get('ph')
        R = postdata.get('r')
        Crop = postdata.get('crop')
        data = Contribute(Nitrogen = N,
        Phosphorous = P,
        Potassium = K,
        Temperature = T,
        Humidity = H,
        Ph = PH,
        Rainfall = R,
        Suitable_crop = Crop)
        data.save()
        return render(request, 'contribute.html')


