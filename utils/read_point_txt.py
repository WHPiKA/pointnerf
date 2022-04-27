import numpy as np
from tqdm import tqdm

p = '/media/share_data/zhupengfei/pointnerf/my_checkpoints/col_nerfsynth/carla03_20220425/points/'
filename = 'step-init-0.txt'


with open(p + filename, 'r') as file:
    points = np.loadtxt(file, delimiter=";")

header = [
        'ply',
        'format ascii 1.0',
        'element vertex',
        'property float32 x',
        'property float32 y',
        'property float32 z',
        'end_header'
    ]



writer = open(p + filename + '.ply', 'w+')
header[2] += ' ' + str(points.shape[0])
for line in header:
    writer.write(line + '\n')
for line in tqdm(points):
    writer.write(' '.join([str(i) for i in line[:3]]) + '\n')
writer.close()
