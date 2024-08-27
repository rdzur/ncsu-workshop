import os
import requests
import csv
import glob
import time
import argparse
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor
from itertools import repeat

# def download_file(url,out_fld):
#     command = f"wget -P {out_fld} -np -nd -r -nH -L {url}"
#     os.system(command)

def download_file(url, out_fld):
    try:
        # Extract the filename from the URL
        filename = os.path.basename(url)
        
        # Create the full path for the output file
        output_path = os.path.join(out_fld, filename)
        
        # Send a GET request to the URL
        response = requests.get(url, stream=True)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Write the content to a file
        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        
        print(f"Successfully downloaded: {filename}")
        return True
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i_f", "--in_file",required=True,help="Input file of all urls that ned to be downloaded")
    parser.add_argument("-o","--out_fld",required=True,help="Output folder.")

    config = parser.parse_args()

    start_time = time.time()
    os.makedirs(config.out_fld,exist_ok=True)

    with open(config.in_file,'r') as file:
        urls,reader = [],csv.reader(file)
        for line in reader: urls.append(line[0])
    
    pool = ProcessPoolExecutor(max_workers=mp.cpu_count())
    _ = list(
        pool.map(
            download_file,
            urls,
            repeat(config.out_fld)
        )
    )

    print(f"\n\n\n------ Done. {time.time() - start_time} seconds ------")