# UGR Driverless X GUTS Code Olympics 2021

This repository houses the UGRacing challenges for the GUTS Code Olympics 2021 competition.

## Challenge 1: UGRDV-64 (easy)

Our team head doesn't use a password manager.  He keeps his main password in this file and encodes it with Base 64 for "security reasons".  He repeats the encoding several times, but we all maintain that this is insecure.

We're not exactly sure how many times he encoded the password, but could you help us prove it?

Write a program that decodes the data in the file. Your program should return a tuple of `(decoded_password, <number_of_times_encoded>)`.

**HINT**: The password starts with `flag{`

## Challenge 2: UGRDV Really-Stupid-Algorithm (medium)

Thanks to you, our team head saw the error in his ways, so he got the IT team to help him with his password security. They told him to use an *actual* encryption algorithm, so he opted for RSA.  However, IT seem to think that because his password is encrypted, and without access to the decryption key, his password is safe.

Write a program to decrypt the encrypted password (`c`) using the prime numbers specified in the file (`p`, `q`, and `e`). Your program should return the password in cleartext

**HINT**: Do you understand RSA? Here's a [link](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) that might help... 

## Challenge 3: UGRDV Cone Detection (easy)

Now that the password issues have been sorted, we can actually start developing. One of the main problems we have in the Driverless team at UGRacing is finding the coordinates of the cones from our stereo camera. Our approach is to use the coordinates from the left and the right camera and take the mean to find the exact coordinates of the cone.

Given two arrays of tuples of x and y coordinates (floats) retrieved from the left and right camera, respectively, write a program to calculate the mean of the coordinates. Your program should return an array of tuples containing the mean x and y values, as floats. You can also assume that there are an equal number of tuples in each array. For example, the arrays `[(3.0, 9.0), (12.0, 16.0)]` and `[(4.0, 10.0), (13.0, 17.0)]` should return a single array `[(3.5, 9.5), (12.5, 16.5)]`.
