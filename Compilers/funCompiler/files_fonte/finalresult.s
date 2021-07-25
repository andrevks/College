.global main 
.func main 
main: 
LDR R1, =backup_lr @Address of the var 
STR LR, [R1]  @Store LinkRegister in var 
@------BEGIN--------

LDR R0, =string0 @Send variable address
BL printf  @Function to receive input from the keyboard

LDR R0, =pattern @int pattern (%d)
LDR R1, =max @Send variable address
BL scanf  @Function to receive input from the keyboard

LDR R1,=max @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
PUSH {R2} @(Result) to the stack

MOV R2, #1 @Move value to the R2
PUSH {R2} @(Result) to the stack

@ADD
POP {R1} 
POP {R0} 
ADD R2, R0, R1  @R2 = R0 + R1
PUSH {R2} @(Result) to the stack
@END-ADD
POP {R2} @Result of the acc from stack to R2

LDR R1, =max @Getting var address
STR R2, [R1]  @Store exp result in var

MOV R2, #1 @Move value to the R2
LDR R1, =counted @Getting var address
STR R2, [R1]  @Store exp result in var

MOV R2, #1 @Move value to the R2
LDR R1, =factorial @Getting var address
STR R2, [R1]  @Store exp result in var

LDR R0, =string1 @Send variable address
BL printf  @Function to receive input from the keyboard

_enquanto0: @Loop label before condition
@CONDITION
LDR R1,=counted @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
MOV R3, R2  @Send end result to R3
LDR R1,=max @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
CMP R3, R2  @Compare R3 and R2, changes flags status
@END-CONDITION
BEQ _fim_enquanto1  @Jumps if R3 == R1
@EXPRESSIONS
LDR R1,=factorial @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
PUSH {R2} @(Result) to the stack

LDR R1,=counted @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
PUSH {R2} @(Result) to the stack

@MULT
POP {R1} 
POP {R0} 
MUL R2, R0, R1 @R2 = R0 * R1
PUSH {R2} @(Result) to the stack
@END-MULT
POP {R2} @Result of the acc from stack to R2

LDR R1, =factorial @Getting var address
STR R2, [R1]  @Store exp result in var

LDR R1,=counted @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
PUSH {R2} @(Result) to the stack

MOV R2, #1 @Move value to the R2
PUSH {R2} @(Result) to the stack

@ADD
POP {R1} 
POP {R0} 
ADD R2, R0, R1  @R2 = R0 + R1
PUSH {R2} @(Result) to the stack
@END-ADD
POP {R2} @Result of the acc from stack to R2

LDR R1, =counted @Getting var address
STR R2, [R1]  @Store exp result in var

@END-EXPRESSIONS
B _enquanto0 @Jumps unconditionally 
_fim_enquanto1: 
LDR R0, =string2 @Send variable address
BL printf  @Function to receive input from the keyboard

LDR R0, =pattern_print @int pattern (%d)
LDR R1, =factorial @Send variable address
LDR R1, [R1] @Send variable address
BL printf  @Function to receive input from the keyboard

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
max: .word 0 
counted: .word 0 
factorial: .word 0 
string0: .asciz "Digite o fatorial que quer encontrar:\n"  
string1: .asciz " \n"  
string2: .asciz "O resultado do fatorial eh: \n"  
