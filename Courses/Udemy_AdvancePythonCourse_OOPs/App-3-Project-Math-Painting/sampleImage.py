import numpy as np 
from PIL import Image 

data = np.zeros((100, 500, 3), dtype=np.uint8) 
print(data[0][0][0])

data[30][50] = [255, 255, 0]
data[50:60, 100:500] = [255, 0, 0]


img = Image.fromarray(data, 'RGB')
img.save("img.png")