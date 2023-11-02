#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    ln = len(sys.argv) - 1
    sm = 0
    for i in range(0, ln):
        sm = sm + int(args[i])
    print("{:d}".format(sm))
