.global main 
.func main 
main: 
LDR R1, =backup_lr @Address of the var 
STR LR, [R1]  @Store LinkRegister in var 
@------BEGIN--------

MOV R2, #8 @Move value to the R2
LDR R1, =old @Getting var address
STR R2, [R1]  @Store exp result in var

LDR R0, =pattern_print
LDR R1, =old
LDR R1, [R1]
BL printf

@------END--------
LDR LR, =backup_lr @Address of the var 
LDR LR, [LR] 
BX LR @Return from the main function

.data @ Data section
.balign 8 @Bytes allocated to each var
pattern: .asciz "%d" @Int format
pattern_print: .asciz "%d\n" 
backup_lr: .word 0
 

.global printf 
.global scanf 
old: .word 0 
