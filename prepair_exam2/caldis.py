import math

def caldistance(x2, y2, x1=3, y1=3):
    dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dis

print(f'distance = {caldistance(6, 9):.2f}')