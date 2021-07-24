.global main 
.func main 
main: 
LDR R1, =backup_lr @Address of the var 
STR LR, [R1]  @Store LinkRegister in var 
@------BEGIN--------

LDR R0, =pattern @int pattern (%d)
LDR R1, =four @Send variable address
BL scanf  @Function to receive input from the keyboard

LDR R0, =pattern @int pattern (%d)
LDR R1, =five @Send variable address
BL scanf  @Function to receive input from the keyboard

LDR R0, =pattern @int pattern (%d)
LDR R1, =twenty @Send variable address
BL scanf  @Function to receive input from the keyboard

LDR R0, =string0 @Send variable address
BL printf  @Function to receive input from the keyboard

LDR R1,=twenty @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
PUSH {R2} @(Result) to the stack

MOV R2, #2 @Move value to the R2
PUSH {R2} @(Result) to the stack

@DIVISION
POP {R1} @Divisor(under bar) from stack
POP {R0} @Dividend(above bar) from stack
MOV R2, #0 @Reset R2(Quotient) to 0
_div0:
 @Begin of the label(div)
CMP R0, R1 @R0 should be >= than R1 to divide
BLT _end_div1 @Jump to end_div if R0 < R1
ADD R2, R2, #1 @Increment R2(Quotient/Result)
SUB R0, R0, R1  @R0 = R0 - R1
B _div0 @Jump to 
_end_div1: 
PUSH {R2} @(Quotient/Result) to the stack
@END-DIVISION
LDR R1,=five @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
PUSH {R2} @(Result) to the stack

MOV R2, #4000 @Move value to the R2
PUSH {R2} @(Result) to the stack

@ADD
POP {R1} 
POP {R0} 
ADD R2, R0, R1  @R2 = R0 + R1
PUSH {R2} @(Result) to the stack
@END-ADD
@MULT
POP {R1} 
POP {R0} 
MUL R2, R0, R1 @R2 = R0 * R1
PUSH {R2} @(Result) to the stack
@END-MULT
LDR R1,=four @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
PUSH {R2} @(Result) to the stack

MOV R2, #40 @Move value to the R2
PUSH {R2} @(Result) to the stack

@MULT
POP {R1} 
POP {R0} 
MUL R2, R0, R1 @R2 = R0 * R1
PUSH {R2} @(Result) to the stack
@END-MULT
@DIVISION
POP {R1} @Divisor(under bar) from stack
POP {R0} @Dividend(above bar) from stack
MOV R2, #0 @Reset R2(Quotient) to 0
_div2:
 @Begin of the label(div)
CMP R0, R1 @R0 should be >= than R1 to divide
BLT _end_div3 @Jump to end_div if R0 < R1
ADD R2, R2, #1 @Increment R2(Quotient/Result)
SUB R0, R0, R1  @R0 = R0 - R1
B _div2 @Jump to 
_end_div3: 
PUSH {R2} @(Quotient/Result) to the stack
@END-DIVISION
POP {R2} @Result of the acc from stack to R2

LDR R1, =valor_total @Getting var address
STR R2, [R1]  @Store exp result in var

LDR R0, =pattern_print @int pattern (%d)
LDR R1, =valor_total @Send variable address
LDR R1, [R1] @Send variable address
BL printf  @Function to receive input from the keyboard

LDR R0, =string1 @Send variable address
BL printf  @Function to receive input from the keyboard

LDR R0, =string2 @Send variable address
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
four: .word 0 
five: .word 0 
twenty: .word 0 
valor_total: .word 0 
string0: .asciz "Resultado valor_total\n"  
string1: .asciz "Invista seu dinheiro\n"  
string2: .asciz "Continue fazendo analises dos precos\n"  
