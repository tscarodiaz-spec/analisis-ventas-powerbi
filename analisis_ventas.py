import pandas as pd

# Cargar el dataset
df = pd.read_csv("train.csv", encoding='latin-1')

# Ver primeras filas
print(df.head())

# Ver información general
print(df.info())

# Número de filas y columnas
print("Dimensiones:", df.shape)

# Estadísticas básicas
print(df.describe())

# Ver columnas
print("Columnas:", df.columns)

total_ventas = df["Sales"].sum()
print("Total de ventas:", total_ventas)

ventas_categoria = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print(ventas_categoria)

# Convertir fechas correctamente
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors='coerce')
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True, errors='coerce')

# Crear columna de mes
df["Mes"] = df["Order Date"].dt.to_period("M")

# Crear tiempo de envío (nivel pro)
df["Tiempo_Envio"] = (df["Ship Date"] - df["Order Date"]).dt.days

# Ventas por mes
ventas_mes = df.groupby("Mes")["Sales"].sum().sort_index()
print("\nVentas por mes:")
print(ventas_mes)

import matplotlib.pyplot as plt

# Convertir periodo a string para graficar
ventas_mes.index = ventas_mes.index.astype(str)

# Crear columna año
df["Año"] = df["Order Date"].dt.year

# Ventas por año
ventas_anio = df.groupby("Año")["Sales"].sum()

print(ventas_anio)

plt.figure()
plt.plot(ventas_anio.index, ventas_anio.values)

plt.title("Ventas por Año")
plt.xlabel("Año")
plt.ylabel("Ventas")

plt.show()

# Crear columna mes número
df["Mes_num"] = df["Order Date"].dt.month

# Ventas por mes (todos los años juntos)
ventas_mes_patron = df.groupby("Mes_num")["Sales"].sum()

print(ventas_mes_patron)

plt.figure()
plt.plot(ventas_mes_patron.index, ventas_mes_patron.values)

plt.title("Patrón de ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Ventas")

plt.show()

# Top 10 clientes por ventas
top_clientes = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)

print(top_clientes)

plt.figure()
plt.barh(top_clientes.index, top_clientes.values)

plt.title("Top 10 Clientes por Ventas")
plt.xlabel("Ventas")
plt.ylabel("Clientes")

plt.show()

# Total ventas general
total_ventas = df["Sales"].sum()

# Ventas del top 10
ventas_top10 = top_clientes.sum()

# Porcentaje
porcentaje = (ventas_top10 / total_ventas) * 100

print("Ventas Top 10:", ventas_top10)
print("Total ventas:", total_ventas)
print("Porcentaje Top 10:", porcentaje)

import matplotlib.pyplot as plt

# Ordenar clientes
ventas_clientes = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False)

# Acumulado
ventas_acumuladas = ventas_clientes.cumsum()
porcentaje_acumulado = ventas_acumuladas / ventas_clientes.sum()

# Gráfico
plt.figure()
plt.plot(porcentaje_acumulado.values)

plt.title("Curva de Pareto - Clientes")
plt.xlabel("Clientes (ordenados)")
plt.ylabel("Porcentaje acumulado de ventas")

plt.show()

# Encontrar el punto donde se alcanza el 80%
pareto_80 = porcentaje_acumulado[porcentaje_acumulado <= 0.8]

cantidad_clientes_80 = len(pareto_80)
total_clientes = len(ventas_clientes)

porcentaje_clientes = (cantidad_clientes_80 / total_clientes) * 100

print("Clientes necesarios para 80% de ventas:", cantidad_clientes_80)
print("Total clientes:", total_clientes)
print("Porcentaje de clientes:", porcentaje_clientes)

print("Filas totales:", len(df))

# Ver duplicados
duplicados = df.duplicated().sum()
print("Duplicados:", duplicados)

# Ver si Order ID se repite
print("Órdenes únicas:", df["Order ID"].nunique())