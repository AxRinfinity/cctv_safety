import cv2
import numpy as np
import tensorflow as tf

# Load pre-trained model (you can replace this with your own model)
model = tf.keras.models.load_model('path_to_your_model.h5')

# Function to preprocess the input image
def preprocess_image(image):
    image = cv2.resize(image, (224, 224))  # Resize to match model input shape
    image = image / 255.0  # Normalize the image
    return np.expand_dims(image, axis=0)  # Add batch dimension

# Function to detect hazards in the video stream
def detect_hazards(video_source):
    cap = cv2.VideoCapture(video_source)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = preprocess_image(frame)
        prediction = model.predict(processed_frame)

        # Assuming the model outputs a probability for 'unsafe' condition
        if prediction[0][0] > 0.5:  # Threshold for unsafe condition
            cv2.putText(frame, "Hazard Detected!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            # Optionally add more actions like alerting or logging

        cv2.imshow('Warehouse Safety Monitor', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Main function to run the application
if __name__ == "__main__":
    video_source = 'path_to_your_video.mp4'  # Replace with your video source (e.g., CCTV feed)
    detect_hazards(video_source)
