def steps(number):
    """Execute the Collatz conjecture on a number, and return the number of steps
    parameter : number, the number to start
    Return : the number of steps to reach 1"""

    if (number < 1):
        raise ValueError("Only positive integers are allowed")
        
    nb_steps = 0
    while (number != 1):
        if (number % 2 == 0):
            number /= 2
        else:
            number = (3 * number) + 1
        nb_steps += 1

    return nb_steps
