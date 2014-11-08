import math
m1 = 0b11110000
m2 = 0b00001111

def encode(data):
    encoded = []
    for c in data:
        encoded.append((c & m1) >> 4)
        encoded.append(c & m2)
    return encoded

def decode(data):
    decoded = []
    if len(data) % 2 != 0:
        raise ValueError, "Invalid data array, length must be multiple of 2"
    for i in xrange(0, len(data), 2):
        decoded.append(data[i] << 4 | data[i+1])
    return decoded
        
            
def camo(d1, d2, d3, bPixel):
    return (net(d1, bPixel[0]), net(d2, bPixel[1]), net(d3, bPixel[2]))

def uncamo(pixel, bPixel):
    d1, d2, d3 = pixel
    return (denet(d1, bPixel[0]), denet(d2, bPixel[1]), denet(d3, bPixel[2]))

def net(d1, p1):
    section = math.floor(p1 / 16.0)
    return int(16*section + d1)

def denet(d1, p1):
    section = math.floor(p1 / 16.0)
    return int(d1 - (section*16))
