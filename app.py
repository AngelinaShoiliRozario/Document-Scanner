# import sys
# from docscan.doc import scan

# sys.stdout.buffer.write(scan(sys.stdin.buffer.read()))


import sys
from docscan.doc import scan
import numpy as np
import os
import cv2

if __name__ == "__main__":
    # Read input image data from a file or any other source
    # For simplicity, I'm assuming that you'll provide the image data as a binary file
    path= os.path.join('document.jpg')
    

    # image = cv2.imread(path)
    with open(path, 'rb') as f:
        image_data = f.read()

    # Call the scan function with the image data
    output_image_data = scan(image_data)
   
    # Call the scan function with the input image data
    # output_image_data = scan(image)

    # # Write the output image data to stdout or any other destination
    # sys.stdout.buffer.write(output_image_data)
    output_path = "output_document.jpg"

    # Write the output image data to a file
    with open(output_path, 'wb') as f:
        f.write(output_image_data)

    print(f"Processed image saved to {output_path}")
