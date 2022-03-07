#!/usr/bin/env python3

# Created by Yiyun Qin
# Created on March 2022
# This is the math program, with proper style

import constants


def main():
    # This function calculates the circumference of a circle

    # input
    radius = int(input("Enter the length of the radius (mm): "))

    # process
    circumference = constants.TAU * radius

    # output
    print("")
    print("Circumference is {} mm.".format(circumference))

    print("\nDone.")


if __name__ == "__main__":
    main()
