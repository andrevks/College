.global main 
.func main 
main: 
LDR R1, =backup_lr @Address of the var 
STR LR, [R1]  @Store LinkRegister in var 
@------BEGIN--------

LDR R0, =string0 @Send variable address
BL printf  @Function to receive input from the keyboard

MOV R2, #1 @Move value to the R2
LDR R1, =x @Getting var address
STR R2, [R1]  @Store exp result in var

MOV R2, #2 @Move value to the R2
LDR R1, =y @Getting var address
STR R2, [R1]  @Store exp result in var

MOV R2, #1 @Move value to the R2
LDR R1, =z @Getting var address
STR R2, [R1]  @Store exp result in var

MOV R2, #2 @Move value to the R2
LDR R1, =t @Getting var address
STR R2, [R1]  @Store exp result in var

MOV R2, #1 @Move value to the R2
LDR R1, =a @Getting var address
STR R2, [R1]  @Store exp result in var

MOV R2, #2 @Move value to the R2
LDR R1, =b @Getting var address
STR R2, [R1]  @Store exp result in var

@CONDITION
LDR R1,=a @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
MOV R3, R2  @Send end result to R3
LDR R1,=b @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
CMP R3, R2  @Compare R3 and R2, changes flags status
@END-CONDITION
BNE _se0  @Jumps if R3 > R1 (Zero is not set)
B _senao1 @Jumps unconditionally 
_se0: @add symbol after expr
LDR R0, =string1 @Send variable address
BL printf  @Function to receive input from the keyboard

_senao1: 
@CONDITION
LDR R1,=x @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
MOV R3, R2  @Send end result to R3
LDR R1,=y @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
CMP R3, R2  @Compare R3 and R2, changes flags status
@END-CONDITION
BGT _se2  @Jumps if R3 > R1 (Zero is set)
B _senao3 @Jumps unconditionally 
_se2: @add symbol after expr
LDR R0, =string2 @Send variable address
BL printf  @Function to receive input from the keyboard

_senao3: 
@CONDITION
LDR R1,=z @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
MOV R3, R2  @Send end result to R3
LDR R1,=t @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
CMP R3, R2  @Compare R3 and R2, changes flags status
@END-CONDITION
BLT _se4  @Jumps if R3 < R1
B _senao5 @Jumps unconditionally (R3 == R1)
_se4: @add symbol after expr
LDR R0, =string3 @Send variable address
BL printf  @Function to receive input from the keyboard

_senao5: 
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
x: .word 0 
y: .word 0 
z: .word 0 
t: .word 0 
a: .word 0 
b: .word 0 
string0: .asciz "INICIO DO PROGRAMA\n"  
string1: .asciz "a <> b\n"  
string2: .asciz "x > y\n"  
string3: .asciz "z < t\n"  
