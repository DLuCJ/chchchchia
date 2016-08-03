# Chip-8 

import sys

num_gp_regs = 16

class Register:
    def __init__(self, size, value=0):
        self.value, self.size = value, size
        self.mask = 2**size - 1

    def __str__(self):
        return str(self.value) + str(self.size) + str(self.mask)

class Cpu:
    def __init__(self):
        self.reg_gp = [Register(8) for reg in range(num_gp_regs)]

        #TODO: exact sizes?
        self.reg_delay_timer = Register(32)
        self.reg_snd_timer = Register(32)

        self.reg_pc = Register(16)
        self.reg_sp = Register(8)

    
def main():

    filename = sys.argv[1]

    file = open(filename, 'rb').read()

    print(file)

    cpu = Cpu()

    for reg in cpu.reg_gp:
        print(reg)

    print(cpu.reg_delay_timer)
    print(cpu.reg_snd_timer)
    print(cpu.reg_pc)
    print(cpu.reg_sp)


if __name__ == "__main__":
    main()
