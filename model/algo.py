from ultralytics import YOLO
from pathlib import Path

# LOAD MODEL
MODEL_PATH = Path(r"C:\Users\ASUS\Desktop\CV_Projects\backend_v0.0.3\runs\segment\segmentation_model\weights\best.pt")
model = YOLO(MODEL_PATH)

# CONFIG

PRIORITY = {
    "Assistive": 10,
    "Elderly": 7,
    "Normal": 3
}

FLOOR_NAMES = {
    0: "Ground Floor",
    1: "1st Floor",
    2: "2nd Floor"
}

EMOJI = {
    "Assistive": "♿",
    "Elderly": "👴",
    "Normal": "👤"
}

# YOLO PREDICTION
def predict_multiple(image_paths):
    results = model.predict(source=image_paths, conf=0.25, save=False)

    final_output = []

    for i, r in enumerate(results):
        floor_result = {
            "floor": i,
            "detections": []
        }

        if r.boxes is not None:
            for cls, conf in zip(r.boxes.cls, r.boxes.conf):
                class_name = model.names[int(cls)]
                floor_result["detections"].append({
                    "class_id": int(cls),
                    "class_name": class_name,
                    "confidence": float(conf)
                })

        final_output.append(floor_result)

    return final_output

# ASSIGN SCORES
def assign_scores(detections):
    scores = {}
    details = {}

    for floor_data in detections:
        floor = floor_data["floor"]
        dets = floor_data["detections"]

        if len(dets) == 0:
            class_name = "None"
            score = 0
        else:
            class_name = dets[0]["class_name"]  # single person assumption
            score = PRIORITY.get(class_name, 3)

        scores[floor] = score
        details[floor] = {
            "class": class_name,
            "score": score,
            "emoji": EMOJI.get(class_name, "👤")
        }

    return scores, details


# GREEDY ALGORITHM (CAPACITY-AWARE)
def greedy_lift_order(scores, capacity=1):
    # Assume 1 person per floor (extendable later)
    people_per_floor = {floor: 1 for floor in scores}

    # Sort by score DESC, then by floor ASC (tie-breaker)
    sorted_floors = sorted(scores.keys(), key=lambda x: (-scores[x], x))

    selected_order = []
    current_load = 0

    for floor in sorted_floors:
        people = people_per_floor[floor]

        if current_load + people <= capacity:
            selected_order.append(floor)
            current_load += people

    return selected_order

# FINAL OUTPUT
def build_output(detections, capacity=1):
    scores, details = assign_scores(detections)
    order = greedy_lift_order(scores, capacity)

    # Priority Queue (sorted view)
    priority_queue = sorted(
        [
            {
                "floor": f,
                "floorName": FLOOR_NAMES[f],
                "score": scores[f],
                "description": f"1 {details[f]['class']}"
            }
            for f in scores
        ],
        key=lambda x: x["score"],
        reverse=True
    )

    # YOLO Output (for frontend)
    yolo_output = []
    for f in scores:
        yolo_output.append({
            "floor": f,
            "floorName": FLOOR_NAMES[f],
            "persons": [
                {
                    "type": details[f]["class"].lower(),
                    "class_name": details[f]["class"],
                    "priority": details[f]["score"],
                    "emoji": details[f]["emoji"]
                }
            ],
            "totalScore": scores[f]
        })

    # Final Decision
    final_decision = []
    for i, f in enumerate(order):
        final_decision.append({
            "position": i + 1,
            "floor": f,
            "floorName": FLOOR_NAMES[f],
            "score": scores[f]
        })

    return {
        "priority_queue": priority_queue,
        "yolo_output": yolo_output,
        "final_decision": final_decision,
        "order": order,
        "scores": scores
    }


# MAIN RUN
if __name__ == "__main__":
    image_paths = [
        r"C:\Users\ASUS\Desktop\CV_Projects\test_images\floor1.png",
        r"C:\Users\ASUS\Desktop\CV_Projects\test_images\floor0.png",
        r"C:\Users\ASUS\Desktop\CV_Projects\test_images\floor2.png"
    ]

    detections = predict_multiple(image_paths)
    result = build_output(detections, capacity=5)
    
    print(result)
    
    # For Cleaner Print :-

    # # PRINT RESULTS
    # print("\n" + "="*60)
    # print("PRIORITY QUEUE")
    # print("="*60)
    # for item in result['priority_queue']:
    #     print(f"\n{item['floorName']}")
    #     print(f"  Score: {item['score']}")
    #     print(f"  {item['description']}")

    # print("\n" + "="*60)
    # print("YOLO OUTPUT")
    # print("="*60)
    # for floor in result['yolo_output']:
    #     print(f"\n{floor['floorName']}")
    #     for p in floor['persons']:
    #         print(f"  {p['emoji']} {p['type']}: {p['priority']}pts")

    # print("\n" + "="*60)
    # print("FINAL DECISION")
    # print("="*60)
    # for d in result['final_decision']:
    #     print(f"{d['position']}. {d['floorName']} (Score: {d['score']})")