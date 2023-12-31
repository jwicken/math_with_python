import matplotlib.pyplot as plt 
import matplotlib.cm as cm
import random

def initialize_image(x_p, y_p): 
    image = []
    for i in range(y_p):
        x_colors = []
        for j in range(x_p): 
            x_colors.append(0)
        image.append(x_colors)
    return image 

def color_points(): 
    x_p = 400
    y_p = 400
    max_iteration = 1000
    image = initialize_image(x_p, y_p)

    x_min, x_max = -2.5, 1
    y_min, y_max = -1, 1

    for y in range(y_p): 
        for x in range(x_p):
            real = x_min + (x / x_p) * (x_max - x_min)
            imag = y_min + (y / y_p) * (y_max - y_min)
            c = complex(real, imag)
            z = 0 + 0j
            iteration = 0

            while abs(z) <= 2 and iteration < max_iteration:
                z = z*z + c
                iteration += 1

            # Normalize the color
            color = iteration / max_iteration
            image[y][x] = color

    # Plotting
    plt.imshow(image, origin='lower', extent=(x_min, x_max, y_min, y_max), cmap=cm.viridis, interpolation='nearest')
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    color_points()
