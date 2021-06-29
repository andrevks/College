.data 
.balign 4
question: .asciz "\nEscolha a operação ( SOMA:1 | SUB:2 | MULT:3 | DIV:4 )\n"

.balign 4
option_text: .asciz "Opção: \n"

.balign 4
number1_text: .asciz "1º Numero: \n"

.balign 4
number2_text: .asciz "2º Numero: \n"

.balign 4
result1: .asciz "Resultado da Soma: %d + %d = %d\n"

.balign 4
result2: .asciz "Resultado da Subtração: %d - %d = %d\n"

.balign 4
result3: .asciz "Resultado da Multiplicação: %d * %d = %d\n"

.balign 4
result4: .asciz "Resultado da Divisão: %d / %d = %d\n"

.balign 4
option: .word 0

.balign 4
number1: .word 0

.balign 4
number2: .word 0

.balign 4
pattern: .asciz "%d"

.balign 4
backup_lr: .word 

.text
.global main
.func main
main: 
  LDR R1, addr_backup_lr @Address for the linkRegister
  STR lr, [R1] @Store value to R1
  @------BEGIN---------
_start:
  @Print Initial string
  LDR R0, addr_question @Storing the string in question
  BL printf @jump and come back

_key_input:
  LDR R0, addr_option_text @Storing the string in question
  BL printf @jump and come back

  LDR R0, addr_pattern @%d
  LDR R1, addr_option  @value stored from the keyboard
  BL scanf

  LDR R0, addr_number1_text @Storing the string in question
  BL printf @jump and come back

  LDR R0, addr_pattern @%d
  LDR R1, addr_number1  @value stored from the keyboard
  BL scanf
  
  LDR R0, addr_number2_text @Storing the string in question
  BL printf @jump and come back

  LDR R0, addr_pattern @%d
  LDR R1, addr_number2  @value stored from the keyboard
  BL scanf

_switch:
  LDR R3, addr_option
  LDR R3, [R3]
_load_values:
  LDR R0, addr_number1
  LDR R0, [R0]
  LDR R1, addr_number2
  LDR R1, [R1]
_cases:
  CMP R3, #1 @case 1 ...
    BEQ _sum
  CMP R3, #2
    BEQ _sub
  CMP R3, #3
    BEQ _mult
  CMP R3, #4
    MOV R3, #0
    BEQ _div
  _default:
    BAL _result1

_sum: 
  ADD R3, R0, R1
  BAL _result1

_sub:
  SUB R3, R0, R1
  BAL _result2

_mult:
  MUL R3, R0, R1
  BAL _result3

_div:
  @R1 = divisor
  CMP R0, R1
  SUB R0, R0, R1
  ADD R3, R3, #1 @incr result
  BHI _div
  BAL _result4
  
_result1:
  LDR R0, addr_result1 @String Result: %d
  BAL _print_result

_result2:
  LDR R0, addr_result2 @String Result: %d
  BAL _print_result

_result3:
  LDR R0, addr_result3 @String Result: %d
  BAL _print_result

_result4:
  LDR R0, addr_result4 @String Result: %d
  BAL _print_result

_print_result:
  LDR R1, addr_number1
  LDR R1, [R1]
  LDR R2, addr_number2
  LDR R2, [R2]
  BL printf
  BAL _end
  @------END---------
_end:
  LDR lr, addr_backup_lr@End func, reset LR
  LDR lr, [lr]
  BX lr @Return for the main
@Address for the data:
addr_question: .word question
addr_option_text: .word option_text
addr_number1_text: .word number1_text
addr_number2_text: .word number2_text 
addr_pattern: .word pattern
addr_option: .word option
addr_number1: .word number1
addr_number2: .word number2
addr_result1: .word result1
addr_result2: .word result2
addr_result3: .word result3
addr_result4: .word result4
addr_backup_lr: .word backup_lr


.global printf
.global scanf