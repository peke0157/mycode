import numpy as np
import librosa
import librosa.display
from pathlib import Path
from sklearn import datasets

data_dir = Path('testdata')
npy_files = list(data_dir.glob('**/*.npy'))

X = []
Y = []

for npy_files in npy_files:
    mfccs = np.load(npy_files)