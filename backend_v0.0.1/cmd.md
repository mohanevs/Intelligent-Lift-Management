---
yolo task=detect mode=train model=yolov8n.pt data="E:/dataset/Disabled person.v4i.yolov8/data.yaml" epochs=25 imgsz=512 batch=8 device=0
---

Terminal output :

(env) PS C:\Users\ASUS\Desktop\CV_Projects> yolo task=detect mode=train model=yolov8n.pt data="E:/dataset/Disabled person.v4i.yolov8/data.yaml" epochs=25 imgsz=512 batch=8 device=0
Downloading https://github.com/ultralytics/assets/releases/download/v8.4.0/yolov8n.pt to 'yolov8n.pt': 100% ━━━━━━━━━━━━ 6.2MB 209.6KB/s 30.5s
Ultralytics 8.4.32  Python-3.13.3 torch-2.11.0+cu128 CUDA:0 (NVIDIA GeForce RTX 2050, 4096MiB)
engine\trainer: agnostic_nms=False, amp=True, angle=1.0, augment=False, auto_augment=randaugment, batch=8, bgr=0.0, box=7.5, cache=False, cfg=None, classes=None, close_mosaic=10, cls=0.5, compile=False, conf=None, copy_paste=0.0, copy_paste_mode=flip, cos_lr=False, cutmix=0.0, data=E:/dataset/Disabled person.v4i.yolov8/data.yaml, degrees=0.0, deterministic=True, device=0, dfl=1.5, dnn=False, dropout=0.0, dynamic=False, embed=None, end2end=None, epochs=25, erasing=0.4, exist_ok=False, fliplr=0.5, flipud=0.0, format=torchscript, fraction=1.0, freeze=None, half=False, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, imgsz=512, int8=False, iou=0.7, keras=False, kobj=1.0, line_width=None, lr0=0.01, lrf=0.01, mask_ratio=4, max_det=300, mixup=0.0, mode=train, model=yolov8n.pt, momentum=0.937, mosaic=1.0, multi_scale=0.0, name=train, nbs=64, nms=False, opset=None, optimize=False, optimizer=auto, overlap_mask=True, patience=100, perspective=0.0, plots=True, pose=12.0, pretrained=True, profile=False, project=None, rect=False, resume=False, retina_masks=False, rle=1.0, save=True, save_conf=False, save_crop=False, save_dir=C:\Users\ASUS\Desktop\CV_Projects\runs\detect\train, save_frames=False, save_json=False, save_period=-1, save_txt=False, scale=0.5, seed=0, shear=0.0, show=False, show_boxes=True, show_conf=True, show_labels=True, simplify=True, single_cls=False, source=None, split=val, stream_buffer=False, task=detect, time=None, tracker=botsort.yaml, translate=0.1, val=True, verbose=True, vid_stride=1, visualize=False, warmup_bias_lr=0.1, warmup_epochs=3.0, warmup_momentum=0.8, weight_decay=0.0005, workers=8, workspace=None
Overriding model.yaml nc=80 with nc=2

                   from  n    params  module                                       arguments
  0                  -1  1       464  ultralytics.nn.modules.conv.Conv             [3, 16, 3, 2]
  1                  -1  1      4672  ultralytics.nn.modules.conv.Conv             [16, 32, 3, 2]
  2                  -1  1      7360  ultralytics.nn.modules.block.C2f             [32, 32, 1, True]
  3                  -1  1     18560  ultralytics.nn.modules.conv.Conv             [32, 64, 3, 2]
  4                  -1  2     49664  ultralytics.nn.modules.block.C2f             [64, 64, 2, True]
  5                  -1  1     73984  ultralytics.nn.modules.conv.Conv             [64, 128, 3, 2]
  6                  -1  2    197632  ultralytics.nn.modules.block.C2f             [128, 128, 2, True]
  7                  -1  1    295424  ultralytics.nn.modules.conv.Conv             [128, 256, 3, 2]
  8                  -1  1    460288  ultralytics.nn.modules.block.C2f             [256, 256, 1, True]
  9                  -1  1    164608  ultralytics.nn.modules.block.SPPF            [256, 256, 5]
 10                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']
 11             [-1, 6]  1         0  ultralytics.nn.modules.conv.Concat           [1]
 12                  -1  1    148224  ultralytics.nn.modules.block.C2f             [384, 128, 1]
 13                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']
 14             [-1, 4]  1         0  ultralytics.nn.modules.conv.Concat           [1]
 15                  -1  1     37248  ultralytics.nn.modules.block.C2f             [192, 64, 1]
 16                  -1  1     36992  ultralytics.nn.modules.conv.Conv             [64, 64, 3, 2]
 17            [-1, 12]  1         0  ultralytics.nn.modules.conv.Concat           [1]
 18                  -1  1    123648  ultralytics.nn.modules.block.C2f             [192, 128, 1]
 19                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]
 20             [-1, 9]  1         0  ultralytics.nn.modules.conv.Concat           [1]
 21                  -1  1    493056  ultralytics.nn.modules.block.C2f             [384, 256, 1]
 22        [15, 18, 21]  1    751702  ultralytics.nn.modules.head.Detect           [2, 16, None, [64, 128, 256]] 
Model summary: 130 layers, 3,011,238 parameters, 3,011,222 gradients, 8.2 GFLOPs

Transferred 319/355 items from pretrained weights
Freezing layer 'model.22.dfl.conv.weight'
AMP: running Automatic Mixed Precision (AMP) checks...
Downloading https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26n.pt to 'yolo26n.pt': 100% ━━━━━━━━━━━━ 5.3MB 299.3KB/s 18.1s
AMP: checks passed 
train: Fast image access  (ping: 0.10.1 ms, read: 174.9161.9 MB/s, size: 45.4 KB)
train: Scanning E:\dataset\Disabled person.v4i.yolov8\train\labels.cache... 9001 images, 0 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 9001/9001 2.5Git/s 0.0s    
WARNING Box and segment counts should be equal, but got len(segments) = 13, len(boxes) = 10133. To resolve this only boxes will be used and all segments will be removed. To avoid this please supply either a detect or segment dataset, not a detect-segment mixed dataset.
val: Fast image access  (ping: 0.10.1 ms, read: 114.956.6 MB/s, size: 44.0 KB)
val: Scanning E:\dataset\Disabled person.v4i.yolov8\valid\labels.cache... 1500 images, 0 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 1500/1500 133.9Mit/s 0.0s    
WARNING Box and segment counts should be equal, but got len(segments) = 2, len(boxes) = 1699. To resolve this only boxes will be used and all segments will be removed. To avoid this please supply either a detect or segment dataset, not a detect-segment mixed dataset.
optimizer: 'optimizer=auto' found, ignoring 'lr0=0.01' and 'momentum=0.937' and determining best 'optimizer', 'lr0' and 'momentum' automatically... 
optimizer: AdamW(lr=0.001667, momentum=0.9) with parameter groups 57 weight(decay=0.0), 64 weight(decay=0.0005), 63 bias(decay=0.0)
Plotting labels to C:\Users\ASUS\Desktop\CV_Projects\runs\detect\train\labels.jpg... 
Image sizes 512 train, 512 val
Using 8 dataloader workers
Logging results to C:\Users\ASUS\Desktop\CV_Projects\runs\detect\train
Starting training for 25 epochs...

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       1/25     0.721G      1.222      1.679      1.368          5        512: 100% ━━━━━━━━━━━━ 1126/1126 9.1it/s 2:04
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.0it/s 9.4s
                   all       1500       1699      0.823      0.739       0.82      0.482

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       2/25     0.822G      1.248      1.352      1.374          1        512: 100% ━━━━━━━━━━━━ 1126/1126 10.1it/s 1:52
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.2it/s 9.2s
                   all       1500       1699      0.816      0.754      0.842      0.562

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       3/25     0.822G      1.257      1.288      1.378          0        512: 100% ━━━━━━━━━━━━ 1126/1126 10.3it/s 1:49
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.1it/s 9.3s
                   all       1500       1699      0.828      0.776      0.834      0.545

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       4/25     0.822G      1.212      1.197      1.345          1        512: 100% ━━━━━━━━━━━━ 1126/1126 10.4it/s 1:49
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.3it/s 9.1s
                   all       1500       1699      0.835      0.779      0.849      0.564

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       5/25     0.824G      1.156       1.11      1.304          1        512: 100% ━━━━━━━━━━━━ 1126/1126 10.4it/s 1:48
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.2it/s 9.2s
                   all       1500       1699      0.873      0.808      0.891      0.609

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       6/25     0.824G      1.122      1.044      1.282          1        512: 100% ━━━━━━━━━━━━ 1126/1126 10.4it/s 1:48
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.2it/s 9.3s
                   all       1500       1699      0.897      0.855      0.914       0.64

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       7/25     0.824G      1.098      1.019      1.274          2        512: 100% ━━━━━━━━━━━━ 1126/1126 10.4it/s 1:48
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.3it/s 9.1s
                   all       1500       1699      0.904      0.852      0.915      0.651

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       8/25     0.824G      1.072     0.9782      1.258          2        512: 100% ━━━━━━━━━━━━ 1126/1126 10.5it/s 1:48
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.4it/s 9.0s
                   all       1500       1699      0.893      0.872      0.915       0.65

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       9/25     0.824G      1.046     0.9546       1.24          7        512: 100% ━━━━━━━━━━━━ 1126/1126 10.5it/s 1:47
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.4it/s 9.1s
                   all       1500       1699      0.908      0.891      0.928      0.675

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      10/25     0.824G      1.033     0.9097       1.23          4        512: 100% ━━━━━━━━━━━━ 1126/1126 10.5it/s 1:47
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.4it/s 9.0s
                   all       1500       1699      0.912      0.887      0.928      0.681

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      11/25     0.824G      1.006     0.8761      1.212          3        512: 100% ━━━━━━━━━━━━ 1126/1126 10.5it/s 1:47
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.5it/s 8.9s
                   all       1500       1699      0.922       0.88       0.93      0.681

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      12/25     0.824G     0.9948     0.8785      1.211          5        512: 100% ━━━━━━━━━━━━ 1126/1126 10.4it/s 1:48
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.5it/s 8.9s
                   all       1500       1699      0.911       0.88      0.933      0.692

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      13/25     0.824G      0.978     0.8459      1.198          4        512: 100% ━━━━━━━━━━━━ 1126/1126 10.5it/s 1:47
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.5it/s 9.0s
                   all       1500       1699      0.915        0.9      0.933      0.692

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      14/25     0.824G     0.9632     0.8308      1.193          2        512: 100% ━━━━━━━━━━━━ 1126/1126 10.3it/s 1:49
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.4it/s 9.1s
                   all       1500       1699      0.913       0.89      0.935      0.698

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      15/25     0.824G     0.9457     0.8042      1.179          3        512: 100% ━━━━━━━━━━━━ 1126/1126 10.5it/s 1:48
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.4it/s 9.0s
                   all       1500       1699      0.926      0.897      0.938      0.708
Closing dataloader mosaic

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      16/25     0.824G     0.8581     0.6609      1.153          1        512: 100% ━━━━━━━━━━━━ 1126/1126 10.5it/s 1:47
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.4it/s 9.1s
                   all       1500       1699      0.915      0.896       0.94      0.718

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      17/25     0.824G      0.843     0.6336      1.143          1        512: 100% ━━━━━━━━━━━━ 1126/1126 10.5it/s 1:47
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.5it/s 8.9s
                   all       1500       1699      0.919      0.906      0.946      0.721

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      18/25     0.824G     0.8247      0.615      1.136          1        512: 100% ━━━━━━━━━━━━ 1126/1126 10.5it/s 1:47
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.6it/s 8.9s
                   all       1500       1699      0.924      0.906      0.946       0.73

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      19/25     0.824G     0.8002     0.5976      1.124          1        512: 100% ━━━━━━━━━━━━ 1126/1126 10.6it/s 1:47
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.3it/s 9.1s
                   all       1500       1699      0.927       0.91      0.944      0.735

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      20/25     0.824G     0.7827     0.5744      1.108          1        512: 100% ━━━━━━━━━━━━ 1126/1126 10.5it/s 1:47
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.5it/s 8.9s
                   all       1500       1699      0.922      0.915      0.947      0.736

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      21/25     0.824G     0.7644     0.5546      1.099          1        512: 100% ━━━━━━━━━━━━ 1126/1126 10.5it/s 1:47
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.5it/s 9.0s
                   all       1500       1699      0.932      0.916      0.951      0.743

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      22/25     0.824G     0.7552     0.5465      1.085          1        512: 100% ━━━━━━━━━━━━ 1126/1126 10.5it/s 1:47
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.5it/s 9.0s
                   all       1500       1699      0.934      0.918      0.948      0.743

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      23/25     0.824G     0.7268     0.5271      1.074          1        512: 100% ━━━━━━━━━━━━ 1126/1126 10.5it/s 1:47
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.4it/s 9.0s
                   all       1500       1699      0.935      0.918      0.951      0.745

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      24/25     0.824G     0.7138     0.5199      1.066          1        512: 100% ━━━━━━━━━━━━ 1126/1126 10.5it/s 1:47
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.6it/s 8.9s
                   all       1500       1699      0.927      0.919       0.95      0.747

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      25/25     0.824G     0.6963     0.5036      1.059          2        512: 100% ━━━━━━━━━━━━ 1126/1126 10.5it/s 1:47
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 10.5it/s 9.0s
                   all       1500       1699      0.942      0.912       0.95      0.749

25 epochs completed in 0.822 hours.
Optimizer stripped from C:\Users\ASUS\Desktop\CV_Projects\runs\detect\train\weights\last.pt, 6.2MB
Optimizer stripped from C:\Users\ASUS\Desktop\CV_Projects\runs\detect\train\weights\best.pt, 6.2MB

Validating C:\Users\ASUS\Desktop\CV_Projects\runs\detect\train\weights\best.pt...
Ultralytics 8.4.32  Python-3.13.3 torch-2.11.0+cu128 CUDA:0 (NVIDIA GeForce RTX 2050, 4096MiB)
Model summary (fused): 73 layers, 3,006,038 parameters, 0 gradients, 8.1 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 94/94 9.7it/s 9.7s
                   all       1500       1699      0.941      0.912       0.95      0.749
              Crutches        717        773      0.919      0.878      0.921      0.783
            Wheelchair        783        926      0.964      0.946      0.979      0.715
Speed: 0.2ms preprocess, 2.6ms inference, 0.0ms loss, 1.0ms postprocess per image
Results saved to C:\Users\ASUS\Desktop\CV_Projects\runs\detect\train
 Learn more at https://docs.ultralytics.com/modes/train
VS Code: view Ultralytics VS Code Extension  at https://docs.ultralytics.com/integrations/vscode






---
yolo task=detect mode=predict model="runs/detect/train/weights/best.pt" source="images.jpg"
---