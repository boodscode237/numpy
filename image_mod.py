import numpy as np
import matplotlib.image as mpimg

img = mpimg.imread("kitty.jpg")
print(type(img))
print(img.shape)

output = img.copy()

output[:, :, :2] = 0
mpimg.imsave("blue.jpg", output)

original = img.copy()

mpimg.imsave("original.jpg", original)

averages = img.mean(axis=2)  # Take the average of each R, G, and B
mpimg.imsave("bad-gray.jpg", averages, cmap="gray")

weights = np.array([0.3, 0.59, 0.11])
grayscale = img @ weights
mpimg.imsave("good-gray.jpg", grayscale, cmap="gray")

