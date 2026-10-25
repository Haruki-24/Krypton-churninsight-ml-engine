"""
Krypton ML Engine - Script de Inferencia (Producción)
------------------------------------------------------
Este script simula el consumo de los modelos "Champion" por parte del backend.
Carga los modelos serializados desde la carpeta /models y realiza una predicción
sobre un cliente de ejemplo.
"""

import pickle
import pandas as pd
import os

# --- 1. Configuración de Rutas ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")

PATH_XGBOOST = os.path.join(MODELS_DIR, "champion_massive_xgboost.pkl")
PATH_CATBOOST = os.path.join(MODELS_DIR, "champion_explain_catboost.pkl")

# --- 2. Carga de los Modelos ---
def cargar_modelo(path):
    """Carga un modelo entrenado desde un archivo .pkl"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"⚠️ No se encontró el modelo en: {path}")
    with open(path, 'rb') as file:
        return pickle.load(file)

print("🔄 Cargando modelos Champion...")
try:
    model_xgboost = cargar_modelo(PATH_XGBOOST)
    model_catboost = cargar_modelo(PATH_CATBOOST)
    print("✅ Modelos cargados exitosamente.\n")
except Exception as e:
    print(f"❌ Error al cargar modelos: {e}")
    exit()

# --- 3. Definición del Cliente de Ejemplo ---
cliente_nuevo = {
    'Customer_Age': 45,
    'Months_Inactive_12_mon': 3,
    'Contacts_Count_12_mon': 2,
    'Total_Ct_Chng_Q4_Q1': 0.75,
    'Avg_Utilization_Ratio': 0.85,      # Alta utilización (riesgo)
    'Low_Relationship_Count': 1,        # Pocos productos (riesgo)
    'Gender_M': 1,
    'Card_Category_Gold': 0,
    'Card_Category_Platinum': 0,
    'Card_Category_Silver': 1
}

# Convertimos el diccionario a un DataFrame (como espera el modelo)
df_cliente = pd.DataFrame([cliente_nuevo])

# --- 4. Inferencia ---
print("👤 Datos del Cliente ingresado:")
print(df_cliente.T.to_string(header=False))
print("\n🔮 Generando predicciones...\n")

# Predicción XGBoost (Masivo - Recall Alto)
# predict_proba devuelve [prob_clase_0, prob_clase_1]
prob_xgb = model_xgboost.predict_proba(df_cliente)[0][1]

# Predicción CatBoost (Explicativo)
prob_cat = model_catboost.predict_proba(df_cliente)[0][1]

# --- 5. Resultados ---
print("=========================================")
print("RESULTADOS DEL MOTOR DE PREDICCIÓN")
print("=========================================")
print(f"Modelo Masivo (XGBoost):")
print(f"   Probabilidad de Cancelación: {prob_xgb:.2%}")
if prob_xgb > 0.5:
    print("   🚨 ACCIÓN: Cliente en Alto Riesgo. Derivar a campaña de retención.\n")
else:
    print("   ✅ ACCIÓN: Cliente estable. Monitoreo rutinario.\n")

print(f"2️⃣ Modelo Explicativo (CatBoost):")
print(f"   Probabilidad de Cancelación: {prob_cat:.2%}")
print("=========================================")
