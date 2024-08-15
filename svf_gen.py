import os
import rvt.default
import rvt.vis
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor

def svf_gen(file, in_fld, out_fld, default):
    ''' Generates SVF imagery using max number of cpus possible from the computer.'''
    # default = rvt.default.DefaultValues()
    default.save_sky_view_factor(f"{in_fld}/{file}",custom_dir=out_fld,save_float=False,save_8bit=True)