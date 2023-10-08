import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(width, height, max_iter):
    x = np.linspace(-2, 2, width)
    y = np.linspace(-2, 2, height)
    c = np.array(np.meshgrid(x, y)).T.reshape(-1, 2)
    z = np.zeros(c.shape, dtype=complex)
    img = np.zeros(c.shape[0], dtype=int)

    for i in range(max_iter):
        z = z * z + c
        mask = np.abs(z) < 2
        img += mask

    img = img.reshape(width, height) 
    return img

width, height = 800, 800
max_iter = 256
mandelbrot_img = mandelbrot(width, height, max_iter)


plt.imshow(mandelbrot_img, extent=(-2, 2, -2, 2))
plt.show()
