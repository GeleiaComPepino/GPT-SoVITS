import os

IPABr =[5, 28, 37, 40, 25, 24, 16, 26, 12, 6, 27, 34, 21, 20, 22, 10, 32, 30, 42, 17, 13, 11, 7, 33, 39, 36, 18, 23, 9, 8, 14, 15, 38, 19, 43, 31, 41, 29]
symbols = IPABr
symbols = sorted(set(symbols))
print(symbols)
if __name__ == "__main__":
    print(len(symbols))
