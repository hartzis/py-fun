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
    #test if number is even a number let alone an integer
    if not type(test_num) == int:
        print "Not a valid input integer"
        return
    #check if number is divisible by 2 and/or <=7 or zero,
    #then create list for prime test
    if test_num == 0:
        print "Zero not valid"
        return
    elif test_num in (1,2,3,5,7):
        print "Number {} is a prime".format(test_num)
        return
    elif test_num % 2 == 0:
        print "Number {} is not a prime, divisible by 2".format(test_num)
        return
    else:
        test_list = range((test_num/2))
    #reverse list for prime test
    test_list.reverse()

    #prime test: check the remainder of each division to see if number is a prime
    #if it gets all the way to 1 it is a prime
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
