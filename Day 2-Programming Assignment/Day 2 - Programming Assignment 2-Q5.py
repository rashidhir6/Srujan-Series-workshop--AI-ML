Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.


#   5.  Write a program to
#          (a) read a .csv file in a numpy array and
#          (b) write a numpy array to a .csv file.


# (a)Saving a NumPy array as a csv file
import numpy as np

my_array = np.loadtxt('iris.csv',delimiter=",", skiprows=1)

print (my_array[0:10,:]) # prints first 10 rows




# (b)saving a NumPy array to a csv. 


np.savetxt("numpy_data.csv", my_array, delimiter=",")


