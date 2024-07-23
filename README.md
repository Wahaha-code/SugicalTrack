# SurgTrack: 3D Tracking of Real-world Surgical Instruments

<div align=center>
<img src="./docs/framework.png"> 
</div>

## Installation
  ```
  cd docker/
  docker pull gww106/sugicaltrack:tagname
  bash docker/run_container.sh
  bash build_all.sh
  docker exec -it sugicaltrack bash
```

## Checkpoints
- Download pretrained [weights of segmentation network](https://drive.google.com/file/d/1MEZvjbBdNAOF7pXcq6XPQduHeXB50VTc/view?usp=share_link), and put it under
`./checkpoints/saves/XMem-s012.pth`

- Download pretrained [weights of LoFTR outdoor_ds.ckpt](https://drive.google.com/drive/folders/1xu2Pq6mZT5hmFgiYMBT9Zt8h1yO-3SIp), and put it under
`./checkpoints/LoFTR/weights/outdoor_ds.ckpt`

# Inference
- Prepare your RGBD video folder as below.
```
root
  ├──rgb/    (PNG files)
  ├──depth/  (PNG files, stored in mm, uint16 format. Filename same as rgb)
  ├──masks/       (PNG files. Filename same as rgb. 0 is background. Else is foreground)
  └──cam_K.txt   (3x3 intrinsic matrix, use space and enter to delimit)
```
- Run your RGBD video. There are 3 steps.
```
# 1) Run joint tracking and reconstruction
python run_custom.py --mode run_video --video_dir /home/surgicaltrack --use_segmenter 1 --use_gui 1 --debug_level 2

# 2) Run global refinement post-processing to refine the mesh
python run_custom.py --mode global_refine --video_dir /home/surgicaltrack   # Change the path to your video_directory

# 3) (Optional) If you want to draw the oriented bounding box to visualize the pose, similar to our demo
python run_custom.py --mode draw_pose --out_folder /home/surgicaltrack
```




## Citation

If you use our code or paper in your work, please cite our paper.
