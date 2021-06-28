.data 
.balign 4
question: .asciz "Escolha a operação (SOM:1,SUB:2,MUL:3,DIV:4)\n"

.balign 4
op: .asciz "DIV: (%d/%d) =: %d\n" 

.balign 4
result: .asciz "Resultado da operação: %d\n"

.balign 4
number: .word 0

.balign 4
pattern: .asciz "%d"

.balign 4
backup_lr: .word 

.balign 4
backup_lr1: .word

.text
.global main
.func main
main: 
  LDR R1, addr_backup_lr @Address for the linkRegister
  STR lr, [R1] @Store value to R1
  @---------------
  LDR R0, addr_question @Storing the string in question
  BL printf @jump and come back
  @scanf:
  LDR R0, addr_pattern @%d
  LDR R1, addr_number  @value stored from the keyboard
  BL scanf
  @result:
  LDR R0, addr_result @String Result: %d
  LDR R1, addr_number @Address number stored
  LDR R1, [R1] @Getting the value out
  BL printf




  @---------------
  LDR lr, addr_backup_lr@End func, reset LR
  LDR lr, [lr]
  BX lr@Return for the main
@Address for the data:
addr_question: .word question
addr_op: .word op
addr_pattern: .word pattern
addr_number: .word number
addr_result: .word result
addr_backup_lr: .word backup_lr
addr_backup_lr1: .word backup_lr1

.global printf
.global scanf