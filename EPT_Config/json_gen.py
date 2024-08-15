import os
import glob
import argparse
import json
import numpy as np
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor
from itertools import repeat
import time

def json_creation(num,in_fld,out_fld,out_json):
    dictio = {"input":os.path.abspath(in_fld),"output":os.path.abspath(out_fld),"subset":{"id":int(num),"of":64}}
    with open(f"{out_json}/config{num}.json","w") as file: 
        json.dump(dictio,file,indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i_f","--in_fld",required=True,help="The location of the colorized las/laz files.")
    parser.add_argument("-o_j","--out_json",required=True,help="Location where the json files are going to be output.")
    parser.add_argument("-o_f","--out_fld",required=True,help="EPT file location output folder.")

    config = parser.parse_args()

    start_time = time.time()

    os.makedirs(config.out_fld,exist_ok=True)
    vals = np.arange(1,65)

    # print(os.path.abspath(config.in_fld))

    pool = ProcessPoolExecutor(max_workers=mp.cpu_count())
    _ = list(
        pool.map(
            json_creation,
            vals,
            repeat(config.in_fld),
            repeat(config.out_fld),
            repeat(config.out_json)
        )
    )
