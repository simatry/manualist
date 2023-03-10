""" Evaluate model performance on a given data loader."""
import torch
import torch.nn as nn

from data.encoding.label_encoder import vec_to_word


@torch.no_grad()
def evaluate_performance(device, data_loader: torch.utils.data.DataLoader, model: nn.Module):
    """ Evaluate model performance for on a given dataloader.
    Currently only calculates accuracy score, but more options need to be added.
    """
    count = 0
    count_correct = 0
    for features, label in data_loader:
        features = features.to(device=device)
        label = label.to(device=device)
        pred = model.predict(features)

        predicted_label = vec_to_word(pred)
        actual_label = vec_to_word(label)

        count += 1
        if predicted_label == actual_label:
            count_correct += 1

    return count_correct / count
