# Playing around with exponential functions i.e 2^3,etc.

# return base ^ power  This does not work 3 ^4 fro this will give 7 as op

def raise_to_power(base, power):
    result = 1;
    for index in range(power):
        result = result * base
    return result


print(raise_to_power(3, 4))  # This gives out 81 as result
