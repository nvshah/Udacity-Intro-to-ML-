""" quiz materials for feature scaling clustering """

# Appraoch 1 (Manual)

### FYI, the most straightforward implementation might 
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!  
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    least, peak = min(arr), max(arr)
    if least == peak:
        # raise ZeroDivisionError
        return [0.5] * len(arr)
    
    return [(e - least) / (peak-least) for e in arr]

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print(featureScaling(data))



# Appraoch 2 (library)

from sklearn.preprocessing import MinMaxScaler
import numpy

arr = numpy.array([[115.], [140.], [175.]])  # Assume each data point has only single feature i.e 1D simulate as 2D
# fit = find min and max
# transform = apply formula
scaled_arr = MinMaxScaler().fit_transform(arr)

print(scaled_arr)
