# Análisis del desempeño de estudiantes

Proyecto de análisis exploratorio de datos utilizando el dataset **Students Performance in Exams** de Kaggle.

## Objetivo

Analizar el desempeño académico de estudiantes en las áreas de matemáticas, lectura y escritura, identificando patrones relacionados con el curso de preparación y el nivel educativo de los padres.

## Estructura del proyecto

```text
nombre-proyecto/
│
├── data/
│   └── dataset.csv
│
├── src/
│   └── analysis.py
│
├── outputs/
│   └── resultados/
│       ├── 01_promedio_por_area.png
│       ├── 02_rendimiento_academico.png
│       ├── 03_curso_preparacion.png
│       ├── 04_educacion_padres.png
│       ├── dataset_procesado.csv
│       ├── porcentaje_rendimiento.csv
│       ├── promedios_por_area.csv
│       ├── promedios_por_educacion_padres.csv
│       └── promedios_por_preparacion.csv
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Requisitos

- Python 3.10 o superior
- pandas
- matplotlib

## Instalación

Abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
pip install -r requirements.txt
```

## Ejecución

Desde la carpeta raíz del proyecto:

```bash
python src/analysis.py
```

## Variable creada

Se creó la variable:

`average_score`

Esta representa el promedio de:

- Math score
- Reading score
- Writing score

## Clasificación del rendimiento

Se utilizaron los siguientes criterios:

| Promedio | Categoría |
|---|---|
| 0 a 59.99 | Bajo |
| 60 a 79.99 | Medio |
| 80 a 100 | Alto |

## Análisis realizados

1. ¿Cuál de las tres áreas tiene el promedio más alto?
2. ¿Los estudiantes que completaron el curso de preparación presentan mejores resultados?
3. ¿Existen diferencias según el nivel educativo de los padres?
4. ¿Qué porcentaje de estudiantes alcanza un promedio de 70 puntos o más?

## Visualizaciones

El programa genera cuatro gráficas:

1. Promedio de calificaciones por área.
2. Cantidad de estudiantes por nivel de rendimiento.
3. Promedio según curso de preparación.
4. Promedio según nivel educativo de los padres.

## Conclusiones

El análisis permite observar diferencias entre las áreas académicas y entre distintos grupos de estudiantes. Lectura presenta el promedio más alto entre las tres áreas. Los estudiantes que completaron el curso de preparación presentan un promedio mayor que quienes no lo realizaron. También se observan diferencias en el promedio de acuerdo con el nivel educativo de los padres.

Estas relaciones son asociaciones observadas en el dataset y no deben interpretarse automáticamente como relaciones causales.

## Fuente

Kaggle. *Students Performance in Exams*.

Dataset original:
https://www.kaggle.com/datasets/spscientist/students-performance-in-exams
