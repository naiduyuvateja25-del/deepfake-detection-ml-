import cv2
import os

def extract_frames(video_path, output_folder, label, max_frames=200):
    os.makedirs(os.path.join(output_folder, label), exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret or count >= max_frames:
            break

        save_path = os.path.join(output_folder, label, f"{os.path.basename(video_path)}_{count}.jpg")
        cv2.imwrite(save_path, frame)

        count += 1

    cap.release()