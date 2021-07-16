.global main 
.func main 
main:
  @ @here the LR(Link Register) is stored in a variable
  LDR R1, =backup_lr @Address for the linkRegister
  STR LR, [R1] @Store value to R1
  @ PUSH {IP,LR}
  @------BEGIN--------

  @ESCREVA String
  LDR R0, =question @Storing the string in question
  BL printf @jump and come back

  @LEIA Var
  LDR R0, =pattern
  LDR R1, =variable
  BL scanf

  @ATRIB Var
  LDR R1,=result @after some calculation (sum,sub...)
  LDR R1, [R1]
  LDR R0,=variable
  STR R1, [R0]

  @ATRIB Num
  MOV R0, #1
  LDR R1, =variable2
  STR R0, [R1]

  @ESCREVA STRING
  LDR R0, =string
  BL printf

  @ESCREVA VAR
  LDR R0, =pattern_print
  LDR R1, =variable
  LDR R1, [R1]
  BL printf

  @ESCREVA STRING
  LDR R0, =string2
  BL printf

  @ESCREVA VAR
  LDR R0, =pattern_print
  LDR R1, =variable2
  LDR R1, [R1]
  BL printf


  @-------END---------
_end:
  LDR LR, =backup_lr @End func, reset LR
  LDR LR, [LR]
  BX LR @Return from the main
  @ POP {IP,LR}

.data
.balign 8
@default
pattern: .asciz "%d"
pattern_print: .asciz "%d\n"
backup_lr: .word 0
@Data definition
variable: .word 0  
variable2: .word 0
result: .word 100
string: .asciz "Primeira Var:" 
string2: .asciz "Segunda var:" 
question: .asciz "Digite um numero:\n"
number1: .word 0

.global printf
.global scanf