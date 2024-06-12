import cv2
from super_gradients.training import models
from super_gradients.common.object_names import Models
model = models.get('yolo_nas_s', num_classes=26, checkpoint_path = 'C:/Users/D E L L/Desktop/SignSense/YOLONAS/model_weights/ckpt_best.pth')

output = model.predict_webcam()