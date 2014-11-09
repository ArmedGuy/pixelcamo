# pixelcamo
Encode and mask data inside pixels


This is concept code at the moment. Alpha-level stuff.


##### Wordlist

 * data-pixel: A pixel in an image that uses the rgb-values to store 3 bytes of data.


### Concept

pixelcamo attempts to hide data by encoding it into rgb-values in pixels, and mask the data so that the image looks normal.

#### Step 1 - encode data
First it splits each byte up into the first 4 bits, and last 4 bits (which allows for 2^4=16 different values).
This causes the pixelcamo-encoded version of the data to be twice the size.


#### Step 2 - pixel pattern
This step is up to the implementing program to decide. The main goal is to determine the frequency of data inside an image. (I.e. to use every second pixel as a data-pixel)
The denser the data-pixels are stored, the more data can be stored in an image, BUT it also affects the visual look of the image more. (obviously)


#### Step 3 - masking
Pixelcamo masks data by using the rgb-value of an adjacent pixel, and letting the data-pixel represent that rgb-value as an estimate.
This is made possible by the pixelcamo-encoded data, which makes any r,g or b value to *always* be within 16 digits of the adjacent pixel, and therefor have a color similar, and sometimes exactly the same.

##### Laying the camo-net - the net(d1, p1) function
To encode data for the red channel of a pixel, we declare the variable `d1` (our encoded data-value, a number between 0 and 15), and `p1` which, in this case, is the red channel of our adjacent pixel.
The resulting integer is what becomes the red channel for our data-pixel.

We simply divide the red channel into 16 different sections, and transform the data-value to be within the same section. This gives us `abs(r2 - r1) < 16` which allows us to store data, while retaining similar colors.
```
>>> p1 = 123
>>> d1 = 12
>>> section = math.floor(p1 / 16.0)
>>> result = int(16 * section + d1)
>>> result
124
```


The downside of the algorithm is obviously that the size of the encoded data is twice as large.


### Example - without image


```python
import pixelcamo

data = "Hello world"
bdata = []

# convert ascii to byte array
for c in data: 
  bdata.append(ord(c))
  
pxenc = pixelcamo.encode(bdata) # encode binary data

print bdata
# Outputs: [72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]

print pxenc
# Outputs: [4, 8, 6, 5, 6, 12, 6, 12, 6, 15, 2, 0, 7, 7, 6, 15, 7, 2, 6, 12, 6, 4]

# Now, the encoded data can be inserted inside an image.
# For the example, we will just use the first three values of the encoded data

adjPixel = (231, 53, 67) # RGB of the adjacent pixel we want to look like

rgb = pixelcamo.camo(pxenc[0], pxenc[1], pxenc[2], adjPixel) # rgb value of the data-pixel.

print rgb
# Outputs: (228, 56, 70)

print pixelcamo.uncamo(rgb, adjPixel) # unmask the values
# Outputs: (4, 8, 6)
```

To compare, the adjacent pixel on the left, and the data-pixel on the right.

<img src="http://placehold.it/150x150/E73543/FFFFFF&text=%28231,+53,+67%29" alt="" />
<img src="http://placehold.it/150x150/E43846/FFFFFF&text=%28228,+56,+70%29" alt="" />




