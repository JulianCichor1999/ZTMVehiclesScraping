from requests import get
from bs4 import BeautifulSoup
import csv

def list_split(listA, n):
    for x in range(0, len(listA), n):
        every_chunk = listA[x: n+x]

        if len(every_chunk) < n:
            every_chunk = every_chunk + \
                [None for y in range(n-len(every_chunk))]
        yield every_chunk

def add_text_to_list(name_of_element):
     for element in name_of_element:
        vehicles_list.append(element.get_text())

columns = ["No of vehicle", "Manufacturer", "Type", "Carrier", "Depot"]
vehicles_list = []

for i in range(1,106):
    if i == 1:
        URL = "https://www.ztm.waw.pl/baza-danych-pojazdow/"

    else:
        URL = "https://www.ztm.waw.pl/baza-danych-pojazdow/page/"+str(i)+"/"

    page = get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="ztm_vehicles_grid")

    vehicles = results.find_all("a", class_="grid-row-active")

    for vehicle in vehicles:
        number_manu_type = vehicle.find_all("div", class_="grid-col grid-col-sm")
        carrier = vehicle.find_all("div", class_="grid-col grid-col-lg grid-col-mb-hidden")
        depot = vehicle.find_all("div", class_="grid-col grid-col-md grid-col-tb-hidden")
        add_text_to_list(number_manu_type)
        add_text_to_list(carrier)
        add_text_to_list(depot)

    with open('C:\\Users\\Julian\\Desktop\\wozy.csv', 'w', newline='', encoding='utf-8') as file:
        vehicle_writer = csv.writer(file)
        vehicle_writer.writerow(columns)
        for element in list_split(vehicles_list,5):
            vehicle_writer.writerow(element)
