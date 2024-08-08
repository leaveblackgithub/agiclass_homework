from __init__ import *
import sys
import os

AGI_BASE=os.getenv("AGI_BASE")
sys.path.insert(0,os.path.join(AGI_BASE,"00_shared")) 
# from backend import *
from environment_import import *