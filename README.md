# SurgTrack: 3D Tracking of Real-world Surgical Instruments

## Overview

<div align=center>
<img src="./docs/framework.png"> 
</div>

## Env setup(GPU 4090): docker
  ```
  cd docker/
  docker pull gww106/sugicaltrack:tagname
  bash docker/run_container.sh
  ```

If it's the first time you launch the container, you need to build extensions.
```
bash build_all.sh
```

Later you can execute into the container without re-build.
```
docker exec -it sugicaltrack bash
```

## Data download
- Download pretrained [weights of segmentation network](https://drive.google.com/file/d/1MEZvjbBdNAOF7pXcq6XPQduHeXB50VTc/view?usp=share_link), and put it under
`./BundleTrack/XMem/saves/XMem-s012.pth`

- Download pretrained [weights of LoFTR outdoor_ds.ckpt](https://drive.google.com/drive/folders/1xu2Pq6mZT5hmFgiYMBT9Zt8h1yO-3SIp), and put it under
`./BundleTrack/LoFTR/weights/outdoor_ds.ckpt`

- Download HO3D data. We provide the augmented data that you can download [here](https://drive.google.com/drive/folders/1Wk-HZDvUExyUrRn7us4WWEbHnnFHgOAX?usp=share_link). Then download YCB-Video object models from [here](https://drive.google.com/file/d/1-1m7qMMyUHYLhaRiQBbsSRMt5dMRX4jD/view?usp=share_link). Finally, make sure the structure is like below, and update your root path of `HO3D_ROOT` at the top of `BundleTrack/scripts/data_reader.py`
  ```
  HO3D_v3
    ├── evaluation
    ├── models
    └── masks_XMem
  ```


# Inference
- Prepare your RGBD video folder as below (also refer to the example milk data). You can find an [example milk data here](https://drive.google.com/file/d/1akutk_Vay5zJRMr3hVzZ7s69GT4gxuWN/view?usp=share_link) for testing.
```
root
  ├──rgb/    (PNG files)
  ├──depth/  (PNG files, stored in mm, uint16 format. Filename same as rgb)
  ├──masks/       (PNG files. Filename same as rgb. 0 is background. Else is foreground)
  └──cam_K.txt   (3x3 intrinsic matrix, use space and enter to delimit)
```

Due to license issues, we are not able to include [XMem](https://github.com/hkchengrex/XMem) in this codebase for running segmentation online. If you are interested in doing so, please download the code separately and add a wrapper in `segmentation_utils.py`.

- Run your RGBD video (specify the video_dir and your desired output path). There are 3 steps.
```
# 1) Run joint tracking and reconstruction
python run_custom.py --mode run_video --video_dir /home/surgicaltrack --use_segmenter 1 --use_gui 1 --debug_level 2

# 2) Run global refinement post-processing to refine the mesh
python run_custom.py --mode global_refine --video_dir /home/surgicaltrack   # Change the path to your video_directory

# 3) (Optional) If you want to draw the oriented bounding box to visualize the pose, similar to our demo
python run_custom.py --mode draw_pose --out_folder /home/surgicaltrack
```

- Finally the results will be dumped in the `out_folder`, including the tracked poses stored in `ob_in_cam/` and reconstructed mesh with texture `textured_mesh.obj`.



## Citation

If you use our code or paper in your work, please cite our paper.
