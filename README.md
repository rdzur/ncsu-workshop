# Technical Exchange Meeting (TEM)

**Exploring open-source object detection and visualization methods in an expanding big data era.**  
An interactive session designed as part of the North Carolina State University Geospatial Forum Studio series, September 6, 2024.

## Abstract

**TEM** material was developed to share applied concepts in:  

1. Object detection with [YOLOv8](https://github.com/ultralytics/ultralytics) (YOLO (You Only Look Once)).
2. Point cloud visualization with [Entwine](https://entwine.io/en/latest/).
3. Data analysis for derivative feature extraction with [GRASS GIS](https://grass.osgeo.org).

A set of Jupyter Notebooks have been developed to illustrate some production methods and techniques under development at [Bohannan Huston, Inc. (BHI)](https://www.bhinc.com).  These techniques are primarily for data quality assessment and assurance of large (multiple billion) airborne-collected point cloud datasets.  Point cloud visualization methods are applied in all BHI [Airborne LiDAR](https://potree.bhinc.com/data/view.html?r=%22https://entwine.bhinc.com/nnd12_lidar_rgb%22), [Mobile LiDAR](https://potree.bhinc.com/data/view.html?r=[%22https://entwine.bhinc.com/coh_mls%22,%22https://entwine.bhinc.com/coh_ppc%22,%22https://entwine.bhinc.com/coh_lidar_rgb%22]), [Terrestrial Laser Scanning](https://potree.bhinc.com/data/view.html?r=%22https://entwine.bhinc.com/Mesilla_Church_Scan%22), and [UAS LiDAR](https://potree.bhinc.com/data/view.html?r=%22https://entwine.bhinc.com/North_Domingo_Baca_Dam_rgb%22) point cloud projects.

## Data

Data for this TEM represent a small subset of larger [NOAA](https://chs.coast.noaa.gov/htdata/lidar1_z/) / [USGS](https://www.usgs.gov/3d-elevation-program) (see also:(https://usgs.entwine.io)) public-domain datasets initially used to investigate hardware performance benchmarking of object detection tasks (both data preparation and inference or prediction). Four North Carolina (NC) state-wide LiDAR datasets (2014/2015/2016/2017) were analyzed to evaluate model and hardware performance on a variety of internal computing platforms.  These data provided useful test case material with some key characteristics including:

1. Large Quality Level (QL) 2 LiDAR data volume at just over 30,000 square miles.
2. Detailed point cloud classification including buildings.
3. Sensor and processing variety including a Geiger-mode collected area (Phase 4 2016).

## Model

The object detection model in this TEM exercise was developed to predict remnant buildings in ground classified bare-earth LiDAR digital elevation models (DEM).  Traditional automated LiDAR classification routines for ground filtering may result in buildings of varying configurations being left in the terrain surface.  Despite visual inspection and review, these situations (buildings / structures) can be at times difficult to identify, reclassify and thus remove from the ground surface.  Training data for the model was developed from QL 2 LiDAR-based DEM data over southern New Mexico high-desert terrain represented as Sky View Factor (SVF) imagery through the the Relief Visualization Toolboox (RVT).  The YOLOv8 model was developed on a 4-GPU system using 676 annotated training images, another 84 images for testing and 76 images for model validation. 

## Environment

Specific Anaconda environment for object detection and point cloud colorization was created for tasks related to:

1. Data Download,
2. SVF Image Generation,
3. Splitting SVF Imagery, 
4. Predictions, 
5. Point Cloud Colorization, and
6. EPT Visualization

This environment is described in the following getting started material [GettingStarted.pdf](GettingStarted.pdf).

## Citations

[RVT Python library](https://github.com/EarthObservation/RVT_py/tree/master) by Žiga Kokalj, Žiga Maroh, Krištof Oštir, Klemen Zakšek and Nejc Čož, 2022.

Ultralytics by Jocher, G., Chaurasia, A., & Qiu, J. (2023). Ultralytics YOLO (Version 8.0.0) [Computer software]. https://github.com/ultralytics/ultralytics

PDAL https://doi.org/10.5281/zenodo.10884408

GRASS GIS https://doi.org/10.5281/zenodo.13102854



## Contacts

- Robert S. Dzur, Bohannan Huston, Inc.
- Federico Kurten, Bohannan Huston, Inc.
- Dennis R. Sandin, Bohannan Huston, Inc.
- Andres Lucero, Bohannan Huston, Inc.
