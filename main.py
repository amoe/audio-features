import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import librosa


def seconds_to_mmss(seconds: float) -> str:
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m:02d}:{s:02d}"


# Load YAMNet
yamnet_model = hub.load("https://tfhub.dev/google/yamnet/1")

# Get class names once
class_map_path = yamnet_model.class_map_path().numpy()
class_names = [c for c in tf.io.gfile.GFile(class_map_path).read().splitlines()]

def detect_coughs(file_path, threshold=0.5):
    # Load audio at 16 kHz mono
    waveform, sr = librosa.load(file_path, sr=16000, mono=True)
    waveform = waveform.astype(np.float32)

    # Run through YAMNet: one prediction per ~0.48s patch
    scores, embeddings, spectrogram = yamnet_model(waveform)
    scores = scores.numpy()

    val = '42,/m/01b_21,Cough'
    cough_idx = class_names.index(val)

    cough_events = []
    frame_duration = 0.48  # seconds per YAMNet frame

    for i, frame_scores in enumerate(scores):
        prob = frame_scores[cough_idx]
        if prob >= threshold:
            start_time = i * frame_duration
            end_time = (i + 1) * frame_duration
            cough_events.append((start_time, end_time, float(prob)))

    return cough_events

# Example usage
if __name__ == "__main__":
    coughs = detect_coughs("example.wav", threshold=0.5)
    for start, end, prob in coughs:
        print(f"Cough {seconds_to_mmss(start)}–{seconds_to_mmss(end)} (p={prob:.2f})")        
#        print(f"Cough from {start:.2f}s to {end:.2f}s (p={prob:.2f})")
