import os
import argparse
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor
from itertools import repeat
from PIL import Image
import time
import pdal

def pdal_colorization(file,in_fld,out_fld,dem_file,naip_file,crs):

    json = ''' 
{        
     "pipeline": [
            "%s",
            {
                "type": "filters.reprojection",
                "out_srs": "%s"
            },
            {
                "type":"filters.range",
                "limits":"Classification![7:7]"
            },
            {
                "type":"filters.range",
                "limits":"Classification![18:18]"
            },
            {
                "type":"filters.dem",
                "raster":"%s",
                "limits":"Z[50:300]"
            },
            {
                "type":"filters.colorization",
                "raster":"%s",
                "dimensions": ["Red:1:1.0", "Green:1:1.0", "Blue:1:1.0"]
            },
            {
                "type":"writers.las",
                "filename":"%s",
                "compression":"true",
                "minor_version":"4",
                "global_encoding":"17",
                "dataformat_id":"7"
            }
        ]
}'''% (f"{in_fld}/{file}",crs,dem_file,naip_file,f"{out_fld}/{file}")

    pipeline = pdal.Pipeline(json)
    pipeline.execute() 