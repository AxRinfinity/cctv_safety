import tensorflow as tf
import numpy as np
import pandas as pd

class FrameGenerator(tf.keras.utils.Sequence):
    def __init__(self, dataframe, batch_size=32, n_frames=10):
        self.dataframe = dataframe
        self.batch_size = batch_size
        self.n_frames = n_frames
        self.indices = self.dataframe.index.tolist()

    def __len__(self):
        return int(np.ceil(len(self.dataframe) / self.batch_size))

    def __getitem__(self, idx):
        batch_indices = self.indices[idx * self.batch_size:(idx + 1) * self.batch_size]
        frames, labels = [], []

        for i in batch_indices:
            video_path = self.dataframe.iloc[i]['video_path']
            label = self.dataframe.iloc[i]['label']
            frames_sequence = []

            # Load frames for the video
            for j in range(self.n_frames):
                frame_path = f"{video_path}/frame_{j:04d}.jpg"  # Adjust based on your naming convention
                img = tf.keras.preprocessing.image.load_img(frame_path, target_size=(224, 224))
                img_array = tf.keras.preprocessing.image.img_to_array(img) / 255.0  # Normalize
                frames_sequence.append(img_array)

            frames.append(np.array(frames_sequence))
            labels.append(label)

        return np.array(frames), np.array(labels)

# Load your CSV with video paths and labels
dataframe = pd.read_csv('path_to_your_labels.csv')
