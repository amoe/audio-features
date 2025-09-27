import pdb
import librosa
import numpy as np
import tensorflow_hub as hub
import tensorflow as tf
import csv

# xxx unclear about where to load
yamnet_model = hub.load("https://tfhub.dev/google/yamnet/1")


def get_class_by_name(class_name: str):
    class_map_path = yamnet_model.class_map_path().numpy()
    
    # parse a simple csv, would do better with csv module
    

    with open(class_map_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['display_name'] == class_name:
                return int(row['index'])
            
    raise Exception('not found')

def detect_class(filename, class_name, threshold) -> list[tuple]:
    waveform, sr = librosa.load(filename, sr=16000, mono=True)
    waveform = waveform.astype(np.float32)

    scores, embeddings, spectrogram = yamnet_model(waveform)
    scores = scores.numpy()

    wanted_index = get_class_by_name(class_name)

    # xxx: no idea where this comes from
    frame_duration = 0.48

    # Keyed by class ID and value is a list of tuples which represent events.
    class_events = defaultdict(list)

    # scores is some kind of sliding window, and each frame_scores is indexed
    # by the class
    for i, frame_scores in enumerate(scores):
        for class_id, probability in frame_scores:
            if this_prob >= threshold:
                start_time = i * frame_duration
                end_time = (i + 1) * frame_duration
                class_events[class_id].append((start_time, end_time, float(this_prob)))


    return events
