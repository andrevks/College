.data
.balign 4
backup_lr: .word

.balign 4
pattern: .asciz "%d"

.balign 4
variable: .word 0  

.balign 4
variable2: .word 1

.balign 4
string: .asciz "Primeira var: %d %d\n" 

.balign 4
string2: .asciz "Segunda var\n" 

.balign 4
question: .asciz "Digite um numero: \n"

.balign 4
number1: .word 0

.text
.global main 
.func main 
main:
  @here the LR(Link Register) is stored in a variable
  LDR R1, addr_backup_lr @Address for the linkRegister
  STR lr, [R1] @Store value to R1
  @------BEGIN--------
_start:
  @Print Initial string
  LDR R0, addr_question @Storing the string in question
  BL printf @jump and come back
  @LEIA and put in the variable

  LDR R0, addr_pattern
  LDR R1, addr_variable1
  BL scanf

  LDR R0, addr_pattern
  LDR R1, addr_variable2
  BL scanf
  @ @ATRIB of two var
  @ LDR R1, addr_variable
  @ STR R0, [R1]

  @ESCREVA string
  @ LDR R0, addr_string @string text
  @ BL printf

  @ESCREVA var
  @ LDR R0, addr_string
  @ LDR R1, addr_variable
  @ LDR R1, [R1]
  @ BL printf

_print_result:
  LDR R0, addr_string
  LDR R1, addr_variable1
  LDR R1, [R1]
  LDR R2, addr_variable2
  LDR R2, [R2]
  BL printf

  @ @ESCREVA string
  @ LDR R0, addr_string2 @string text
  @ BL printf

  @ @ESCREVA var
  @ LDR R0, addr_pattern
  @ LDR R1, addr_variable2
  @ BL printf

  @ LDR R1, addr_variable2
  @ LDR R1, [R1]
  @ ADD R0, R0, R1 


  @-------END---------
_end:
  LDR lr, addr_backup_lr @End func, reset LR
  LDR lr, [lr]
  BX lr @Return from the main

@Default var address
addr_backup_lr: .word backup_lr
addr_pattern: .word pattern
@Var address
addr_variable: .word variable 
addr_variable2: .word variable2
addr_number1: .word number1
addr_string: .word string
addr_string2: .word string2
addr_question: .word question

.global printf
.global scanf