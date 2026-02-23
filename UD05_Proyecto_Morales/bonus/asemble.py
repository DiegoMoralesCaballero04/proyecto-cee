import numpy as np
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

from tensorflow import keras

MODEL_PATHS = [
    "../modelos/mejor_modelo_fase1.keras",
    "../modelos/mejor_modelo_fase2.keras",
    "../modelos/mejor_modelo_fase3.keras"
]

def load_models():
    return [keras.models.load_model(p) for p in MODEL_PATHS]

def ensemble_predict(models, X):
    preds = [m.predict(X, verbose=0) for m in models]
    avg_preds = np.mean(preds, axis=0)
    return np.argmax(avg_preds, axis=1)

if __name__ == "__main__":
    print("Ensemble script cargado correctamente.")