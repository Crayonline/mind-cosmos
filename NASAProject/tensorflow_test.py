import numpy as np
import pandas as pd

import tensorflow as tf

from tensorflow import feature_column
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split

import pathlib

csv_file = '/Users/jeffreyklinck/Desktop/NASAProject/training.csv'

dataframe = pd.read_csv(
    csv_file, names = ["SRB", "FP2", "FPz", "FP1", "FT10",
           "FT9", "T9", "T10","Emotion"])

emotion_features = dataframe.copy()
emotion_labels = dataframe.pop('Emotion')

emotion_features = np.array(emotion_features)


emotion_model = tf.keras.Sequential([
  layers.Dense(64),
  layers.Dense(1)
])

emotion_model.compile(loss = tf.keras.losses.MeanSquaredError(),
                      optimizer = tf.keras.optimizers.Adam())

emotion_model.fit(emotion_features, emotion_labels, epochs=10)
