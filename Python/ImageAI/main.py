from imageai.Detection import ObjectDetection
import os

exec_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(exec_path, "/home/akokov/Рабочий стол/Python/resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()

list = detector.detectObjectsFromImage(
    input_image=os.path.join(exec_path, "/src/objects.jpg"),
    output_image_path=os.path.join(exec_path, "/src/new_objects.jpg"),
    minimum_percentage_probability=50,
    display_percentage_probability=True,
    display_object_name=True
)
