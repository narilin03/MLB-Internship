import os      
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
os.environ['TF_ENABLE_ONEDNN_OPTS']='0'

import tensorflow as tf       
import keras   

print("TensorFlow:",tf.__version__)
print("Keras:",keras.__version__)

print("TensorFlow and Keras imported successfully.")
