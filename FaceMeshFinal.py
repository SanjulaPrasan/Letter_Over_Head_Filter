import sys
import time
import cv2
import numpy as np
import mediapipe as mp
import random
import string


mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
cap = cv2.VideoCapture(0)
window_name = 'img'

for x in range(100):
    timeout_start = time.time()
    with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as face_mesh:
        while time.time() < timeout_start + 5:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)
            height, width, _ = frame.shape
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(rgb_frame)
            if results.multi_face_landmarks:
                for idx in results.multi_face_landmarks:
                    pt1 = idx.landmark[109]
                    x = int(pt1.x * width)
                    y = int(pt1.y * height)
                    text = random.choice(string.ascii_uppercase)            
                    cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,255), 2, 2)

            cv2.imshow('img', frame)
            if cv2.waitKey(1) & 0xFF == 27 or cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
                cap.release()
                cv2.destroyAllWindows()
                sys.exit()

        while time.time() < timeout_start + 10:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(rgb_frame)
            if results.multi_face_landmarks:
                for idx in results.multi_face_landmarks:
                    pt1 = idx.landmark[109]
                    x = int(pt1.x * width)
                    y = int(pt1.y * height)
                    cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 0, 255), 2, 2)
            cv2.imshow('img', frame)
            if cv2.waitKey(1) & 0xFF == 27 or cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
                cap.release()
                cv2.destroyAllWindows()
                sys.exit()

cap.release()
cv2.destroyAllWindows()








