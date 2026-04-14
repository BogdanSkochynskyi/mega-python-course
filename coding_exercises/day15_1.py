import random

lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enter upper bound: "))

def random_number(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)


print(random_number(lower_bound, upper_bound))