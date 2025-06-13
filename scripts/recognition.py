import os
import cv2
import face_recognition
import numpy as np

# Caminhos das pastas
faces_dir = "faces"
frames_dir = "frames"

# Carrega os rostos conhecidos
known_face_encodings = []
known_face_names = []

print("[INFO] Carregando rostos conhecidos...")
for filename in os.listdir(faces_dir):
    filepath = os.path.join(faces_dir, filename)
    image = face_recognition.load_image_file(filepath)
    encodings = face_recognition.face_encodings(image)
    if encodings:
        known_face_encodings.append(encodings[0])
        name = os.path.splitext(filename)[0]
        known_face_names.append(name)
    else:
        print(f"[AVISO] Nenhum rosto detectado em {filename}")

# Assume que há apenas uma imagem na pasta frames
frame_files = [f for f in os.listdir(frames_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
if not frame_files:
    print("Nenhuma imagem encontrada na pasta 'frames'.")
    exit()

frame_path = os.path.join(frames_dir, frame_files[0])
frame = cv2.imread(frame_path)
rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Localiza e codifica os rostos na imagem do frame
face_locations = face_recognition.face_locations(rgb_frame)
face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

print(f"[INFO] {len(face_encodings)} rosto(s) encontrado(s) na imagem.")

# Reconhecimento
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

    name = "Desconhecido"
    color = (0, 0, 255)  # vermelho
    percentage = 0.0

    if len(face_distances) > 0:
        best_match_index = np.argmin(face_distances)
        distance = face_distances[best_match_index]
        percentage = max(0, 1 - distance) * 100

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            if percentage >= 90:
                color = (0, 255, 0)  # verde
            else:
                color = (128, 0, 128)  # roxo

    label = f"{name} ({percentage:.2f}%)"

    cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
    cv2.putText(frame, label, (left + 6, bottom - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

# Redimensiona a imagem para 200x200 antes de mostrar, mantendo proporção
desired_size = 1000

height, width = frame.shape[:2]
scale = desired_size / max(height, width)
new_width = int(width * scale)
new_height = int(height * scale)

resized_frame = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_AREA)

cv2.imshow("Reconhecimento de Faces", resized_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
