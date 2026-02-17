# src/detector.py

from pycoral.utils.edgetpu import make_interpreter
from pycoral.adapters import common


class ViolationDetector:

    def __init__(self, model_path):
        self.interpreter = make_interpreter(model_path)
        self.interpreter.allocate_tensors()

    def detect(self, image_path):
        """
        Replace with real inference logic.
        For demo returns random violation.
        """

        import random
        return random.choice([True, False])
