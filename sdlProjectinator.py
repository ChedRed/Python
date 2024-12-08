# Basic stuff that should not be changed
from pathlib import Path as pl
import requests as rs
import os

import psm as pm

workdir = str(pl().absolute())
psm = pm.storage()

try:
    os.makedirs(workdir+"/SDLPdownloads")
except FileExistsError:
    os.rmdir(workdir+"/SDLPdownloads")
    os.makedirs(workdir+"/SDLPdownloads")
# Main code :>

psm.write_data("data:>","sdlProjectinator","test")