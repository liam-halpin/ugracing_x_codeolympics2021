#!/usr/bin/env python3

from Crypto.Util.number import inverse

def ugrdv_challenge_2():
	"""Using the primes, p, q, and e, decrypt c to find the password

	Returns:
		str: decrypted password in cleartext
	"""
	c = 827917049735351705182196799205489665205453711705680183817600093460407091538598548
	p = 1899107986527483535344517113948531328331
	q = 674357869540600933870145899564746495319033
	e = 65537

	# n = p x q
	n = p * q

	# phi = (p - 1) x (q - 1)
	phi = (p - 1) * (q - 1)

	# d = e^-1 mod phi
	d = inverse(e, phi)

	# m = c^d mod n
	m = pow(c, d, n)

	# decode from hex and remove "0x"
	password = bytes.fromhex(hex(m)[2:]).decode("utf-8")
	return password


# driver code
if __name__ == "__main__":
	print(ugrdv_challenge_2())  # flag{d0_y0u_3v3n_RSA_br0}
