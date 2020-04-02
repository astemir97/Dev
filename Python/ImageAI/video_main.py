from imageai.Detection import VideoObjectDetection
import os
import cv2

execution_path = os.getcwd()

camera = cv2.VideoCapture(0)

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path , "yolo.h5"))
detector.loadModel()

video_path = detector.detectObjectsFromVideo(
    input_file_path=os.path.join(execution_path, "/src/video.mp4"),
    output_file_path=os.path.join(execution_path, "/src/new_video.mp4"),
    frames_per_second=40,
    log_progress=True,
    minimum_percentage_probability=30
)
print(video_path)
