from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.boe.es/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

boletin = soup.find_all("a", class_="link-contenedor-otro")

#print (boletin)
direcciones = list()
nombres= list()

for i in boletin:
	nombres.append(i.text)
	direcciones.append(i.get('href'))

#print(nombres)
#print(direcciones)

#CREAR UN DATAFRAME con PANDAS
df = pd.DataFrame({"Nombre": nombres, "Direccion": direcciones})
#print(df)

for x in range	(len(df)):
	if df.iloc[x]['Nombre'] == "Último BOE":
		print (df.iloc[x]['Nombre'], df.iloc[x]['Direccion'])
		UltimoBOE="https://www.boe.es" + str(df.iloc[x]['Direccion'])
		print (UltimoBOE)

page = requests.get(UltimoBOE)
soup = BeautifulSoup(page.content, 'html.parser')
TodaPagina = str(soup)

#print (soup)
inic = TodaPagina.find("sec125A")
fin = TodaPagina.find("sec125B")

print(inic,fin)
subastas = TodaPagina[inic:fin]
soup = BeautifulSoup(subastas, 'html.parser')
#subastas = TodaPagina.find_all("h3", id="sec125A")
print (soup)

Anuncios = soup.find_all("li")#, class_="puntoHTML")

direccionesHTML = list()

for i in Anuncios:
	direccionesHTML.append(i.get('href'))

print (direccionesHTML)

#CREAR UN DATAFRAME con PANDAS
dfBol = pd.DataFrame({"Direccion": direccionesHTML})
print(dfBol)