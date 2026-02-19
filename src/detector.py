import cv2
import numpy as np
from pycoral.utils.edgetpu import make_interpreter
from pycoral.adapters.common import input_size, set_input, output_tensor
import config


class Detector:

    def __init__(self, model_path):

        print("Loading Edge TPU model...")

        self.interpreter = make_interpreter(model_path)
        self.interpreter.allocate_tensors()

        self.width, self.height = input_size(self.interpreter)

    def detect(self, image_path):

        img = cv2.imread(image_path)
        if img is None:
            print("Failed to load image:", image_path)
            return False

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_resized = cv2.resize(img_rgb, (self.width, self.height))

        set_input(self.interpreter, img_resized)
        self.interpreter.invoke()

        output = output_tensor(self.interpreter, 0)

        if output is None:
            return False

        violation_found = False

        if isinstance(output, np.ndarray):

            for det in output:

                if len(det) < 2:
                    continue

                class_id = int(det[0])
                confidence = float(det[1])

                # Print detected class (for debugging)
                if class_id in config.CLASS_NAMES:
                    print(
                        f"Detected: {config.CLASS_NAMES[class_id]} "
                        f"(conf: {confidence:.2f})"
                    )

                # 🚨 ONLY no_helmet is violation
                if (
                    class_id == config.NO_HELMET_CLASS_ID
                    and confidence > config.CONF_THRESHOLD
                ):
                    violation_found = True

        return violation_found
