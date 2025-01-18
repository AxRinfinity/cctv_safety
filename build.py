from sklearn.model_selection import train_test_split
import tensorflow as tf
from pipeline import FrameGenerator
import pandas as pd

dataframe = pd.read_csv('path_to_your_labels.csv')
train_df, val_df = train_test_split(dataframe, test_size=0.2)

train_generator = FrameGenerator(train_df)
val_generator = FrameGenerator(val_df)

base_model = tf.keras.applications.EfficientNetB0(include_top=False, input_shape=(10, 224, 224, 3))
base_model.trainable = False

model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling3D(),
    tf.keras.layers.Dense(1, activation='sigmoid')  # Binary classification (safe/unsafe)
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(train_generator,
          validation_data=val_generator,
          epochs=10,
          callbacks=[tf.keras.callbacks.EarlyStopping(patience=2)])

loss, accuracy = model.evaluate(val_generator)
print(f'Validation Loss: {loss}, Validation Accuracy: {accuracy}')
