from util.stack import Stack
import re


def is_digit(elem):
    digit = r'\d'
    return re.match(digit, elem)


def is_variable(elem):
    var_pattern = r'[A-Za-z]|\d|_'
    return re.match(var_pattern, elem)


class FinalRaspberry:
    def __init__(self, intermediate, var_list):
        self.__intermediate_code = intermediate
        self.__var_list = var_list
        self.__final_code = []
        self.__log_final_code = []
        self.__stack = Stack()
        self.__label_num = -1
        self.generate_final_code()

    def calculate_arith_exp(self, ar_exp):
        if len(ar_exp) == 1:
            elem = ar_exp[0]
            self.get_value(elem)
        # else:
        #     for elem in ar_exp:
        #         if elem == '/':


    def get_value(self, elem):
        if is_digit(elem):
            self.append_final_code(f'MOV R2, #{str(elem)}', '@Move value to the R2')
        elif is_variable(elem):
            self.append_final_code(f'LDR R1,={elem}', '@Send address to the R1')
            self.append_final_code(f'LDR R2, [R1]', '@Move value from R2 to var location')

    def append_final_code(self, txt, comment=''):
        self.__final_code.append(f'{txt} {comment}')

    def get_new_label(self, keyword):
        self.__label_num += 1
        return ''.join(f'_{keyword}{self.__label_num}')

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
                self.append_final_code('LDR R0, =pattern', '@int pattern (%d)')
                self.append_final_code(f'LDR R1, ={inter_line}', '@Send variable address')
                self.append_final_code(f'BL scanf', ' @Function to receive input from the keyboard\n')
            elif '=' in inter_code[l_index].split():
                if inter_code[l_index].split()[1] == '=':
                    var = inter_code[l_index].split()[0]
                    ar_exp = inter_code[l_index].split()[2:]

                    self.calculate_arith_exp(ar_exp)
                    self.append_final_code(f'LDR R1, ={var}', '@Getting var address')
                    self.append_final_code(f'STR R2, [R1] ', '@Store exp result in var\n')

            elif inter_line == 'se':
                se_label = self.get_new_label('se')
                senao_label = self.get_new_label('senao')
                self.__stack.push(senao_label)
                inter_line = inter_code[l_index].split()
                print(f"EXPR_IN_SE: {inter_line}")
                i = 1
                OP_RE = ['<>', '=', '<', '>']
                BOOL = ['\\', '&']
                while inter_line[i] != 'entao':
                    elem = inter_line[i]

                    if elem in OP_RE:
                        previous_var = inter_line[i - 1]
                        posterior_var = inter_line[i + 1]
                        self.get_value(previous_var)  # value of a prev_var, send it to R2
                        self.append_final_code(f'MOV R3, R2 ', '@Send end result to R3')
                        self.get_value(posterior_var)  # value of the post_var, send it to R2
                        self.append_final_code(f'CMP R3, R2 ', '@Compare R3 and R2, changes flags status')
                        if elem == '<':
                            self.append_final_code(f'BLT {se_label} ', '@Jumps if R3 < R1')
                            self.append_final_code(f'B {senao_label}', '@Jumps unconditionally (R3 == R1)')
                        elif elem == '>':
                            self.append_final_code(f'BGT {se_label} ', '@Jumps if R3 > R1 (Zero is set)')
                            self.append_final_code(f'B {senao_label}', '@Jumps unconditionally ')
                        elif elem == '=':
                            self.append_final_code(f'BEQ {se_label} ', '@Jumps if R3 == R1 (Zero is set)')
                            self.append_final_code(f'B {senao_label}', '@Jumps unconditionally (R3 <> R1)')
                        elif elem == '<>':
                            self.append_final_code(f'BNE {se_label} ', '@Jumps if R3 > R1 (Zero is not set)')
                            self.append_final_code(f'B {senao_label}', '@Jumps unconditionally ')
                    i += 1
                self.append_final_code(f'{se_label}:', '@add symbol after expr')
            elif inter_line == 'senao':
                fim_se_label = self.get_new_label("fim_se")
                senao_label = self.__stack.pop()
                self.__stack.push(fim_se_label)
                self.append_final_code(f'B {fim_se_label}', '@Jumps unconditionally')
                self.append_final_code(f'{senao_label}:', '@add symbol after expr')
            elif inter_line == 'fim_se':
                fim_label = self.__stack.pop()
                self.append_final_code(f'{fim_label}:')

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
        self.append_final_code(f'\n.global printf')
        self.append_final_code(f'.global scanf')
        for var in self.__var_list:
            self.append_final_code(f'{var}: .word 0', )

        file = open('files_fonte/finalresult.fonte', 'w')
        for line in self.__final_code:
            file.writelines(line + '\n')
            print(line)
        file.close()