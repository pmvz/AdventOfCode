import numpy as np
from scipy.signal import convolve2d
from scipy.ndimage import zoom
from skimage.measure import label


# Load the input as characters, convert them to their
# ASCII value, and use scikit to label each region
garden = np.genfromtxt("2024/12/input", delimiter=1, dtype="<U1")
garden = np.vectorize(ord)(garden)
labels = label(garden, connectivity=1)


laplacian = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

cost = 0
for plant in np.unique(labels):
    # Convolution with this kernel adds four edges for each cell,
    # but subtracts one for each neighbouring cell with the same plant
    selected = labels == plant
    perimeter = convolve2d(selected, -laplacian, mode="same")
    cost += selected.sum() * perimeter[selected].sum()

print(cost)  # Part 1


# Define Sobel kernels (this looks more impressive than using scipy.ndimage.sobel)
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

cost = 0
for plant in np.unique(labels):
    # Double the array size because one-tile wide edges would not work otherwise
    selected = labels == plant
    zoomed = zoom(selected, 2, order=0)

    # Find the corners by finding regions with change in x and y
    verticaledges = convolve2d(zoomed, sobel_x, mode="same")
    horizontaledges = convolve2d(zoomed, sobel_y, mode="same")
    cornerness = abs(verticaledges * horizontaledges * zoomed)

    # 3 is an edge tile adjacent to a corner, so ignore those
    corners = ((cornerness != 3) & (cornerness != 0)).sum()
    cost += selected.sum() * corners  # #corners = #edges in any closed loop

print(cost)  # Part 2
