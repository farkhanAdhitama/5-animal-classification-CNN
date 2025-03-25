import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("my_model.h5")

# Class list
class_names = ["Elephant", "Horse", "Lion", "Cat", "Dog"]


# Fucntion for image processing
def preprocess_image(img):
    img = img.resize((224, 224))
    img = np.array(img) / 255.0  # image normalization
    img = np.expand_dims(img, axis=0)
    return img


# Function for prediction
def classify_img(image):
    image = preprocess_image(image)  # Preprocessing gambar
    prediction = model.predict(image)[0]  # Prediksi gambar
    probabilities = {
        class_names[i]: float(prediction[i]) for i in range(len(class_names))
    }
    return probabilities


# Buat UI dengan Gradio
interface = gr.Interface(
    fn=classify_img,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(),
    title="5 Animal Classifier",
    description="Upload an image of an animal (Elephant, Horse, Lion, Cat, Dog) and get the classification result.",
)

interface.launch()
