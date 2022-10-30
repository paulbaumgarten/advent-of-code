from pprint import pprint
import time

def inverse(a, m):
    """
    Modular Multiplicative Inverse.
    Definition from https://en.wikipedia.org/wiki/Modular_multiplicative_inverse

    A modular multiplicative inverse of an integer `a` is an integer `x` such that 
    the product `a*x` is congruent to `1` with respect to the modulus `m`.

    Return x, given a & m
    """
    # Brute force it?
    x = 1
    while True:
        if (a*x) % m == 1:
            return x
        x += 1

def chinese_remainder(numbers, remainders):
    """
    Chinese remainder theorem is a rule that...
    Given a set of numbers and a set of remainders,
    Find the smallest number, x, that when you divide by number num[i] gives remainder rem[i] for all numbers and remainders

    Eg: numbers =    [3, 4, 5]
        remainders = [2, 3, 1]
    The smallest number is 11 because...
    11 mod 3 == 2
    11 mod 4 == 3
    11 mod 5 == 1
    """
    # Find size of datasets
    size = len(numbers) # Assuming matches len(remainders)
    # Find product of all numbers
    product = 1
    for i in range(0, size) : 
        product = product * numbers[i] 
    # Intialise result
    result = 0
    for i in range(0, size):
        # Find the product without the current number as a factor
        product_excluding_current = product // numbers[i]
        # Formula requies a "Modular Multiplicative Inverse"
        result += remainders[i] * inverse(product_excluding_current, numbers[i]) * product_excluding_current
    return result % product

def problem2b(buses):
    numbers = []
    remainders = []
    increment = 0
    for bus in buses.split(','):
        if bus != "x":
            numbers.append(int(bus))
            remainders.append(increment)
        increment += 1
    print(numbers)
    print(remainders)
    # Find the substractor
    subtractor = chinese_remainder(numbers, remainders)
    print(f"Subtractor           {subtractor}")
    product = 1
    for i in range(len(numbers)):
        product *= numbers[i]
    print(f"Product              {product}")
    product_subtracted = product - subtractor
    print(f"Product - subtractor {product_subtracted}")
    print("Add back the largest remainder for the end point of the pattern")
    result = product_subtracted + max(remainders)
    print(f"Final                {result}")

def problem1(bus_interval, mytime):
    since_last_bus = mytime % bus_interval
    nextbus = mytime - since_last_bus + bus_interval
    waiting_time = nextbus - mytime
    print(f"Next bus for {bus_interval} is {nextbus}. Waiting time is {waiting_time}. Score is {waiting_time * bus_interval}")
    return nextbus

#### MAIN ####

with open("13.txt", "r") as f:
    content = f.read().splitlines()
mytime = int(content[0])
results = {}
for bus in content[1].replace('x,','').split(","):
    results[ int(bus) ] = problem1(int(bus), mytime)
problem2b(content[1])

# Part 1 answer: 102.
# Part 2 answer: 327300950120029.
