import os
import glob

# Check label files
label_files = glob.glob("E:/dataset/Baru Lagi.v3i.yolov8/train/labels/*.txt")

class_counts = {0: 0, 1: 0, 2: 0}  # Assistive, Non-Assistive, Normal

for label_file in label_files:
    with open(label_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) > 0:
                class_id = int(parts[0])
                class_counts[class_id] += 1

print("Class distribution:")
print(f"Assistive (class 0): {class_counts[0]} instances")
print(f"Non-Assistive (class 1): {class_counts[1]} instances")
print(f"Normal (class 2): {class_counts[2]} instances")