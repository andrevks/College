class FinalRaspberry:
    def __init__(self, intermediate, var_list):
        self.__intermediate_code = intermediate
        self.__var_list = var_list
        self.__final_code = []
        self.generate_final_code()

    def append_final_code(self, txt, comment=''):
        self.__final_code.append(f'{txt} {comment}')

    def generate_final_code(self):
        inter_code = self.__intermediate_code
        l_index = 0

        print('\n____FINAL:')

        self.append_final_code('.global main')
        self.append_final_code('.func main')
        self.append_final_code('main:')
        self.append_final_code('LDR R1, =backup_lr', '@Address of the var ')
        self.append_final_code('STR LR, [R1] ', '@Store LinkRegister in var ')
        self.__final_code.append('@------BEGIN--------\n')

        while l_index < len(inter_code):
            inter_line = inter_code[l_index].split()[0]

            if inter_line == 'leia':
                inter_line = inter_code[l_index].split()[1]
                self.append_final_code('LDR R0, =pattern', '@ int pattern (%d)')
                self.append_final_code(f'LDR R1, ={inter_line}', '@Send variable address')
                self.append_final_code(f'BL scanf', ' @Function to receive input\n')

            l_index += 1

        print("\n-----------FINAL CODE-------------")
        self.__final_code.append('@------END--------')
        self.append_final_code('LDR R1, =backup_lr', '@Address of the var ')
        self.append_final_code('LDR LR, [LR]')
        self.append_final_code('BX LR', 'Return from the main function')

        self.append_final_code('\n.data', '@ Data section')
        self.append_final_code('.balign 8', '@Bytes allocated to each var')
        self.append_final_code(f'pattern: .asciz \"%d\"', '@Int format')
        self.append_final_code(f'pattern_print: .asciz \"%d\\n\"')
        self.append_final_code(f'backup_lr: .word 0\n')
        for var in self.__var_list:
            self.append_final_code(f'{var}: .word 0',)

        for line in self.__final_code:
            print(line)
