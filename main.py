from elasticsearch import Elasticsearch #Es importante usar la version de elasticsearch 6.4.0
from elasticsearch.helpers import scan
import pandas as pd
import os
import json
from datetime import datetime


#Revisar el requirements.txt
#============================


es = Elasticsearch(host='192.168.2.24', port=9200)

def get_data_from_elastic():
    current_folder = os.path.dirname(__file__)  # con esto puedo obtener la carpeta donde se ejecuta el codigo
    file = f"{current_folder}/elasticquery"
    f = open(file, "r", encoding='UTF-8')
    elasticquery = f.read()


    query = json.loads(elasticquery) # string a dictionary

    rel = scan(client=es,             
               query=query,
               size=10, #No tiene ningún efecto, por lo que la limitacion lo da la fecha
               scroll='1m',
               index='clipsx2018',
               raise_on_error=True,
               preserve_order=False,
               clear_scroll=True
               )

    # Keep response in a list.
    result = list(rel)

    temp = []

    # We need only '_source', which has all the fields required.
    # This elimantes the elasticsearch metdata like _id, _type, _index.
    for hit in result:
        temp.append(hit['_source'])

    # Create a dataframe.
    df = pd.DataFrame(temp)

    return df


def getData():

    df = get_data_from_elastic()

    if df.empty == True:
        print("No hay datos a procesar")

    else:

        # fecha = df[['fecha_lectura']]
        #
        # try:
        #     fechaConverted = datetime.strptime(fecha,
        #                                        "%Y-%m-%dT%H:%M:%S.%f")  # Fecha que viene desde ElasticSearch, en ocasiones viene con milisegundos
        #
        # except:
        #     fechaConverted = datetime.strptime(fecha,
        #                                        "%Y-%m-%dT%H:%M:%S")  # Fecha que viene desde ElasticSearch, sin milisegundos
        #
        # fechaConverted = fechaConverted.strftime("%d-%m-%Y %H:%M:%S")  # La vuelvo a convertir para insertarla en MS SQL


        #por cosas de tiempo, no alcanzo a convertir la fecha todavia.


        print(df.head())
        print(df.columns)
        print(df.size)
        lista = df[
            ['id_noticia','titular','texto','fecha_lectura' ]]
        # for index, row in lista.iterrows():
        #     # variables
        #     idnoticia = row["id_noticia"]
        #     titular = row["titular"]
        #     URL = row["link"]
        #     fecha = row["fecha_lectura"]

            # print(idnoticia,titular, URL, fecha)
        lista.to_excel("FIDAE_2018-2.xlsx")



if __name__ == '__main__':
    getData()