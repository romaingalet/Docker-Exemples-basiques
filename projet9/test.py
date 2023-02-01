
print('Test imports')
import os

os.environ['PROJ_LIB'] = '/opt/conda/share/proj'

try:
  
  import sys
  import shutil
  import io
  
  import datetime 
  import argparse

  from pathlib import Path
  
except ImportError as impErr:
  print("Erreur d'import de {}".format(impErr.args[0]))


try:
  import geopandas
  import fiona
  import shapely
except ImportError as impErr:
#except Exception as e:
  print("Erreur d'import geo de {}".format(impErr.args[0]))
#  print("Erreur d'import geo")


try:

  import psycopg2
  import logging
  import traceback
  import multiprocessing
  import traceback
  
except ImportError as impErr:
  print("Erreur d'import (autre) de {}".format(impErr.args[0]))

