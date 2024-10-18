import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir