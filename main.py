import rasterio
import numpy
import matplotlib.pyplot as plt

image_file = "analyticPicture.tif"

# we open the picture using rasterio
# and get only the red band
with rasterio.open(image_file) as src:
    band_red = src.read(1) # we get only the red band

# we open the picture using rasterio
# and get only the near-infrared band
with rasterio.open(image_file) as src:
    band_nir = src.read(4)

# we allow division by zero
numpy.seterr(divide='ignore', invalid='ignore')

# we calculate the NDVI using the formula NDVI = (NIR-RED)/(NIR+RED)
ndvi = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red)

# setting spatial characteristics of the output object to mirror the input
kwargs = src.meta
kwargs.update(
    dtype=rasterio.float32,
    count = 1)

# creating the file
with rasterio.open('ndvi.tif', 'w', **kwargs) as dst:
        dst.write_band(1, ndvi.astype(rasterio.float32))

# saving the file
plt.imsave("ndvi_cmap.png", ndvi, cmap=plt.cm.viridis)
