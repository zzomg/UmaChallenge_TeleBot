import torch
import numpy as np
from fastai import *
from fastai.vision import *
from config import storage_path, learner_path

learn = load_learner(learner_path)
model_classes_indices = learn.data.c2i

def get_top_preds(outputs):
    out_indices = np.array(outputs.indices.tolist())
    out_values = np.array(outputs.values.tolist())

    top_indices = out_indices[0:5]
    top_values = out_values[0:5]

    top_preds = {}
    for idx, val in zip(top_indices, top_values):
        for class_n, class_index in model_classes_indices.items():
            if idx == class_index:
                top_preds[class_n] = val * 100

    return top_preds

def process_image(image_name):
    img = open_image("{0}/{1}".format(storage_path, image_name))
    pred_class, pred_idx, outputs = learn.predict(img)

    sorted_outputs = torch.sort(outputs, descending=True)

    top_preds = get_top_preds(sorted_outputs)
    
    out = "The picture belongs to:\n"
    for class_n, val in top_preds.items():
        out += f"Class {class_n}, probability: {val:.4f}%\n"

    return out
