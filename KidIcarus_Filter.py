from PIL import Image
import numpy as np
import os
import multiprocessing

# Dir with your images
source = "REPLACE ME WITH A FILE PATH"
target_color = np.array([0, 255, 255])

def count_colors(image):
  # Open the image and convert it to RGB
  im = Image.open(image).convert('RGB')
  # Make a numpy array from the image
  na = np.array(im)
  # Get the unique colors and their counts
  colors, counts = np.unique(na.reshape(-1,3), axis=0, return_counts=True)
  # Calculate the percentages of each color
  percentages = counts / counts.sum() * 100
  # Check if the image has more than 6.25% of (0, 255, 255)
  for color, percentage in zip(colors, percentages):
    if np.all(color == target_color) and percentage > 6.20:
      # Delete the image
      os.remove(image)
      # Return a message
      print (f"\033[92m{image} not deleted\033[0m")
    else:
        print (f"\033[91m{image} deleted\033[0m")

        

# Create a list of filepaths
filepaths = [os.path.join(source, filename) for filename in os.listdir(source)]
# Create a pool of processes with the number of CPU cores available
pool = multiprocessing.Pool(multiprocessing.cpu_count())
# Apply the count_colors function to each filepath in parallel and get the results
results = pool.map(count_colors, filepaths)
# Close the pool and wait for the processes to finish
pool.close()
pool.join()
