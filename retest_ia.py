import cv2
from ultralytics import YOLO

# 1. Chargement du modèle
model = YOLO('best.pt') 

# 2. Configuration Caméra
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # On monte en résolution pour mieux voir
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print("--- S.A.V.E.S : SYSTÈME POLYVALENT TOTAL ACTIVÉ ---")

while cap.isOpened():
    success, frame = cap.read()
    if not success: break
    frame = cv2.flip(frame, 1)

    # On utilise conf=0.35 pour être très sensible et ne rien rater
    results = model(frame, conf=0.35)

    detected_items = [] # Liste pour stocker tout ce qu'on voit à l'écran

    if results[0].boxes:
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id].lower()
            conf = box.conf[0]
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # --- LOGIQUE DE CLASSIFICATION LARGE (POLYVALENTE) ---
            color = (255, 255, 255) # Blanc par défaut
            category = "INFO"

            # Detection des mots-clés pour ne rien rater
            if any(word in label for word in ["stop", "no_entry", "enter", "red", "yield"]):
                color = (0, 0, 255) # Rouge (Arrêt/Danger)
                category = "URGENT"
            elif any(word in label for word in ["pedestrian", "work", "child", "cross", "danger", "bump", "curve"]):
                color = (0, 165, 255) # Orange (Attention)
                category = "PRUDENCE"
            elif any(word in label for word in ["speed", "limit", "max", "min"]):
                color = (255, 255, 0) # Cyan (Vitesse)
                category = "VITESSE"
            elif "green" in label:
                color = (0, 255, 0) # Vert (Libre)
                category = "VOIE LIBRE"

            # On ajoute l'objet à notre liste d'affichage
            detected_items.append(f"{label.upper()} ({conf:.2f})")

            # Dessin de la boite pour CHAQUE objet (pas d'oubli)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 3)
            cv2.putText(frame, label.upper(), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # --- AFFICHAGE DU TABLEAU DE BORD (HUD) ---
    # Fond noir à gauche pour lister les détections
    cv2.rectangle(frame, (0, 0), (350, 720), (0, 0, 0), -1)
    cv2.putText(frame, "S.A.V.E.S RADAR", (20, 40), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)
    cv2.line(frame, (20, 55), (300, 55), (255, 255, 255), 2)

    # Lister tous les panneaux vus en même temps
    y_pos = 100
    if not detected_items:
        cv2.putText(frame, "ROUTE LIBRE", (20, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    else:
        for item in detected_items:
            cv2.putText(frame, f"> {item}", (20, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
            y_pos += 40

    cv2.imshow("S.A.V.E.S - Vision Polyvalente", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()