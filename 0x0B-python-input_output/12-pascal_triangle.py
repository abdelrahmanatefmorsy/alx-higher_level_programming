#!/usr/bin/python3
""" module"""


    def pascal_triangle(n):
        """ return list """
        mylist = []
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                mylist.append(j)
        return mylist
