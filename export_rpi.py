from ultralytics import YOLO

# 1. Chargement de ton modèle (le fichier best.pt téléchargé de Kaggle)
print("--- ÉTAPE 1 : Chargement du modèle best.pt ---")
model = YOLO('best.pt')

# 2. Exportation vers le format Raspberry Pi (TFLite)
# int8=True : On compresse les données pour que le Raspberry soit 3x plus rapide
print("--- ÉTAPE 2 : Conversion en cours... Cela peut prendre 3 minutes ---")
model.export(format='tflite', int8=True)

print("--- ÉTAPE 3 : Terminé avec succès ! ---")