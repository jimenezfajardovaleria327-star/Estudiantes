import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================
# CONFIGURACIÓN
# =========================

# Define la ruta relativa dinámica hacia la carpeta data
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "dataset.csv")

# Definición del directorio de salida (se crea si no existe)
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs", "resultados")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Cargar el dataset
df = pd.read_csv(data_path)

# Limpiar posibles espacios o comillas en los nombres de las columnas
df.columns = df.columns.str.replace('"', '').str.strip()

print("=" * 50)
print("ANÁLISIS DE DESEMPEÑO DE ESTUDIANTES")
print("=" * 50)

# =========================
# 2. EXPLORACIÓN INICIAL
# =========================
print("\n1. NÚMERO DE REGISTROS")
print(df.shape[0])

print("\n2. NÚMERO DE COLUMNAS")
print(df.shape[1])

print("\n3. NOMBRES DE LAS VARIABLES")
print(df.columns.tolist())

print("\n4. TIPOS DE DATOS")
print(df.dtypes)

print("\n5. VALORES FALTANTES")
print(df.isnull().sum())

print("\n6. REGISTROS DUPLICADOS")
print(df.duplicated().sum())

print("\n7. ESTADÍSTICAS DESCRIPTIVAS")
print(df.describe())

# =========================
# 3. LIMPIEZA
# =========================
df = df.drop_duplicates()
df = df.dropna()

# =========================
# 4. CREAR AVERAGE_SCORE
# =========================
df["average_score"] = (
    df["math score"] +
    df["reading score"] +
    df["writing score"]
) / 3

df["average_score"] = df["average_score"].round(2)

# =========================
# 5. CLASIFICACIÓN
# Bajo: 0-59
# Medio: 60-79
# Alto: 80-100
# =========================
def clasificar_rendimiento(promedio):
    if promedio < 60:
        return "Bajo"
    elif promedio < 80:
        return "Medio"
    else:
        return "Alto"

df["performance"] = df["average_score"].apply(clasificar_rendimiento)

# =========================
# 6. ANÁLISIS 1
# ¿Cuál área tiene el promedio más alto?
# =========================
promedios_areas = df[
    ["math score", "reading score", "writing score"]
].mean().round(2)

print("\n" + "=" * 50)
print("ANÁLISIS 1: PROMEDIO POR ÁREA")
print("=" * 50)
print(promedios_areas)

area_mayor = promedios_areas.idxmax()
print("Área con mayor promedio:", area_mayor)
print("Promedio:", promedios_areas.max())

# =========================
# 7. ANÁLISIS 2
# Curso de preparación
# =========================
promedios_preparacion = (
    df.groupby("test preparation course")["average_score"]
    .mean()
    .round(2)
)

print("\n" + "=" * 50)
print("ANÁLISIS 2: CURSO DE PREPARACIÓN")
print("=" * 50)
print(promedios_preparacion)

if "completed" in promedios_preparacion.index and "none" in promedios_preparacion.index:
    diferencia = round(
        promedios_preparacion["completed"] -
        promedios_preparacion["none"], 2
    )
    print("Diferencia entre completed y none:", diferencia)

# =========================
# 8. ANÁLISIS 3
# Educación de los padres
# =========================
promedios_padres = (
    df.groupby("parental level of education")["average_score"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)

print("\n" + "=" * 50)
print("ANÁLISIS 3: EDUCACIÓN DE LOS PADRES")
print("=" * 50)
print(promedios_padres)

# =========================
# 9. ANÁLISIS 4
# Porcentaje con promedio >= 70
# =========================
porcentaje_70 = round((df["average_score"] >= 70).mean() * 100, 2)

print("\n" + "=" * 50)
print("ANÁLISIS 4: PROMEDIO >= 70")
print("=" * 50)
print("Porcentaje:", porcentaje_70, "%")

distribucion = df["performance"].value_counts()
porcentajes = (
    df["performance"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("\nDistribución del rendimiento:")
print(distribucion)
print("\nPorcentajes:")
print(porcentajes)

# =========================
# 10. GUARDAR RESULTADOS
# =========================
df.to_csv(
    os.path.join(OUTPUT_DIR, "dataset_procesado.csv"),
    index=False
)

promedios_areas.to_csv(
    os.path.join(OUTPUT_DIR, "promedios_por_area.csv")
)

promedios_preparacion.to_csv(
    os.path.join(OUTPUT_DIR, "promedios_por_preparacion.csv")
)

promedios_padres.to_csv(
    os.path.join(OUTPUT_DIR, "promedios_por_educacion_padres.csv")
)

porcentajes.to_csv(
    os.path.join(OUTPUT_DIR, "porcentaje_rendimiento.csv")
)

# =========================
# 11. VISUALIZACIÓN 1
# Promedio por área
# =========================
plt.figure(figsize=(8, 5))
promedios_areas.plot(kind="bar")
plt.title("Promedio de calificaciones por área")
plt.xlabel("Área")
plt.ylabel("Promedio")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "01_promedio_por_area.png"))
plt.close()

# =========================
# 12. VISUALIZACIÓN 2
# Rendimiento académico
# =========================
plt.figure(figsize=(8, 5))
distribucion.plot(kind="bar")
plt.title("Cantidad de estudiantes por rendimiento")
plt.xlabel("Rendimiento")
plt.ylabel("Cantidad de estudiantes")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "02_rendimiento_academico.png"))
plt.close()

# =========================
# 13. VISUALIZACIÓN 3
# Curso de preparación
# =========================
plt.figure(figsize=(8, 5))
promedios_preparacion.plot(kind="bar")
plt.title("Promedio según curso de preparación")
plt.xlabel("Curso de preparación")
plt.ylabel("Promedio")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "03_curso_preparacion.png"))
plt.close()

# =========================
# 14. VISUALIZACIÓN 4
# Educación de los padres
# =========================
plt.figure(figsize=(9, 5))
promedios_padres.sort_values().plot(kind="barh")
plt.title("Promedio según nivel educativo de los padres")
plt.xlabel("Promedio")
plt.ylabel("Nivel educativo de los padres")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "04_educacion_padres.png"))
plt.close()

print("\n" + "=" * 50)
print("ANÁLISIS TERMINADO")
print("=" * 50)
print("Los resultados se guardaron en:", OUTPUT_DIR)