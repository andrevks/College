.data
.balign 4
backup_lr: .word

.balign 4
pattern: .asciz "%d"

@_Var
.balign 4
variable: .word 0  

@_Var
.balign 4
variable2: .word 1

@_String
.balign 4
string: .asciz "Primeira var: %d\n" 

@_String
.balign 4
string2: .asciz "Segunda var\n" 

.balign 4
number1: .word 0

.text @if the data section is before it
.global main @indicate the label to start
.func main 
main:
  @here the LR(Link Register) is stored in a variable
  LDR R1, addr_backup_lr @Address for the linkRegister
  STR lr, [R1] @Store value to R1
  @------BEGIN--------

  LDR R0, addr_pattern @%d
  LDR R1, addr_number1  @value stored from the keyboard
  BL scanf

  @LEIA and put in the variable
  @ LDR R0, addr_pattern
  @ LDR R1, addr_variable
  @ BL scanf

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
  LDR R1, addr_number1
  LDR R1, [R1]
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
  BX lr @Return for the main

@Default var address
addr_backup_lr: .word backup_lr
addr_pattern: .word pattern

@Var address
addr_variable: .word variable 
addr_variable2: .word variable2
addr_number1: .word number1
addr_string: .word string
addr_string2: .word string2

@lib_c
.global printf
.global scanf