#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    name = sys.argv[0]
    number = len(sys.argv) - 1
    args = sys.argv[1:]
    if number == 0:
        print("{} arguments.".format(number))
    elif number == 1:
        print("{} argument".format(number))
    else:
        print("{} arguments:".format(number))
    for i in range(0, number):
        print("{:d}: {}".format(i + 1, args[i]))
