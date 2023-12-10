from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.core.window import Window
from kivy.logger import Logger

import cv2
import tensorflow as tf
from layers import L1Dist
import os
import numpy as np

class CamApp(App):
    def build(self):
        # Set window properties
        Window.size = (400, 600)
        Window.clearcolor = (0.9, 0.9, 0.9, 1)  # Classic background color

        # Create layout components
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        # Webcam display
        self.web_cam = Image(size_hint=(1, 0.8))
        layout.add_widget(self.web_cam)

        # Verification button
        self.button = Button(text="Verify", on_press=self.verify, size_hint=(1, 0.1))
        self.button.background_color = (0.2, 0.6, 1, 1)  # Set initial button background color
        layout.add_widget(self.button)

        # Verification label
        self.verification_label = Label(text="Verification Uninitiated", size_hint=(1, 0.1), color=(0.2, 0.2, 0.2, 1))
        layout.add_widget(self.verification_label)

        # Load TensorFlow model
        self.model = tf.keras.models.load_model('siamesemodelv2.h5', custom_objects={'L1Dist': L1Dist})

        # Setup video capture device
        self.capture = cv2.VideoCapture(0)

        # Trigger the update loop 33 times every second
        Clock.schedule_interval(self.update, 1.0 / 33.0)

        return layout

    # Update function to continuously get webcam feed
    def update(self, *args):
        # Read frame from OpenCV
        ret, frame = self.capture.read()
        frame = frame[120:120 + 250, 200:200 + 250, :]

        # Flip horizontally and convert image to texture
        buf = cv2.flip(frame, 0).tostring()
        img_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        img_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.web_cam.texture = img_texture

    # Preprocess function to load image from file and convert to 100x100px
    def preprocess(self, file_path):
        # Read in image from file path
        byte_img = tf.io.read_file(file_path)
        # Load in the image
        img = tf.io.decode_jpeg(byte_img)

        # Preprocessing steps - resizing the image to be 100x100x3
        img = tf.image.resize(img, (100, 100))
        # Scale image to be between 0 and 1
        img = img / 255.0

        # Return image
        return img

    # Verification function to verify
    def verify(self, *args):
        # Specify threshold
        detection_threshold = 0.8
        verification_threshold = 0.8

        # Capture input image from cam
        SAVE_PATH = os.path.join('application_data', 'input_image', 'input_image.jpg')
        ret, frame = self.capture.read()
        frame = frame[120:120 + 250, 200:200 + 250, :]
        cv2.imwrite(SAVE_PATH, frame)

        # Build results array
        results = []

        for image in os.listdir(os.path.join('application_data', 'verification_images')):
            input_img = self.preprocess(os.path.join('application_data', 'input_image', 'input_image.jpg'))
            validation_img = self.preprocess(os.path.join('application_data', 'verification_images', image))

            # Make Predictions
            result = self.model.predict(list(np.expand_dims([input_img, validation_img], axis=1)))
            results.append(result)

        # Detection Threshold: Metric above which a prediction is considered positive
        detection = np.sum(np.array(results) > detection_threshold)

        # Verification Threshold: Proportion of positive predictions / total positive samples
        verification = detection / len(os.listdir(os.path.join('application_data', 'verification_images')))
        verified = verification > verification_threshold

        # Set verification text
        self.verification_label.text = 'Verified :)' if verified else 'Unverified :('
        

        # Change button color after verification
        self.button.background_color = (0.5, 0.8, 0.2, 1) if verified else (0.8, 0.2, 0.2, 1)

        return results, verified

if __name__ == '__main__':
    CamApp().run()
