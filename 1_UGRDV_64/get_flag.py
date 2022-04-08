#!/usr/bin/env python3

import base64

def ugrdv_challenge_1(password_file):
    """Decode from Base 64 to find the password

    Args:
        password_file: file name containing the encoded password

    Returns:
        tuple: (<decoded_password>, <number_of_times_encoded>)
    """
    password = ""
    n_encoding = 0
    password_found = False

    with open(password_file, "r") as f:
        # read in the password and fix the formatting
        encoded_text = f.readlines()
        encoded_text = "".join(encoded_text)
        encoded_text = encoded_text.replace("\n", "").replace(" ", "")

        # decode from base64 until password is found
        while not password_found:
            n_encoding += 1
            encoded_text = base64.b64decode(encoded_text)
            if b"flag{" in encoded_text:
                password = encoded_text.decode()
                password_found = True
    return (password, n_encoding)


# driver code
if __name__ == "__main__":
    print(ugrdv_challenge_1("super_secure_password.txt"))  # ("flag{j01n_ugr_dr1v3rl3ss}", 15)
