import sys
import json
import engine

# drill down to a specific class

with open('out.json', 'r') as f:
    data = json.load(f)

    #xx cast to str

def seconds_to_mmss(seconds: float) -> str:
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m:02d}:{s:02d}"

def print_probabilities(events: dict[int, list[tuple]]) -> None:
    for start, end, prob in events:
        print(f"Event {seconds_to_mmss(start)}–{seconds_to_mmss(end)} (p={prob:.2f})")        

class_name = sys.argv[1]
        
key = str(engine.get_class_by_name(class_name))
x = data.get(key)
if x is None:
    print("Class not found.")
else:
    print_probabilities(x['probabilities'])
    
