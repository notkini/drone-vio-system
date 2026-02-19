import cv2
import numpy as np
from pycoral.utils.edgetpu import make_interpreter
from pycoral.adapters.common import input_size, set_input
from pycoral.adapters.detect import get_objects

import config


class HelmetDetector:
    def __init__(self):
        self.interpreter = make_interpreter(config.MODEL_PATH)
        self.interpreter.allocate_tensors()

        self.width, self.height = input_size(self.interpreter)

    def detect(self, image):

        img = cv2.resize(image, (self.width, self.height))
        set_input(self.interpreter, img)

        self.interpreter.invoke()

        objs = get_objects(
            self.interpreter,
            score_threshold=config.CONF_THRESHOLD
        )

        detections = []
        violation = False

        for obj in objs:
            class_id = int(obj.id)
            score = obj.score
            bbox = obj.bbox

            detections.append({
                "class_id": class_id,
                "label": config.CLASS_NAMES.get(class_id, "unknown"),
                "score": score,
                "bbox": bbox
            })

            # ⭐ ONLY NO_HELMET triggers violation
            if class_id == config.VIOLATION_CLASS_ID:
                violation = True

        return detections, violation
