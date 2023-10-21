import sys
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

MODEL_PATH = 'DMSNR_Curve_model.h5'

if len(sys.argv)==4:
    
    # Load Tensorflow model
    model = keras.models.load_model(MODEL_PATH)

    print(model.summary())

    arguments = sys.argv[1:]

    start = int(arguments[0])
    end = int(arguments[1])
    num = int(arguments[2])

    padded = tf.linspace(start, end, num)

    print(model.predict(padded))

else:
    print('start, end and num iterations numbers as arguments are expected')