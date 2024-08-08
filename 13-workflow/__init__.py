import sys
import os

AGI_BASE=os.getenv("AGI_BASE")
sys.path.insert(0,os.path.join(AGI_BASE,"00_shared")) 
sys.path.insert(0,os.path.join(AGI_BASE,"10-auto-gpt-work")) 
# from backend import *
from environment_import import *