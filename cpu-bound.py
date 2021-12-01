from hashlib import md5
from random import choice
import concurrent.futures


def findToken():
    count = 0
    while count<3:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()
        if h.endswith("00000"):
            count+=1
            print(s, h)


def main():
    findToken()

if __name__ == "__main__":
    main()