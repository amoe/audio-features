import pdb
import os
import sys
import engine
import warnings
import json
import openpyxl
import audioread.exceptions

# probably bad but works
warnings.filterwarnings('ignore')


def seconds_to_mmss(seconds: float) -> str:
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m:02d}:{s:02d}"

#class_name = sys.argv[1]
base_dir = sys.argv[1]

#print("I will look for:", class_name)

def print_probabilities(events: dict[int, list[tuple]]) -> None:
    for start, end, prob in events:
        print(f"Event {seconds_to_mmss(start)}–{seconds_to_mmss(end)} (p={prob:.2f})")        

out_wb = openpyxl.Workbook(write_only=True)
out_ws = out_wb.create_sheet()
out_ws.append(engine.create_header_row())
        
for root, dirs, files in os.walk(base_dir):
    relative_root = os.path.relpath(root, base_dir)
    for file_ in sorted(files):
        absolute_path = os.path.join(root, file_)
        print("Analysing:", absolute_path, flush=True)
        try:
            probabilities = engine.detect_classes(absolute_path, threshold=0.5)

            row = [absolute_path]
            class_indices = engine.get_classes()
            for k in class_indices:
                v = probabilities.get(int(k))
                if v:
                    row.append(len(v))
                else:
                    row.append(0)

            out_ws.append(row)

            with open('out.json', 'w') as f:
                json.dump(probabilities, f)
        except audioread.exceptions.NoBackendError as e:
            # print("skipping:", absolute_path)
            # pass
            raise e

        
#        print_probabilities(probabilities)
out_wb.save('out.xlsx')
