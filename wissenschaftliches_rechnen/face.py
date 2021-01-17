import numpy as np
import matplotlib.pyplot as plt

# from utils import read_random_face, face_path
from python_utils import *

# lese ein Zufallsbild aus DB ein.
random_face = read_random_face(face_path)

print(random_face.shape)