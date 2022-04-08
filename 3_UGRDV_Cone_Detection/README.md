# Challenge 3: UGRDV Cone Detection (easy)

Now that the password issues have been sorted, we can actually start developing. One of the main problems we have in the Driverless team at UGRacing is finding the coordinates of the cones from our stereo camera. Our approach is to use the coordinates from the left and the right camera and take the mean to find the exact coordinates of the cone.

Given two arrays of tuples of x and y coordinates (floats) retrieved from the left and right camera, respectively, write a program to calculate the mean of the coordinates. Your program should return an array of tuples containing the mean x and y values, as floats. You can also assume that there are an equal number of tuples in each array. For example, the arrays `[(3.0, 9.0), (12.0, 16.0)]` and `[(4.0, 10.0), (13.0, 17.0)]` should return a single array `[(3.5, 9.5), (12.5, 16.5)]`.
