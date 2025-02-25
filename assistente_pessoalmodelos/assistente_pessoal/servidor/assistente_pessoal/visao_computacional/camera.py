import cv2
import tensorflow as tf
import requests
import time
import os

detection_model = tf.saved_model.load('../modelos/ssd_mobilenet_v2_coco_1')
camera = cv2.VideoCapture(0)
image_path = "frame.jpg"

try:
    while True:
        ret, frame = camera.read()
        if not ret:
            break
        cv2.imwrite(image_path, frame)
        with open(image_path, 'rb') as image_file:
            files = {'image': (image_path, image_file, 'image/jpeg')}
            try:
                response = requests.post('http://localhost:5000/camera', files=files)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Erro ao enviar imagem: {e}")
        time.sleep(5)
except KeyboardInterrupt:
    print("Captura de câmera interrompida.")
finally:
    camera.release()
    if os.path.exists(image_path):
        os.remove(image_path)