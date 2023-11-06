#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    if len(sentence) == 0:
        c = None
    else:
        c = sentence[0]
    y = (x, c)
    return (y)
