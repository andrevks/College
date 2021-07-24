.global main 
.func main 
main: 
LDR R1, =backup_lr @Address of the var 
STR LR, [R1]  @Store LinkRegister in var 
@------BEGIN--------

LDR R0, =pattern @int pattern (%d)
LDR R1, =terms_to_calculate @Send variable address
BL scanf  @Function to receive input from the keyboard

LDR R0, =pattern @int pattern (%d)
LDR R1, =old @Send variable address
BL scanf  @Function to receive input from the keyboard

LDR R0, =pattern @int pattern (%d)
LDR R1, =gold @Send variable address
BL scanf  @Function to receive input from the keyboard

LDR R0, =pattern @int pattern (%d)
LDR R1, =acc @Send variable address
BL scanf  @Function to receive input from the keyboard

MOV R2, #0 @Move value to the R2
LDR R1, =counted @Getting var address
STR R2, [R1]  @Store exp result in var

LDR R1,=old @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
PUSH {R2} @(Result) to the stack

MOV R2, #10 @Move value to the R2
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
LDR R1,=gold @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
PUSH {R2} @(Result) to the stack

MOV R2, #1000 @Move value to the R2
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
LDR R1,=acc @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
PUSH {R2} @(Result) to the stack

MOV R2, #400 @Move value to the R2
PUSH {R2} @(Result) to the stack

@ADD
POP {R1} 
POP {R0} 
ADD R2, R0, R1  @R2 = R0 + R1
PUSH {R2} @(Result) to the stack
@END-ADD
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

LDR R1,=n1 @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
PUSH {R2} @(Result) to the stack

LDR R1,=n2 @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
PUSH {R2} @(Result) to the stack

@ADD
POP {R1} 
POP {R0} 
ADD R2, R0, R1  @R2 = R0 + R1
PUSH {R2} @(Result) to the stack
@END-ADD
POP {R2} @Result of the acc from stack to R2

LDR R1, =new_number @Getting var address
STR R2, [R1]  @Store exp result in var

LDR R1,=new_number @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
LDR R1, =n2 @Getting var address
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

B _fim_se4 @Jumps unconditionally
None: @add symbol after expr
_fim_se4: 
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
gold: .word 0 
acc: .word 0 
terms_to_calculate: .word 0 
n1: .word 0 
n2: .word 0 
counted: .word 0 
new_number: .word 0 
valor_total: .word 0 
valor_ethereum: .word 0 
valor_barato: .word 0 
taxas: .word 0 
string1: .asciz "Invista seu dinheiro\n"  
string2: .asciz "Continue fazendo analises dos precos\n"  
