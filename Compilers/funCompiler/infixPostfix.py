import re


class StackInfix:
    def __init__(self):
        self.item = []

    def push(self , it):
        self.item.append(it)

    def peek(self):
        if self.isempty():
            return 0
        return self.item[-1]

    def pop(self):
        if self.isempty():
            return 0
        return self.item.pop()

    def length(self):
        return len(self.item)

    def isempty(self):
        if self.item == []:
            return True
        else:
            return False

    def display(self):
        if self.isempty():
            return
        temps = stack()
        while not self.isempty():
            x = self.peek()
            temps.push(x)
            self.pop()
        while not temps.isempty():
            x = temps.peek()
            self.push(x)
            temps.pop()

    def isOperand(self, ch):
        #create your own definition of ID here
        pattern = r'[A-Za-z]|\d|_'
        result = re.match(pattern, ch)
        if result:
            return True
        return False
        # return ch.isalpha()


    def notGreater(self, i):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        if self.peek() == '(':
            return False
        a = precedence[i]
        if not self.isempty():
            b = precedence[self.peek()]
        else:
            b = 0

        if a <= b:
            return True
        else:
            return False

    def infixToPostfix(self, exp):
        postfix = ""
        for i in exp:
            if self.isOperand(i):  # check if operand add to output
                postfix = postfix + i

            # If the character is an '(', push it to stack
            elif i == '(':
                self.push(i)

            elif i == ')':  # if ')' pop till '('
                while (not self.isempty()) and self.peek() != '(':
                    n = self.pop() + ' '
                    # postfix += ' '
                    postfix = postfix + ' ' + n
                if (not self.isempty()) and self.peek() != '(':
                    return -1
                else:
                    #Delete '('
                    x = self.pop()
            elif i == '+' or i == '-' or i == '/' or i == '*':
                postfix += ' '
                while (not self.isempty()) and self.notGreater(i):
                    c = self.pop()
                    postfix = postfix + c + ' '
                self.push(i)
            else:
                continue
        # pop all the operator from the stack
        while not self.isempty():
            postfix += ' '
            op_par = self.pop() + ' '
            postfix = postfix + op_par
        return postfix



