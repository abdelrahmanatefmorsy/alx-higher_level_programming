#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4 as me
    for i in range(dir(me)):
        if i[0:2] != "__":
            print(i)
