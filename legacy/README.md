# 🗄️ Archivo Histórico (Legacy Code)

Esta carpeta contiene los cuadernos de trabajo (notebooks), scripts y modelos experimentales originales del proyecto **Krypton**. 

Fueron mis primeros pasos en Data Science dentro de un proyecto colaborativo. He decidido conservarlos sin refactorizar como un registro de mi evolución técnica y para mostrar el "detrás de escena" del desarrollo.

> **💡 ¿Por qué guardar esto?** En la ciencia de datos real, el 80% de los modelos que se prueban terminan descartándose. Documentar el fracaso y la iteración es tan importante como mostrar el modelo final.

---

## 📂 ¿Qué hay en esta carpeta?

### 🧪 `etl/` y `limpieza/`
Versiones preliminares del pipeline de datos. Incluyen los primeros borradores de limpieza de valores nulos, formateo de variables monetarias y normalización.
*   *Evolución:* Estos borradores fueron consolidados en el notebook final `01_ETL_Data_Cleaning.ipynb` de la carpeta principal.

### 🤖 `modelado/`
El historial de experimentación con diferentes algoritmos:
*   **v1 y v2:** Modelos iniciales (Random Forest y XGBoost) con hiperparámetros por defecto. Útiles para establecer un baseline.
*   **v3 y v4:** Experimentos con CatBoost y arquitecturas más complejas. En estas versiones se realizaron las pruebas de **calibración de probabilidades** que finalmente resultaron en una caída drástica del Recall, motivo por el cual fueron descartados para la fase masiva.

### 📦 `models/`
Los artefactos `.pkl` de los modelos experimentales que no pasaron a producción:
*   `champion1_lightgbm_descartado.pkl`: Un modelo LightGBM subentrenado (`n_estimators=50`, `learning_rate=0.005`) que solo utilizaba 4 de 10 features.
*   `champion2_random_forest_descartado.pkl`: Un Random Forest con profundidad ilimitada (`None`), 200 árboles y sin `random_state`, lo que lo hacía muy pesado para inferencia y difícil de reproducir.

---

## 🚀 El Código de Producción

Para ver la versión final, limpia y optimizada del proyecto, por favor dirígete a la **carpeta raíz del repositorio**, donde encontrarás:
*   El pipeline de ETL definitivo.
*   El notebook de modelado final (`02_Model_Development_Production.ipynb`).
*   La estrategia **Dual-Champion** (XGBoost + CatBoost).
*   El script de inferencia (`src/predict.py`).
