# 🚗 S.A.V.E.S — Smart Autonomous Vehicle Ecosystem and Safety

**S.A.V.E.S** est un projet de véhicule autonome intelligent centré sur la sécurité routière. Ce dépôt contient le module de **détection de panneaux de signalisation** : un modèle YOLO entraîné, ses exports pour l'embarqué et des scripts de test en temps réel avec une caméra.

## 🧩 Le projet S.A.V.E.S

Le dépôt présenté ici n'est qu'une partie du système global, qui comprend :

- un véhicule autonome (ROS 2 Humble, RPLidar A1, Jetson Nano) ;
- deux modèles de Deep Learning : détection de panneaux (ce dépôt) et détection de somnolence ;
- le signalement de collisions via MQTT ;
- une application mobile React Native (reconnaissance faciale, suivi GPS) ;
- un tableau de bord d'administration MERN.

## 🎯 Détection de panneaux

- **Modèle :** YOLO (Ultralytics 8.4.14), tâche de détection, images en 640×640
- **Entraînement :** réalisé sur Kaggle, sur un dataset d'environ 22 000 images augmentées
- **Classes :** 105 classes (limitations de vitesse, stop, cédez le passage, sens interdit, passages piétons, feux tricolores, virages, travaux, etc.)
- **Performance :** précision d'environ 0,80

Les courbes d'évaluation (matrice de confusion, courbes P / R / F1, résultats d'entraînement) sont dans le dossier [`evaluation/`](evaluation/).

## 📁 Contenu du dépôt

```
.
├── best.pt                 Poids du modèle entraîné (PyTorch)
├── best1.pt                Autre version des poids
├── best.onnx               Export ONNX
├── best_saved_model/       Exports TensorFlow / TFLite (float32, float16, int8)
├── evaluation/             Métriques et visualisations de l'entraînement
├── test_cam.py             Recherche et test de l'index de la caméra
├── test_panneaux.py        Détection simple avec ordre « STOP »
├── retest_ia.py            Détection avancée avec tableau de bord (HUD)
├── export_rpi.py           Export du modèle en TFLite int8 pour l'embarqué
└── urgent.mp3              Son d'alerte
```

## 🚀 Installation

### Prérequis
- Python 3.9 ou plus
- Une webcam

```bash
git clone https://github.com/EmnaRiahi/S.A.V.E.S-Smart-Autonomus-Vehicle-Ecosystem-Safety-.git
cd S.A.V.E.S-Smart-Autonomus-Vehicle-Ecosystem-Safety-
pip install ultralytics opencv-python
```

## ▶️ Utilisation

**1. Vérifier la caméra**
```bash
python test_cam.py
```

**2. Lancer la détection simple** (affiche un ordre de freinage à la détection d'un stop)
```bash
python test_panneaux.py
```

**3. Lancer le tableau de bord complet « S.A.V.E.S RADAR »**
```bash
python retest_ia.py
```
Les panneaux détectés sont classés par couleur :

| Couleur | Catégorie | Exemples |
|---|---|---|
| 🔴 Rouge | URGENT | stop, sens interdit, cédez le passage, feu rouge |
| 🟠 Orange | PRUDENCE | piétons, travaux, enfants, virages, ralentisseur |
| 🔵 Cyan | VITESSE | limitations de vitesse |
| 🟢 Vert | VOIE LIBRE | feu vert |

Appuyer sur **Q** pour quitter.

**4. Exporter le modèle pour l'embarqué**
```bash
python export_rpi.py
```
Génère une version TFLite quantifiée en int8, plus légère et plus rapide sur une carte embarquée.

## 🛠️ Technologies

Python · YOLO (Ultralytics) · OpenCV · ONNX · TensorFlow Lite · Kaggle · ROS 2 · Jetson Nano · MQTT · React Native · MERN

## 🔮 Pistes d'amélioration

- Harmoniser les noms de classes en double (ex. `Speed Limit 30`, `Speed Limit 30KM`, `speed_limit_30`)
- Intégrer l'alerte sonore (`urgent.mp3`) dans les scripts de détection
- Ajouter un script d'inférence pour la carte embarquée du véhicule

## 📄 Licence

*(à compléter)*

Ce projet utilise [Ultralytics YOLO](https://github.com/ultralytics/ultralytics), distribué sous licence AGPL-3.0.

## 👤 Auteure

**Emna Riahi** — étudiante en 5ème année du cycle ingénieur, option SLEAM, ESPRIT
