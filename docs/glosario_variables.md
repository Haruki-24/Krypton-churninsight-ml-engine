# 📖 Diccionario de Datos: Proyecto Krypton (Churn Prediction)

Este documento define el diccionario de variables del dataset base utilizado para el entrenamiento del modelo de predicción de cancelación de clientes. Fue elaborado para estandarizar el lenguaje técnico entre los equipos de Data Engineering, Data Science y Negocio.

## 🎯 Variable Objetivo (Target)

| Variable | Tipo de Dato | Descripción | Valores / Observaciones |
| :--- | :--- | :--- | :--- |
| **Attrition_Flag** | Categórica (Binaria) | Indicador de cancelación de la tarjeta. | `0` = Cliente Activo (Abierta)<br>`1` = Cliente Cancelado (Cerrada) |

## 👤 Datos Demográficos del Cliente

| Variable | Tipo de Dato | Descripción | Observaciones |
| :--- | :--- | :--- | :--- |
| **CLIENTNUM** | Numérica (ID) | Número de identificación único del cliente. | Clave primaria. |
| **Customer_Age** | Numérica | Edad del cliente. | Años. |
| **Gender** | Categórica | Género del cliente. | `M` / `F` |
| **Dependent_count** | Numérica | Número de dependientes (hijos/familiares a cargo). | |
| **Education_Level** | Categórica | Nivel educativo máximo alcanzado. | Ej: Graduate, High School, Unknown. |
| **Marital_Status** | Categórica | Estado civil. | Ej: Married, Single, Divorced. |
| **Income_Category** | Categórica | Rango de ingresos anuales del cliente. | Ej: Less than $40K, $60K - $80K. |

## 💳 Datos de la Tarjeta y Relación Comercial

| Variable | Tipo de Dato | Descripción | Observaciones |
| :--- | :--- | :--- | :--- |
| **Card_Category** | Categórica | Categoría de la tarjeta de crédito. | Ej: Blue, Silver, Gold, Platinum. |
| **Months_on_book** | Numérica | Antigüedad del cliente en la relación con el banco. | En meses. |
| **Total_Relationship_Count**| Numérica | Cantidad total de productos financieros del cliente. | Ej: Tarjetas, préstamos, etc. |
| **Months_Inactive_12_mon** | Numérica | Número de meses inactivos en los últimos 12 meses. | |
| **Contacts_Count_12_mon** | Numérica | Cantidad de veces que el cliente contactó al banco (o viceversa) en 12 meses. | Indica nivel de acercamiento. |

## 💰 Comportamiento Financiero y Transaccional

| Variable | Tipo de Dato | Descripción | Observaciones |
| :--- | :--- | :--- | :--- |
| **Credit_Limit** | Numérica | Límite de crédito total aprobado. | |
| **Total_Revolving_Bal**| Numérica | Saldo total revolvente (deuda a pagar de la tarjeta). | |
| **Avg_Open_To_Buy** | Numérica | Límite de crédito promedio disponible (sin usar) en los últimos 12 meses. | |
| **Total_Amt_Chng_Q4_Q1**| Numérica | Variación porcentual del monto de transacciones entre Q4 y Q1. | Indica si gastó más o menos. |
| **Total_Trans_Amt** | Numérica | Monto total de las transacciones realizadas en los últimos 12 meses. | |
| **Total_Trans_Ct** | Numérica | Cantidad total (conteo) de transacciones en los últimos 12 meses. | |
| **Total_Ct_Chng_Q4_Q1** | Numérica | Variación porcentual en la cantidad de transacciones entre Q4 y Q1. | |
| **Avg_Utilization_Ratio**| Numérica | Promedio de utilización del límite de crédito. | Fórmula: (Total_Revolving_Bal / Credit_Limit) |
