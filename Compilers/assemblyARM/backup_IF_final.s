.global main 
.func main 
main: 
LDR R1, =backup_lr @Address of the var 
STR LR, [R1]  @Store LinkRegister in var 
@------BEGIN--------

LDR R0, =string0 @Send variable address
BL printf  @Function to receive input from the keyboard

LDR R0, =pattern @int pattern (%d)
LDR R1, =taxas @Send variable address
BL scanf  @Function to receive input from the keyboard

LDR R1,=taxas @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
MOV R3, R2  @Send end result to R3
MOV R2, #123 @Move value to the R2
CMP R3, R2  @Compare R3 and R2, changes flags status
BLT _se0  @Jumps if R3 < R1
B _senao1 @Jumps unconditionally (R3 == R1)
_se0: @add symbol after expr
LDR R0, =string1 @Send variable address
BL printf  @Function to receive input from the keyboard

_senao1: 
LDR R1,=taxas @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
MOV R3, R2  @Send end result to R3
MOV R2, #123 @Move value to the R2
CMP R3, R2  @Compare R3 and R2, changes flags status
BGT _se2  @Jumps if R3 > R1 (Zero is set)
B _senao3 @Jumps unconditionally 
_se2: @add symbol after expr
LDR R0, =string2 @Send variable address
BL printf  @Function to receive input from the keyboard

_senao3: 
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
taxas: .word 0 
string0: .asciz "Digite o valor da taxa\n"  
string1: .asciz "EH MENOR ( < )\n"  
string2: .asciz "EH MAIOR ( > )\n"  

