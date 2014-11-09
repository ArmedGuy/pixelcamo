# pixelcamo
Encode and mask data inside pixels


This is concept code at the moment. Alpha-level stuff.



### Concept

pixelcamo attempts to hide data by encoding it into rgb values in pixels.

#### Step 1 - encode data
First it splits each byte up into the first 4 bits, and last 4 bits (which allows for 2^4=16 different values).
This causes the pixelcamo-"encoded" version of the data to be twice the size. The reason for this will be explained further down.


#### Step 2 - Pixel pattern
This step is up to the implementing program to decide. The main goal is to determine the frequency of data inside an image. (I.e. to use every second pixel as a data store)


#### Step 3 - masking
Pixelcamo masks data by using the rgb-value of an adjacent pixel, and letting the data represent that rgb-value as an estimate.
This is made possible by the pixelcamo-encoded data, which makes any r,g or b value to always be within 16 digits of the adjacent pixel, and therefor have a color similar, and sometimes exactly the same.



### Example - without image


```python
import pixelcamo

data = "Hello world"
bdata = []

# convert ascii to byte array
for c in data: 
  bdata.append(ord(c))
pxenc = pixelcamo.encode(bdata)
print bdata
# Outputs: [72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]

print pxenc
# Outputs: [4, 8, 6, 5, 6, 12, 6, 12, 6, 15, 2, 0, 7, 7, 6, 15, 7, 2, 6, 12, 6, 4]

# Now, the encoded data can be inserted inside an image.
# For the example, we will just use the first three values of the encoded data

adjPixel = (231, 53, 67) # RGB of the adjacent pixel we want to look like

rgb = pixelcamo.camo(pxenc[0], pxenc[1], pxenc[2], adjPixel) # rgb value of the "data-pixel"

print rgb
# Outputs: (228, 56, 70)
```

To compare, the adjacent pixel on the left, and the data-pixel on the right.
<img src="http://placehold.it/150x150/E73543/FFFFFF&text=%28231,+53,+67%29" alt="" />
<img src="http://placehold.it/150x150/E43846/FFFFFF&text=%28228,+56,+70%29" alt="" />




