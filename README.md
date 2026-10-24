# 🧠 Krypton — Motor de Predicción de Churn (ML Engine)

Este repositorio contiene la arquitectura de datos, el pipeline de entrenamiento y los modelos predictivos desarrollados para el proyecto **Krypton** (NoCountry). El objetivo del sistema es predecir la probabilidad de cancelación de clientes (Churn), priorizando la captura de clientes en riesgo para maximizar la efectividad de las campañas de retención.

## 🎯 Estrategia de KPIs Técnicos y de Negocio

La definición de los KPIs no se basa en la exactitud global, sino en el impacto económico que tiene la pérdida de un cliente para la Fintech:

*   **Recall (Sensibilidad): Target 80% - 85%.** 
    *   *Justificación:* El costo de retener a un cliente (Falso Positivo) es mucho menor al costo de perderlo (Falso Negativo). Priorizamos capturar la mayor cantidad de cancelaciones reales.
*   **F1-Score: Target > 0.75.** 
    *   *Justificación:* Actúa como regulador para asegurar que el modelo no sea excesivamente conservador, manteniendo una precisión viable para el equipo de marketing.
*   **PSI (Population Stability Index): Target < 0.1.** 
    *   *Justificación:* Vital para detectar si cambios en variables críticas (límite de crédito, transacciones) invalidan el modelo en el tiempo.

## 🏗️ Arquitectura de Infraestructura y Pipeline

Para optimizar recursos y garantizar trazabilidad, se diseñó el siguiente flujo de trabajo:

*   **Infraestructura:** Despliegue en **Vertex AI (Colab Enterprise)** con instancias `e2-standard-2` (2 vCPUs, 8 GB RAM) y apagado automático para optimizar la prueba gratuita de GCP.
*   **Pipeline (4 Capas):**
    1.  **Ingesta:** Carga inmutable desde `/data/raw`.
    2.  **Transformación (ETL):** Procesamiento de variables críticas (`Income_Category`, `Total_Trans_Ct`), manejo de nulos y normalización.
    3.  **Modelado:** Split 80/20, entrenamiento con ensambles (XGBoost / Random Forest).
    4.  **Evaluación:** Validación cruzada y registro de experimentos con **MLflow**.

## 📂 Estructura del Repositorio

```txt
├── docs                # Documentos de arquitectura y consulta general
├── data                # Datos del equipo de data science
|   ├── raw             # Almacenamiento de registros originales (Inmutable).
|   └── processed       # Datos tras la limpieza y feature engineering.
├── notebooks           # Segmentación por prefijos para trazabilidad 
├── src                 # Scripts de producción para el pipeline.
|   ├── data            # Scripts de limpieza
|   └── models          # Scripts de entrenamiento
├── requirements.txt    # Control de versiones de librerías (Pandas, Scikit-Learn, XGBoost).
└── README.md
```

