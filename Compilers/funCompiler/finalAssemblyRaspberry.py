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
        while l_index < len(inter_code):
            inter_line = inter_code[l_index].split()[0]

            if inter_line == 'leia':
                inter_line = inter_code[l_index].split()[1]
                self.append_final_code('LDR R0, =pattern', '@ int pattern (%d)')
                self.append_final_code(f'LDR R1, ={inter_line}', '@Send variable address')
                self.append_final_code(f'BL, scanf', ' @Function to receive input\n')

            l_index += 1

        print("\n-----------FINAL CODE-------------")
        for line in self.__final_code:
            print(line)
