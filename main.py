# Chip-8 

import sys

class Register:
    def __init__(self, size, value=0):
        self.value, self.size = value, size
        self.mask = 2**size - 1

    def __str__(self):
        return str(self.value) + str(self.size) + str(self.mask)

class Cpu:
    def __init__(self):
        print("TODO")

    
def main():

    filename = sys.argv[1]

    file = open(filename, 'rb').read()

    print(file)

    testreg = Register(16)
    print(testreg)

    testcpu = Cpu()

if __name__ == "__main__":
    main()
