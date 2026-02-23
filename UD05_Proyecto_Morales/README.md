# UD05 Proyecto Final - Morales

## Dataset utilizado

Para el desarrollo del proyecto se ha utilizado el dataset **Sports Classification (100 clases deportivas)** disponible en Kaggle:

https://www.kaggle.com/datasets/gpiosenka/sports-classification

El dataset contiene aproximadamente 13.000 imágenes distribuidas en 100 clases, organizadas en carpetas de entrenamiento, validación y test.

---

## Fases completadas

El notebook incluye el desarrollo completo de:

- Fase 1 – Fundamentos
- Fase 2 – Experimentación sistemática
- Fase 3 – Excelencia
- Bonus Opción A – Ensemble de modelos

Todo el trabajo está integrado en un único notebook para facilitar la revisión y mantener continuidad en el análisis.

---

## Archivo principal

El proyecto se entrega en el archivo:

UD05_Proyecto_Morales_TodasFases.ipynb

Este notebook contiene:

- Exploración del dataset
- Construcción de la CNN base
- Experimentación sistemática (arquitectura, regularización y data augmentation)
- Tuning de hiperparámetros
- Gestión de desbalanceo
- Ablation study
- Análisis de confianza
- Ensemble de modelos
- Conclusiones finales

El notebook se entrega con todas las celdas ejecutadas y los outputs visibles.

---

## Entorno recomendado

- Python 3.10 o superior
- TensorFlow 2.16+
- GPU recomendada (Google Colab o entorno local)

Durante el desarrollo se trabajó inicialmente en Google Colab. Sin embargo, al aumentar la complejidad de los experimentos (múltiples modelos, tuning, ensemble y análisis avanzados), el consumo de memoria provocaba reinicios de sesión y pérdida de modelos entrenados.

Por este motivo, se migró el proyecto a entorno local. Esta transición redujo el tiempo disponible para completar algunos entrenamientos finales, aunque toda la estructura experimental y el código están completamente implementados.

---

## Instalación de dependencias

Instalar las dependencias necesarias:

```bash
pip install -r requirements.txt

## Dependencias principales

- tensorflow  
- numpy  
- pandas  
- matplotlib  
- seaborn  
- scikit-learn  
- pillow  

---

## Descarga del dataset

Mediante Kaggle CLI:

```bash
kaggle datasets download -d gpiosenka/sports-classification
unzip sports-classification.zip

## Estructura esperada del dataset
train/
valid/
test/


---

## Resultados principales

- **Baseline accuracy:** ~1%  
- **Accuracy Fase 1:** ~48%  
- **Mejor `val_accuracy`:** ~53%  
- **Test accuracy final:** ~49%  

El modelo final es una **CNN de tres bloques convolucionales**, incorporando **Dropout** como regularización y técnicas de **data augmentation** para mejorar la generalización.

---

## Observaciones finales

El proyecto está completamente desarrollado y documentado en un único notebook, incluyendo todas las fases requeridas.

Debido a limitaciones de recursos (memoria en Google Colab y tiempos de reentrenamiento en entorno local), algunos experimentos avanzados no alcanzaron su convergencia total.

Aun así, la lógica de experimentación, comparación de arquitecturas, análisis avanzado y bonus está correctamente implementada, mostrando de forma estructurada todo el proceso de diseño, evaluación y mejora de una CNN para clasificación multiclase.