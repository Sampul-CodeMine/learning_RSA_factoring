#!/usr/bin/python3

"""This is a simple project for educational purposes.
It is does not deal with fast program algorithms as per complexities and
executions, but it teaches how multiple factors for a number is computed
and also to check if multiple pairs are co-prime

The program operates from 2 modes:
- If from the CLI a filepath is specified with the program name during
execution, it reads from the file a line at a time and try to generate
factors for the numbers

- If no filename is specified, it generates a random number and solves
for the multiple factors and the co-primes.

Raises:
    If the program freezes, and the CTRL + Z or CTRL + C keys are pressed,
    a KeyboardInterrupt error is generated.
"""

def factorize(val: int) -> list | None:
    """This function gets the multiples of a given number greater than 1

    Examples:
        >>> print(factorize(4))
        [(2, 2)]

        >>> print(factorize(15))
        [(5, 3), (3, 5)]

    Args:
        val (int): Value for which to get its factors/multiples

    Return:
        (None): if `val` is less than 2.
        (list): a list of tuples containing the different multiples of `val`
    """

    local_factor = []
    i_fact = 2    
    if val < 2:
        return    
    for i in range(2, val + 1):
        for j in range(2, val + 1):
            if i * j == val:
                local_factor.append((j, i))
    return local_factor


def is_prime(val: int) -> bool:
    """This function checks if a specified number is a prime number.

    Examples:
        >>> is_prime(3)
        True

        >>> is_prime(4)
        False

    Args:
        val (int): The value to be checked if it is prime or not
    Return:
        (bool): `True` if the number is prime and greater than 1 else `False`
    """

    for num in range(2, val):
        if val % num == 0:
            return False
    return val > 1


def get_factors(val: int) -> list:
    """This function checks deeply if the `val` is a prime number only
    divisible by 1 and itself.

    Examples:
        >>> print(get_factors(4))
        [(2, 2)]

        >>> print(get_factors(7))
        [(7, 1)]

        >>> print(get_factors(15))
        [(5, 3), (3, 5)]

    Args:
        val (int): The value to be checked if it is prime or not

    Return:
        (list): if `val` is a prime, it returns a list of tuple (1 and itself)
        as the only multiples of `val` else it returns a list of tuples with
        all factors/multiples
    """

    if is_prime(val):
        factor = val, 1
        return [(factor)]
    local_factor = factorize(val)
    return local_factor


def factors_are_prime(val: list) -> list | None:
    """This function accepts a list of tuples and check each pair of tuple if
    each element are co-prime

    Examples:
        >>> print(factors_are_prime([(2, 2)]))
        [(2, 2)]

        >>> print(factors_are_prime([(7, 1)]))
        [(7, 1)]

        >>> print(factors_are_prime([(5, 3), (3, 5)]))
        [(5, 3)]

    Args:
        val (list): A list containing the multiples or factors of a given num.

    Return:
        (list): a list with a single tuple if the length of the tuple is 1
                if the length is not one, it scans through the list tuple by
                tuple to check for a pair that are co-prime.
        (None): if no co-prime is found
    """

    if len(val) == 1:
        return val
    for i in val:
        if is_prime(i[0]) and is_prime(i[1]):
            return i
    return


def read_from_file(file_name: str) -> None:
    """This function accepts a filename as an argument, read through each line
    and uses the value as the number to factorize

    Examples:
        >>> read_from_file("tests/test00")
        Generated Number: 623:
        The list of factor(s):
        [(89, 7), (7, 89)]
        623 has prime multiple factors: (89, 7)

        >>> read_from_file("tests/tes")
        [Errno 2] No such file or directory: 'tests/tes'

        # if the value read is a string
        >>> read_from_file("tests/tes")
        invalid literal for int() with base 10: 'value'

    Args:
        file_name (str): A filename specifying the full path to the file to read
        from.

    Raises:
        (FileNotFoundError): if the file specified is not found.
        (ValueError): When the value read from the file is not valid
        (TypeError): If the value read is not of type integer

    Return:
        (None)
    """

    try:
        with open(file_name) as file:
            line = file.readline()
            while line != "":
                number = int(line.split('\n')[0])
                factors = get_factors(number)
                prime_mult_fact = factors_are_prime(factors)
                print(f"Generated Number: {number}: ")
                print(f"The list of factor(s):\n{factors}")

                if prime_mult_fact is None:
                        print(f"{number} has no multiple factors that are both prime.\n")
                else:
                    print(f"{number} has prime multiple factors: {prime_mult_fact}\n")

                line = file.readline()
    except (FileNotFoundError, ValueError, TypeError) as err:
        print(err)


def use_random() -> None:
    """This function generates a random number for the RSA factor

    Examples:
        >>> use_random()
        Generated Number: 571:
        The list of factor(s):
        [(571, 1)]
        571 has prime multiple factors: [(571, 1)]

        >>> use_random()
        Generated Number: 551:
        The list of factor(s):
        [(29, 19), (19, 29)]
        551 has prime multiple factors: (29, 19)

        >>> use_random()
        Generated Number: 290:
        The list of factor(s):
        [(145, 2), (58, 5), (29, 10), (10, 29), (5, 58), (2, 145)]
        290 has no multiple factors that are both prime.

    Return:
        (None):
    """

    lower_range = r.randint(1, 10)
    upper_range = r.randint(100, 1000)
    number_gen = r.randint(lower_range, upper_range)
    factors = get_factors(number_gen)
    prime_mult_fact = factors_are_prime(factors)
    print(f"Generated Number: {number_gen}: ")
    print(f"The list of factor(s):\n{factors}")

    if prime_mult_fact is None:
        print(f"{number_gen} has no multiple factors that are both prime.\n")
    else:
        print(f"{number_gen} has prime multiple factors: {prime_mult_fact}\n")



if __name__ == "__main__":
    from sys import argv
    import random as r
    
    try:
        if len(argv) == 2:
            filename = argv[1]
            read_from_file(filename)
        else:    
            use_random()
    except KeyboardInterrupt:
        print("Program was interrupted.")
