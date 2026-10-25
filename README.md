# 🧠 Krypton — Predicción de Cancelación de Clientes (ML + Cloud)
[![Demo del Proyecto](https://img.youtube.com/vi/9KX1BNYt9XI/maxresdefault.jpg)](https://www.youtube.com/watch?v=9KX1BNYt9XI)

## Motor de Predicción de Churn (ML Engine)

Este repositorio contiene la arquitectura de datos, el pipeline de entrenamiento y los modelos predictivos desarrollados para el proyecto [**Krypton** (Simulación Laboral NoCountry)](https://github.com/proyectofintech-hackathon/ONE-II-LATAM--Predicci-n-de-Cancelaci-n-de-Clientes). El objetivo del sistema es predecir la probabilidad de cancelación de clientes (Churn) en una Fintech, priorizando la captura de clientes en riesgo para maximizar la efectividad de las campañas de retención.

> **👨‍💻 Mi Rol:** Responsable del ciclo de vida de los datos y modelos (Data Scientist / ML Engineer). Diseñé la arquitectura de modelos, implementé el Feature Engineering, lideré la experimentación con múltiples algoritmos y configuré la infraestructura de despliegue en Google Cloud Platform (GCP).

🔗 **[Documentación Técnica en Notion](https://app.notion.com/p/Proyecto-Krypton-2e8d24359eb3804caf3ac78204e8bfc5)** *(Incluye contexto de negocio, arquitectura de datos y actas del equipo).*

---

### 🎯 El Desafío de Negocio y la Estrategia de KPIs

El dataset presentaba un fuerte **desbalance de clases** (aprox. 84% clientes activos vs 16% cancelados). Un modelo que prediga siempre "no cancela" tendría un Accuracy del 84%, pero sería inútil para el negocio. Por lo tanto, la definición de los KPIs se centró en el impacto económico:

*   **Recall (Sensibilidad) - Target: > 80%.** 
    *   *Justificación:* El costo de retener a un cliente (Falso Positivo) es mucho menor al costo de perderlo (Falso Negativo). Priorizamos capturar la mayor cantidad de cancelaciones reales posibles.
*   **F1-Score - Target: > 0.60.** 
    *   *Justificación:* Regulador para asegurar que el modelo no sea excesivamente conservador, manteniendo una precisión viable para el equipo de marketing.
*   **PSI (Population Stability Index) - Target: < 0.1.** 
    *   *Justificación:* Vital para detectar si cambios en variables críticas invalidan el modelo en el tiempo.

---

### 🏆 Arquitectura Final: Estrategia Dual-Champion

Tras una exhaustiva experimentación (ver carpeta `legacy/`), se descartaron modelos como LightGBM (cuya calibración destruyó el Recall) y se definió una estrategia de dos modelos complementarios en producción:

1.  **Champion Masivo (XGBoost Classifier):** 
    *   *Uso:* Clasificación masiva para campañas de retención.
    *   *Configuración:* 400 árboles, `max_depth=3`, `scale_pos_weight` (5.22) para compensar el desbalanceo.
    *   *Valor:* Optimizado para **maximizar el Recall**. Es el encargado de escanear la base de datos completa y filtrar a los clientes en riesgo.
2.  **Champion Explicativo (CatBoost Classifier):** 
    *   *Uso:* Análisis detallado y generación de motivos.
    *   *Configuración:* Árboles simétricos (`depth=4`), regularización L2 (`l2_leaf_reg=5`) y soporte nativo para variables categóricas.
    *   *Valor:* Optimizado para **interpretabilidad**. Permite al negocio entender el *por qué* de la fuga y priorizar acciones específicas.

---

### 🔬 Experimentación y Decisiones Técnicas Clave

El pipeline de modelado (`02_Model_Development_Production.ipynb`) documenta un proceso riguroso de selección:

*   **Evaluación de 4 Algoritmos:** Se compararon Random Forest, LightGBM, XGBoost y CatBoost usando `GridSearchCV` optimizando la métrica de `recall`.
*   **La Decisión sobre la Calibración (LightGBM vs XGBoost):** Se probó calibrar las probabilidades de LightGBM con `CalibratedClassifierCV` (Isotonic). Aunque mejoró la precisión global, **el Recall cayó dramáticamente del 79% al 30%**. Por esta razón, LightGBM calibrado fue descartado para producción, priorizando el alto Recall de XGBoost para la fase masiva.
*   **Feature Engineering:** Se creó la variable `Low_Relationship_Count` (clientes con pocos productos), demostrando ser un fuerte indicador de fuga.
*   **Interpretabilidad con SHAP:** Se implementó el análisis de valores SHAP en el modelo CatBoost para extraer los motivos específicos de cada cliente.
*   **Umbrales de decisión:** Se desarrollaron funciones interactivas (`filtrar_clientes_por_probabilidad`) para que el equipo de negocio pueda ajustar dinámicamente el umbral de riesgo (ej. filtrar solo a aquellos con `Prob_Cancel > 0.9`) y analizar a los clientes de forma individual (`motivos_cancel`).


### 📂 Estructura del Repositorio

```text
Krypton-ml-engine/
├── data/
│   ├── raw/                    # Almacenamiento de registros originales (Inmutable)
│   └── processed/              # Datos tras la limpieza y feature engineering
├── docs/
│   └── glosario_variables.md   # Glosario técnico de variables
├── models/                     # Artefactos de producción (Modelos .pkl finales)
├── notebooks/                  # Código final (ETL y Modelado)
├── src/
│   └── predict.py              # Script de inferencia y simulación de producción
├── legacy/                     # Historial de experimentación y modelos descartados
├── requirements.txt            # Dependencias del proyecto (Pandas, XGBoost, CatBoost, etc.)
└── README.md
```

### 🚀 Uso Rápido (Inferencia)

Para probar cómo el backend consume el modelo en producción, puedes ejecutar el script de simulación. Asegúrate de tener las dependencias instaladas (pip install -r requirements.txt):

```bash
python src/predict.py
```

El script cargará el modelo XGBoost y CatBoost desde la carpeta models/, simulará los datos de un cliente y arrojará la probabilidad de cancelación.

### 📚 Documentación Adicional

📖 [Diccionario de Datos](https://github.com/Haruki-24/Krypton-ml-engine/blob/main/docs/glosario_variables.md): Glosario técnico de las variables utilizadas.

🗄️ [Archivo Legacy](https://github.com/Haruki-24/Krypton-ml-engine/tree/main/legacy): Repositorio histórico con las versiones de desarrollo (v1 a v4).


### 🛠️ Stack Tecnológico y Modelos Evaluados

A lo largo del proyecto se evaluaron distintas arquitecturas de Machine Learning para encontrar el mejor balance entre Recall e interpretabilidad. 

#### Modelos Implementados
* ![XGBoost](https://img.shields.io/badge/XGBoost-2C8EBB?style=flat-square&logo=xgboost&logoColor=white)    Modelo principal para predicción masiva de cancelaciones
* ![CatBoost](https://img.shields.io/badge/CatBoost-FFCC00?style=flat-square&logo=catboost&logoColor=black)    Modelo secundario para explicar los principales motivos de cancelaciones
* ![LightGBM](https://img.shields.io/badge/LightGBM-9C27B0?style=flat-square&logo=lightgbm&logoColor=white)    Modelo evaluado y descartado (Legacy)
* ![RandomForest](https://img.shields.io/badge/Random_Forest-4CAF50?style=flat-square&logo=scikit-learn&logoColor=white)    Modelo evaluado y descartado (Legacy)

#### Data Science & ML
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![SHAP](https://img.shields.io/badge/SHAP-Explicabilidad-FF6B6B?style=flat-square&logo=python&logoColor=white)

#### Cloud & MLOps
![GCP](https://img.shields.io/badge/Google_Cloud-4285F4?style=flat-square&logo=google-cloud&logoColor=white)
![Vertex AI](https://img.shields.io/badge/Vertex_AI-4285F4?style=flat-square&logo=google-cloud&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
