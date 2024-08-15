import os
import argparse
import re
from time import time
from collections import Counter
from PIL import Image
import numpy as np

def split_image(imgs_fld, rows, cols, output_dir=None):
    '''Function to split image into tiles given the number of rows and columns provided. (#tiles = rows * cols).
    imgs_fld: (string) folder where the images that will be tiled are stored.
    rows & cols: (int) number of rows and columns you want the images to be tiled.
    output_dir: (string) folder where you want the output tiled images stored. The default output tiled images will be stored in the current working
                directory if no folder is provided.'''
    
    ims = os.listdir(imgs_fld)
    images = [f"{imgs_fld}/{i}" for i in ims]
    for i in images:
        im = Image.open(i)
        im_width, im_height = im.size
        row_width = int(im_width / cols)
        row_height = int(im_height / rows)
        name, ext = os.path.splitext(i)
        name = os.path.basename(name)
        
        if output_dir != None:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
        else:
            output_dir = "./"
        n = 0
        for i in range(0, rows):
            for j in range(0, cols):
                box = (j * row_width, i * row_height, j * row_width +
                       row_width, i * row_height + row_height)
                outp = im.crop(box)
                outp_path = name + "_" + str(n) + ext
                outp_path = os.path.join(output_dir, outp_path)
                outp.save(outp_path)
                n += 1

def split_images_gr(file,in_fld,rows,cols,out_fld=None):
    '''Tile images maintaining their crs.
    - file: (str) input dem file.
    - out_fld: (str) output image folder.
    - rows & cols: (int) number of rows and columns you want the image to be split.
    '''

    im = Image.open(f'{in_fld}/{file}')
    im_width, im_height = im.size
    row_width, row_height, n = int(im_width / cols), int(im_height / rows), 0

    for i in range(0,rows):
        for j in range(0,cols):
            x1,y1,x2,y2 = j * row_width, i * row_height, row_width, row_height
            cli = f'gdal_translate -q -of GTIFF -srcwin {x1}, {y1}, {x2}, {y2} {in_fld}/{file} {out_fld}/{file.split(".")[0]}_{n}.tif'
            os.system(cli)
            n += 1


# def split_images_gr(in_fld,rows,cols,out_fld=None):
#     '''Split images that have a reference system to maintain their coordinates.
#     - in_fld: (str) input image folder.
#     - out_fld: (str) output image folder.
#     - rows & cols: (int) number of rows and columns you want the image to be split.
#     '''
#     files = sorted(os.listdir(in_fld))

#     if out_fld != None:
#             if not os.path.exists(out_fld):
#                 os.makedirs(out_fld)
#     else:
#         out_fld = "./"

#     for file in files:
#         im = Image.open(f'{in_fld}/{file}')
#         im_width, im_height = im.size
#         row_width, row_height, n = int(im_width / cols), int(im_height / rows), 0

#         for i in range(0,rows):
#             for j in range(0,cols):
#                 x1,y1,x2,y2 = j * row_width, i * row_height, row_width, row_height
#                 cli = f'gdal_translate -of GTIFF -srcwin {x1}, {y1}, {x2}, {y2} {in_fld}/{file} {out_fld}/{file.split(".")[0]}_{n}.tif'
#                 os.system(cli)
#                 n += 1

def join_split_img(imgs_fld, split_fld, rows, cols, join_fld=None):
    # Function to join more than one tiled image into whole images.
    # images_fld: (string) folder where the untiled images are stored.
    # split_fld: (string) folder where the tiles images are stored.
    # row & cols: (int) number of rows and columns that the images were tiled.
    # join_fld: (string) folder where the output joined images are stored.
    
    im, spls = os.listdir(imgs_fld), os.listdir(split_fld)
    images, splits, n = [f"{imgs_fld}/{i}" for i in im], [f"{split_fld}/{i}" for i in spls], 0
    for i in range(len(images)):
        img = images[i].split("/")[1].split(".")[0]
        files_merge = []
        for j in range(n,n+rows*cols):
            files_merge.append(splits[j])
    
        for index, path in enumerate(files_merge):
            path_number = int(path.split("_")[-1].split(".")[0])
            if path_number != index:
                print("Warning: Image " + path +
                      " has a number that does not match its index!")
                print("Please rename it first to match the rest of the images.")
        images_to_merge = [Image.open(p) for p in files_merge]
        image1 = images_to_merge[0]
        new_width = image1.size[0] * cols
        new_height = image1.size[1] * rows
        new_image = Image.new(image1.mode, (new_width, new_height))
    
        for i in range(0, rows):
            for j in range(0, cols):
                image = images_to_merge[i * cols + j]
                new_image.paste(image, (j * image.size[0], i * image.size[1]))
                
        if join_fld != None:
            if not os.path.exists(join_fld):
                os.makedirs(join_fld)
        else:
            join_fld = "./"
                
        new_image.save(f"{join_fld}/{img}.png")
        n += rows*cols

if __name__ == "__main__":
    main()