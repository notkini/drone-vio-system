# src/detector.py

from pycoral.utils.edgetpu import make_interpreter
from pycoral.adapters import common
from PIL import Image
import config

class Detector:

    def __init__(self, model_path):

        print("Loading Edge TPU model...")
        self.interpreter = make_interpreter(model_path)
        self.interpreter.allocate_tensors()

    def detect(self, image_path):

        image = Image.open(image_path).convert("RGB")
        common.set_resized_input(
            self.interpreter,
            image.size,
            lambda size: image.resize(size, Image.LANCZOS)
        )

        self.interpreter.invoke()

        output = self.interpreter.get_tensor(
            self.interpreter.get_output_details()[0]['index']
        )

        # Simple check for demo
        if output.max() > config.CONF_THRESHOLD:
            return True

        return False
