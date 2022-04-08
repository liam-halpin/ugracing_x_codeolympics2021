# Challenge 1: UGRDV-64 (easy)

Our team head doesn't use a password manager.  He keeps his main password in this file and encodes it with Base 64 for "security reasons".  He repeats the encoding several times, but we all maintain that this is insecure.

We're not exactly sure how many times he encoded the password, but could you help us prove it?

Write a program that decodes the data in the file. Your program should return a tuple of `(<decoded_password>, <number_of_times_encoded>)`.

**HINT**: The password starts with `flag{`
