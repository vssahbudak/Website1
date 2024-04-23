from django.shortcuts import render,redirect
from django.http import HttpResponse
import os
import folium
import pandas
import openpyxl

# Create your views here.

def map(request):
    ### CUSTOM MAP DENEMESİ ################
    # attr =('&copy; CNES, Distribution Airbus DS, © Airbus DS, © PlanetObserver (Contains Copernicus Data) | &copy; <a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors')
    # tiles= "https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png"
    # m = folium.Map(location=(37.85,27.85),tiles=tiles,attr=attr,zoom_start=8)

    
    
    veri = pandas.read_excel('static/city.xlsx')
    enlem = list(veri['enlem'])
    boylam = list(veri['boylam'])
    etiket = list(veri['city'])
    dene1 = list(veri['dene1'])
    dene2 = list(veri['dene2'])
    refno = list(veri['refno'])

    # folium.Circle için koşullar olusturduk#######
    def circle_renk(refno):
        if refno < 20:
            return "green"
        elif refno < 50:
            return "blue"
        else:
            return "red"
    
    def circle_cap(refno):
        if refno < 20:
            return 100
        elif refno < 50:
            return 500
        else:
            return 1000

    
    

    olay_harita = folium.FeatureGroup(name='Olay Haritası') #Ana harita üzerinde olay haritası katmanı olusturduk
    aadvs_harita = folium.FeatureGroup(name='AADVS Haritası')

    m = folium.Map(location=(37.85,27.85),zoom_start=8)
    m.add_child(folium.Marker(location=(37.85,27.85),icon=folium.Icon(color="blue"),popup="Aydın"))

    # for en , boy , eti in zip(enlem,boylam,etiket):
    #     m.add_child(folium.Marker(location=[en,boy],icon=folium.Icon(color='green'),popup=eti))

    ## Asagıdaki for olay haritası katmanı için ######
    for d1 , d2 , eti , ref in zip(dene1,dene2,etiket,refno):
        olay_harita.add_child(folium.Circle(location=(d1,d2),radius=circle_cap(ref),color=circle_renk(ref),
                                  fill_color=circle_renk(ref),
                                  fill_opacity=0.6,popup=eti))

    ## Asağıdaki FOR AADVS Haritası için
    for en, boy, in zip(enlem,boylam):
        aadvs_harita.add_child(folium.Circle(location=(en,boy),radius=100,color='green',
                                             fill_color='lightgreen',fill_opacity=0.8))
## for örnegi ##################
    # koordinatinatlar =[[37.80,27.80],[37.82,27.82],[37.83,27.83]]
    # dongulistesi = ["Dongu 1","Dongu 2","Dongu 3"]
    # for koor,dongu in zip(koordinatinatlar,dongulistesi): # FOR DÖNGÜSÜ 1 DEN FAZLA LİSTE İÇİN
    #     m.add_child(folium.Marker(location=koor,icon=folium.Icon(color="blue"),popup=dongu))
##########################
    m.add_child(olay_harita)
    m.add_child(aadvs_harita)
    m.add_child(folium.LayerControl())
    
    m = m._repr_html_()

    context={
        'mymap':m
    }
    
    return render(request,'map/map.html',context)









  