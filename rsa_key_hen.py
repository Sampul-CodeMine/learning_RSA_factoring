import math

"""Function to calculate LCM"""


def get_lcm(arr):
    lcm = arr[0]
    for itr in range(1, len(arr)):
        lcm = lcm * arr[itr] // math.gcd(lcm, arr[itr])
    print(f"LCM: {lcm}")
    return lcm


"""Function to perform Modular Multiplicative Inverse"""


def mod_mul_inv(ele, tot):
    for itr in range(1, tot):
        if ((ele % tot) * (itr % tot) % tot) == 1:
            print(itr)
            return itr
    return -1


"""Two prime numbers p and q chosen at random """
p = 41
q = 211
n = p * q
totient_val = (p - 1) * (q - 1)  # using totient of n
lcm_val = get_lcm([p - 1, q - 1])  # using the lcm of (p, q)

e = 113  # choose a prime integer value

# Getting the decryption key using the Totient for n
for i in range(1, totient_val):
    if ((e % totient_val) * (i % totient_val) % totient_val) == 1:
        print(i)

for j in range(1, lcm_val):
    if ((e % lcm_val) * (j % lcm_val) % lcm_val) == 1:
        print(j)
