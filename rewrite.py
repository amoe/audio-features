import os
import sys
from engine import detect_class
import warnings

# probably bad but works
warnings.filterwarnings('ignore')


def seconds_to_mmss(seconds: float) -> str:
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m:02d}:{s:02d}"

class_name = sys.argv[1]
base_dir = sys.argv[2]

print("I will look for:", class_name)

def print_probabilities(events: list[tuple]) -> None:
    for start, end, prob in events:
        print(f"Event {seconds_to_mmss(start)}–{seconds_to_mmss(end)} (p={prob:.2f})")        

for root, dirs, files in os.walk(base_dir):
    relative_root = os.path.relpath(root, base_dir)
    for file_ in files:
        absolute_path = os.path.join(root, file_)
        print("Analysing:", absolute_path, flush=True)
        probabilities = detect_class(absolute_path, class_name, threshold=0.3)
        print_probabilities(probabilities)
