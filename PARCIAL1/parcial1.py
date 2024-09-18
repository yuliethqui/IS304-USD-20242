class Fraccion:
    def __init__(self, num=0, den=1):
        self.num = num
        self.den = den

    def set(self, num, den):
        self.num = num
        self.den = den

    def set_num(self, x):
        self.num = x

    def set_den(self, x):
        if x == 0:
            self.den = 1
        else:
            self.den = x

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

def main():
    b = 23
    fr = Fraccion()
    fs = Fraccion(3, 5)
    fr.set_num(1)
    fr.set_den(0)
    print(f"{fr.get_num()}/{fr.get_den()}")
    print(f"{fs.get_num()}/{fs.get_den()}")
    fs.set(8, 9)
    print(f"{fs.get_num()}/{fs.get_den()}")

if __name__ == "__main__":
    main()
