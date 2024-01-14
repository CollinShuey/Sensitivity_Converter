from collections import defaultdict

import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):


    if request.method == "POST":
        
        game = request.POST['game']
        
        current_sens = request.POST['current_sens']
        current_dpi = request.POST['current_dpi']
        current_sens = float(current_sens)
        current_dpi = float(current_dpi)
        

        if game != "VALORANT":
            new_sens = convert_to_val(game,current_sens)
            current_sens = new_sens
        
        game_sens = generate_sens_context(current_sens)
        
        context = {
            "all_sens": game_sens,
        }
        return render(request,"index.html",context)
    else:
        return render(request,"index.html")

def edpi_calculator(request):
    if request.method == "POST":
        current_sens = request.POST["current_sens"]
        current_dpi = request.POST["current_dpi"]
        current_dpi = float(current_dpi)
        current_sens = float(current_sens)

        edpi = current_dpi*current_sens

        context = {
            "edpi": edpi,
        }

        return render(request,"eDPI.html",context)
    else:
        return render(request,"eDPI.html")

def download_sensitivities(request):
    if request.method == "POST":
        sensitivities_data = request.POST.getlist("all_sens")

        df = pd.DataFrame([sensitivity.split(":") for sensitivity in sensitivities_data],columns=["Game","Sensitivity"])

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="sensitivities.csv"'
        df.to_csv(path_or_buf=response,index=False,encoding='utf-8')
        return response

def convert_to_val(game,sens):
    sens_map = {
        "Overwatch 2":10.6,
        "Destiny 2":10.6,
        "COD":10.6,
        "Counter-Strike 2":3.18,
        "Apex Legends": 3.18,
        "Rainbow 6":12.2,
    }
    
    factor = sens_map[game]
    # sens = float(sens)
    return (round(sens/factor,2))

def generate_sens_context(current_sens):
    
    sens_map = {
        "Overwatch 2":10.6,
        "Destiny 2":10.6,
        "COD":10.6,
        "Counter-Strike 2":3.18,
        "Apex Legends": 3.18,
        "Rainbow 6":12.2,
    }

    context = {}
    context["VALORANT"] = current_sens
    for key,factor in sens_map.items():
        print("Key,fact,current_sens: ",key,factor,current_sens)
        context[key] = round(current_sens * factor,2)

    print("Generated context: ", context)

    return context





    

