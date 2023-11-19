## Actividad 01
# Crear una lista con números que comiencen por 30 y que termine en 42 haciendo que el paso entre cada número consecutivo sea de 0.4. Sin usar Numpy.

def numberlist(inicial, final, consecutivo):
    list = []
    count = inicial
    while(count<=final):
        list.append(round(count, 1))
        count += consecutivo
    return list

print(numberlist(30,42,0.4))


## Actividad 02
# Dataset -> https://raw.githubusercontent.com/grammakov/USA-cities-and-states/master/us_cities_states_counties.csv
# Header -> City|State short|State full|County|City alias
# Obtener el número de ciudades que tiene el estado de Florida, usando dicho Dataset
# Sin usar Pandas
import requests
import urllib

#Download file csv
url = 'https://raw.githubusercontent.com/grammakov/USA-cities-and-states/master/us_cities_states_counties.csv'
# Devuelve un fichero desde una url como cadena de caracteres

file = urllib.request.urlopen(url).read().decode('utf-8').strip().split('\n')
listaset_ciudades = {}
ciudades = []
for element in file:
    lista_temp = element.split('|') 
    
    if(lista_temp[1] == 'FL'):
        ciudades.append(lista_temp[0])
        
listaset_ciudades = set(ciudades) 
print("El número de ciudades de florida son: ", len(listaset_ciudades))
print(listaset_ciudades)




