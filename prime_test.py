#-------------------------------------------------------------------------------
# Name:        prime_test
# Purpose:
#
# Author:      brian hartz
#              brianhartz@gmail.com
#
# Created:     19-09-2013
# Copyright:   (c) bhartz 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import argparse,sys


def main():
    parser = argparse.ArgumentParser(description="Is it a prime?")

    parser.add_argument("Number", type=int)

    args = parser.parse_args()

    num = args.Number

    test_list = range(num/2)
    test_list.reverse()

    for i in test_list:
        if num % (i) == 0:
            if i == 1:
                print "number {} is a prime".format(num)
                break
            else:
                print "Number {} is not a prime, divisible by {}".format(num, (i))
                break


if __name__ == '__main__':
    main()
