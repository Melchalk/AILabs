import os
import pathlib

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from models.research.object_detection.utils import label_map_util
import init_funcs as start
import  inference_funcs as inference

PATH_TO_LABELS = 'models/research/object_detection/data/mscoco_label_map.pbtxt'
category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)
PATH_TO_TEST_IMAGES_DIR = pathlib.Path('models/research/object_detection/images/test')
TEST_IMAGE_PATHS = sorted(list(PATH_TO_TEST_IMAGES_DIR.glob("*.jpg")))

def photo_start():
    model_name = 'ssd_mobilenet_v1_coco_2017_11_17'

    detection_model = start.load_model(model_name)
    print(detection_model.signatures['serving_default'].inputs)
    # detection_model.signatures['serving_default'].output_dtypes

    for image_path in TEST_IMAGE_PATHS:
        inference.show_inference(detection_model, image_path, category_index)