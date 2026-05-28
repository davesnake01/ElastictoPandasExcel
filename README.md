# ElastictoPandasExcel

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Elasticsearch](https://img.shields.io/badge/elasticsearch-7.x%20%7C%208.x-yellow.svg)
![Pandas](https://img.shields.io/badge/pandas-data%20analysis-darkblue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

`ElastictoPandasExcel` es una herramienta utilitaria desarrollada en Python diseñada para automatizar la extracción de datos e índices desde **Elasticsearch**, su posterior conversión y estructuración en DataFrames de **Pandas**, y finalmente su exportación limpia a archivos legibles de **Microsoft Excel** (`.xlsx`).

Esta solución es ideal para ingenieros de datos, analistas y administradores de sistemas que necesitan transformar datos complejos de logs, métricas o documentos almacenados en clusters de Elasticsearch en reportes listos para el negocio y auditorías.

## 🛠️ Estructura del Proyecto

El repositorio mantiene la siguiente estructura modular:

```text
├── main.py           # Script principal, lógica de consulta a Elasticsearch y exportación.
├── requirements.txt  # Dependencias del proyecto (Elasticsearch, Pandas, Openpyxl).
└── .idea/            # Configuraciones del entorno de desarrollo (PyCharm).
