import math
# masks for extracting bits
m1 = 0b11110000
m2 = 0b00001111

def encode(data): # split each byte up into 2 values
    encoded = []
    for c in data:
        encoded.append((c & m1) >> 4) # extract the 4 first bits, and shift them down to 0-15 range
        encoded.append(c & m2) # extract the 4 last bits
    return encoded

def decode(data):
    decoded = []
    if len(data) % 2 != 0: 
        raise ValueError, "Invalid data array, length must be multiple of 2"
    for i in xrange(0, len(data), 2):
        decoded.append(data[i] << 4 | data[i+1]) # reconstruct the split bytes
    return decoded
        
            
def camo(d1, d2, d3, bPixel): # mask three pixelcamo-encoded bytes to look like bPixel
    return (net(d1, bPixel[0]), net(d2, bPixel[1]), net(d3, bPixel[2]))

def uncamo(pixel, bPixel): # unmask a pixel that looks like pPixel, into three pixelcamo-encoded bytes
    d1, d2, d3 = pixel
    return (denet(d1, bPixel[0]), denet(d2, bPixel[1]), denet(d3, bPixel[2]))


# "net" is a reference to camo-nets. It sounds cool, okay?

def net(d1, p1): # find which section p1 is in, and transform d1 from data to color value in that section
    section = math.floor(p1 / 16.0)
    return int(16*section + d1)

def denet(d1, p1): # find which section p1 is in, and transform d1 from color value in that section to data
    section = math.floor(p1 / 16.0)
    return int(d1 - (section*16))
