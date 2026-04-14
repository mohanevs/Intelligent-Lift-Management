from ultralytics import YOLO
from pathlib import Path

MODEL_PATH = Path(r"C:\Users\ASUS\Desktop\CV_Projects\backend_v0.0.3\runs\segment\segmentation_model\weights\best.pt")
model = YOLO(MODEL_PATH)


def predict_multiple(image_paths):

    final_output = []

    for i, img_path in enumerate(image_paths):

        results = model.predict(
            source=img_path,
            conf=0.25,
            save=False   
        )

        floor_result = {
            "floor": i,
            "detections": []
        }

        for r in results:
            if r.boxes is not None:
                for cls, conf in zip(r.boxes.cls, r.boxes.conf):
                    floor_result["detections"].append({
                        "class_id": int(cls),
                        "class_name": model.names[int(cls)],
                        "confidence": float(conf)
                    })

        final_output.append(floor_result)

    return final_output


if __name__ == "__main__":

    image_paths = [
        r"C:\Users\ASUS\Desktop\CV_Projects\test_images\floor0.png",
        r"C:\Users\ASUS\Desktop\CV_Projects\test_images\floor1.png",
        r"C:\Users\ASUS\Desktop\CV_Projects\test_images\floor2.png",
        r"C:\Users\ASUS\Desktop\CV_Projects\test_images\floor0_1.png"
    ]

    output = predict_multiple(image_paths)
    print(output)