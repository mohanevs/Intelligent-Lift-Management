from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List
import shutil
import os
import uuid
import uvicorn;

# Your model imports
import sys
sys.path.append(r"C:\Users\ASUS\Desktop\CV_Projects\model")
from algo import predict_multiple, build_output  

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Intelligent Lift API is running", "status": "healthy"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(files: List[UploadFile] = File(...)):
    print(f"📥 Received {len(files)} files")
    
    temp_paths = []

    # save uploaded files temporarily
    for idx, file in enumerate(files):
        temp_name = f"temp_{uuid.uuid4()}.jpg"
        print(f"   Saving file {idx}: {file.filename} -> {temp_name}")

        with open(temp_name, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        temp_paths.append(temp_name)

    # Run YOLO prediction
    print("🔍 Running YOLO prediction...")
    detections = predict_multiple(temp_paths)
    print(f"   Detections: {detections}")
    
    # Build output
    result = build_output(detections, capacity=5)
    print(f"✅ Result: {result}")

    # cleanup
    for path in temp_paths:
        os.remove(path)

    return JSONResponse(content=result)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)