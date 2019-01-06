from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def handshake(request,data):
    if(request.method == "GET" and data.lower() == "loadmodel"):
        #callFunction()
        print("Function called!")
    return JsonResponse({"Status":"Success " + str(data)})

def loadModel():
    #logic to load the locally saved model
    return True
