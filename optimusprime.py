#-------------------------------------------------------------------------------
# Name:        optimusPrime
# Purpose:     Figure out if a number is a prime
#
# Author:      brian hartz
#
# Created:     18-11-2013
# Copyright:   (c) brianhartz 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def optimusPrime(test_num):
    # test if number is even a number let alone an integer
    if not type(test_num) == int:
        print "Not a valid input integer"
        return
    # check if number is divisible by 2 or <=7 or zero,
    # then create list of numbers for prime testing, explained below
    if test_num in (0,1):
        print "Number {} is not a prime".format(test_num)
        return
    elif test_num in (2,3,5,7):
        print "Number {} is a prime".format(test_num)
        return
    # see prime test below for explination
    elif test_num % 2 == 0:
        print "Number {} is not a prime, divisible by 2".format(test_num)
        return
    else:
        # Create a list of all numbers that are less than (test_num/2)
        test_list = range((test_num/2))
    # reverse list for prime test
    test_list.reverse()

    # prime test: Loop through all numbers in test_list, and if the remainder of
    # test_num / test_list is equal to zero, then it is not a prime, unless the
    # list gets all the way to 1, then it is a prime. All of this is quickly
    # calculated using the amazing modulo operator '%'
    for i in test_list:
        if test_num % (i) == 0:
            if i == 1:
                print "Number {} is a prime".format(test_num)
                return
            else:
                print "Number {} is not a prime, divisible by {}".format(test_num, (i))
                return

def main():
    pass

if __name__ == '__main__':
    main()
