import time
import cv2
import numpy as np
import mediapipe as mp
import random
import string

# def face():
#     mp_drawing = mp.solutions.drawing_utils
#     mp_face_mesh = mp.solutions.face_mesh
#
#     timeout_start = time.time()
#     cap = cv2.VideoCapture(0)
#     with mp_face_mesh.FaceMesh(
#         max_num_faces=1,
#         refine_landmarks=True,
#         min_detection_confidence=0.5,
#         min_tracking_confidence=0.5
#     ) as face_mesh:
#         while time.time() < timeout_start + 5:
#             ret, frame = cap.read()
#             frame = cv2.flip(frame, 1)
#             rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             results = face_mesh.process(rgb_frame)
#             if results.multi_face_landmarks:
#                 text = random.choice(string.ascii_uppercase)
#                 cv2.putText(frame, text, (280, 130), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 4)
#
#             cv2.imshow('img', frame)
#             cv2.waitKey(1)
#         while time.time() < timeout_start + 10:
#             ret, frame = cap.read()
#             frame = cv2.flip(frame, 1)
#             cv2.putText(frame, text, (280, 130), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
#             cv2.imshow('img', frame)
#             cv2.waitKey(1)

def main():
    mp_drawing = mp.solutions.drawing_utils
    mp_face_mesh = mp.solutions.face_mesh
    cap = cv2.VideoCapture(0)

    for x in range(5):
        timeout_start = time.time()
        with mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        ) as face_mesh:
            while time.time() < timeout_start + 5:
                ret, frame = cap.read()
                frame = cv2.flip(frame, 1)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = face_mesh.process(rgb_frame)
                if results.multi_face_landmarks:
                    text = random.choice(string.ascii_uppercase)
                    cv2.putText(frame, text, (280, 130), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 4)

                cv2.imshow('img', frame)
                cv2.waitKey(1)
            while time.time() < timeout_start + 10:
                ret, frame = cap.read()
                frame = cv2.flip(frame, 1)
                cv2.putText(frame, text, (280, 130), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
                cv2.imshow('img', frame)
                cv2.waitKey(1)
        # while time.time() < timeout_start + 15:
        #     ret, frame = cap.read()
        #     frame = cv2.flip(frame, 1)
        #     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #     results = face_mesh.process(rgb_frame)
        #     if results.multi_face_landmarks:
        #         text = random.choice(string.ascii_uppercase)
        #         cv2.putText(frame, text, (280, 130), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 4)
        #
        #     cv2.imshow('img', frame)
        #     cv2.waitKey(1)
        # while time.time() < timeout_start + 20:
        #     ret, frame = cap.read()
        #     frame = cv2.flip(frame, 1)
        #     cv2.putText(frame, text, (280, 130), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
        #     cv2.imshow('img', frame)
        #     cv2.waitKey(1)
        # while time.time() < timeout_start + 25:
        #     ret, frame = cap.read()
        #     frame = cv2.flip(frame, 1)
        #     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #     results = face_mesh.process(rgb_frame)
        #     if results.multi_face_landmarks:
        #         text = random.choice(string.ascii_uppercase)
        #         cv2.putText(frame, text, (280, 130), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 4)
        #
        #     cv2.imshow('img', frame)
        #     cv2.waitKey(1)
        # while time.time() < timeout_start + 30:
        #     ret, frame = cap.read()
        #     frame = cv2.flip(frame, 1)
        #     cv2.putText(frame, text, (280, 130), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
        #     cv2.imshow('img', frame)
        #     cv2.waitKey(1)
        # while time.time() < timeout_start + 35:
        #     ret, frame = cap.read()
        #     frame = cv2.flip(frame, 1)
        #     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #     results = face_mesh.process(rgb_frame)
        #     if results.multi_face_landmarks:
        #         text = random.choice(string.ascii_uppercase)
        #         cv2.putText(frame, text, (280, 130), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 4)
        #
        #     cv2.imshow('img', frame)
        #     cv2.waitKey(1)
        # while time.time() < timeout_start + 40:
        #     ret, frame = cap.read()
        #     frame = cv2.flip(frame, 1)
        #     cv2.putText(frame, text, (280, 130), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
        #     cv2.imshow('img', frame)
        #     cv2.waitKey(1)
        # while time.time() < timeout_start + 45:
        #     ret, frame = cap.read()
        #     frame = cv2.flip(frame, 1)
        #     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #     results = face_mesh.process(rgb_frame)
        #     if results.multi_face_landmarks:
        #         text = random.choice(string.ascii_uppercase)
        #         cv2.putText(frame, text, (280, 130), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 4)
        #
        #     cv2.imshow('img', frame)
        #     cv2.waitKey(1)
        # while time.time() < timeout_start + 50:
        #     ret, frame = cap.read()
        #     frame = cv2.flip(frame, 1)
        #     cv2.putText(frame, text, (280, 130), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
        #     cv2.imshow('img', frame)
        #     cv2.waitKey(1)



main()






