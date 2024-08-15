import os
import glob
import argparse
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor
from itertools import repeat
import time

def ept_config(command):
    # print(command)
    os.system(command)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--in_file",required=True,help="The input configuration file")
    
    config = parser.parse_args()

    start_time = time.time()

    with open(config.in_file) as f:
        lines = [i.rstrip() for i in f.readlines()] 

    # if not os.path.exists(config.out_fld):
    #     os.makedirs(config.out_fld)
        

    pool = ProcessPoolExecutor(max_workers=mp.cpu_count())
    _ = list(
        pool.map(
            ept_config,
            lines
        )
    )
    print(f"\n--- {time.time() - start_time} seconds ---")