from numpy import ones,vstack
from numpy.linalg import lstsq
points = [(-2.69, 0.08456668727190535),(-2.7,0.08468661430654152),(-2.71,0.08480935420882739)]
x_coords, y_coords = zip(*points)
A = vstack([x_coords,ones(len(x_coords))]).T
m, c = lstsq(A, y_coords)[0]
print("Line Solution is y = {m}x + {c}".format(m=m,c=c))
