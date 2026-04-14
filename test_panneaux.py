import cv2
from ultralytics import YOLO

# 1. Charger TON modèle que tu viens de télécharger
# S'il n'est pas dans le même dossier, mets le chemin complet
model = YOLO('best.pt') 

# 2. Ouvrir la webcam
cap = cv2.VideoCapture(0)

print("--- SYSTÈME S.A.V.E.S : DÉTECTION DE PANNEAUX LANCÉE ---")
print("Appuyez sur 'q' pour quitter.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # 3. Lancer l'IA sur l'image de la caméra
    # conf=0.5 : On ne garde que si l'IA est sûre à plus de 50%
    results = model(frame, conf=0.5)

    # 4. Logique de décision S.A.V.E.S
    for r in results:
        for box in r.boxes:
            # Récupérer le nom de la classe détectée
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            
            # Afficher un message d'action selon le panneau
            msg = f"DETECTE : {label}"
            color = (0, 255, 0) # Vert

            if "stop" in label.lower():
                msg = "!!! ORDRE : STOP / FREINAGE !!!"
                color = (0, 0, 255) # Rouge
            
            cv2.putText(frame, msg, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

    # 5. Afficher le résultat visuel (avec les boîtes et les noms)
    annotated_frame = results[0].plot()
    cv2.imshow("S.A.V.E.S - Vision Artificielle", annotated_frame)

    # Quitter avec 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()