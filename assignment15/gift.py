import os
import imageio
import numpy as np

images = []
img = os.listdir("image9")
for name in sorted(img):
    image = imageio.v2.imread('image9/' + name)
    image = np.resize(image, (720, 720, 3))
    images.append(image)
imageio.mimsave("output.gif",images)