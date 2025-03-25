# Animal Classification Website with Gradio

This project is a web application for classifying images of animals using a pre-trained TensorFlow model. The application is built using Gradio for the user interface.

## Project Structure

- `app.py`: Main application file that sets up the Gradio interface and handles image classification.
- `my_model.h5`: Pre-trained TensorFlow model for animal classification.
- `requirements.txt`: List of dependencies required to run the project.
- `classification_example/`: Folder containing example images for classification.
- `notebook/`: Folder containing Jupyter notebooks for model training and experimentation.

## Requirements

You can install the required packages using the following command:

```sh
pip install -r requirements.txt
```

## How to Run

1. Clone this repository.
2. Install the required packages using the command above.
3. Run the application:

```sh
python app.py
```

4. Open your web browser and go to the URL provided by Gradio to use the application.

## Usage

Upload an image of an animal (Elephant, Horse, Lion, Cat, Dog) and get the classification result with probabilities for each class.

## Example Images

You can find example images for classification in the `classification_example/` folder.

## License

This project is licensed under the MIT License.
