import os
import pathlib

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
from git import Repo

def load_model(model_name):
    print("Loading model" + model_name)
    base_url = 'http://download.tensorflow.org/models/object_detection/'
    model_file = model_name + '.tar.gz'
    model_dir = tf.keras.utils.get_file(
        fname=model_name, origin=base_url + model_file,untar=True)
    model_dir = pathlib.Path(model_dir)/"saved_model"
    model = tf.saved_model.load(str(model_dir))
    return model

def update_models():
    if "models" in pathlib.Path.cwd().parts:
        while "models" in pathlib.Path.cwd().parts:
            os.chdir('..')
    elif not pathlib.Path('models').exists():
        Repo.clone_from("https://github.com/tensorflow/models",
                        "C:/Users/Mel/PycharmProjects/AILabs/Lab 7/models", depth=1)

def add_google():
    if "google_images" in pathlib.Path.cwd().parts:
        while "google_images" in pathlib.Path.cwd().parts:
            os.chdir('..')
    elif not pathlib.Path('google_images').exists():
        Repo.clone_from("https://github.com/Joeclinton1/google-images-download.git",
                        "C:/Users/Mel/PycharmProjects/AILabs/Lab 7/google_images", depth=1)

def add_labelimg():
    if "labelImg" in pathlib.Path.cwd().parts:
        while "labelImg" in pathlib.Path.cwd().parts:
            os.chdir('..')
    elif not pathlib.Path('labelImg').exists():
        Repo.clone_from("https://github.com/tzutalin/labelImg.git",
                        "C:/Users/Mel/PycharmProjects/AILabs/Lab 7/labelImg", depth=1)