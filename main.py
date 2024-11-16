class Stack:
    def __init__(self):
        # Initialize an empty list to store stack items
        self.items = []
        return
    
    def getSize(self):
        # Return stack size
        return len(self.items)

    def is_empty(self):
        # Return True if the stack is empty, otherwise False
        if len(self.items) == 0:
            return True
        else:
            return False
       
    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)
        return

    def pop(self):
        # Remove and return the top item from the stack if it's not empty
        # If the stack is empty, return None
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()
        
    def peek(self):
        # Return the top item without removing it if the stack is not empty
        # If the stack is empty, return None
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1]



''' PARENTHESES '''



def is_balanced(expression):
    # Create a stack to keep track of opening parentheses
    stack = Stack()

    # Define matching pairs for parentheses
    opening = "({["
    closing = ")}]"
    matches = {')': '(', '}': '{', ']': '['}

    # Loop through each character in the expression
    for char in expression:
        # Check if the character is an opening parenthesis
        if char in opening:
            # Push the opening parenthesis to the stack
           stack.push(char)

        # Check if the character is a closing parenthesis
        elif char in closing:
            # If stack is empty or top of stack doesn't match the closing parenthesis, return False
            # Otherwise, pop the top of the stack
           if stack.is_empty() == None or matches[char] != stack.peek():
               return False
           else:
               stack.pop()

    # If stack is empty, all parentheses were matched; otherwise, return False
    return stack.is_empty() 

# Test cases 
expression1 = "({X+Y}*Z)"
expression2 = "{X+Y}*Z)"
expression3 = "({X+Y}*Z"
expression4 = "[A+B]*({X+Y}]*Z)"

# Expected output: True, False, False, False respectively
print(is_balanced(expression1))
print(is_balanced(expression2))
print(is_balanced(expression3))
print(is_balanced(expression4))



''' CALCULATOR '''
''' Jose: Been trying to figure out how to make the calculator functions work for over 5 hours now.
I gave it my all, can't seem to figure out exactly what is wrong and how to fix it. I know it is somewhere
between the apply_operator function and the combo of ["elif char == ')':" and "elif char in "+-*/":"].
Honestly, not sure exactly how to fix it. Uploading -- hoping for the best. (15/11/24)'''



def evaluate_expression(expression):
    # Initialize two stacks: one for numbers and one for operators
    num_stack = Stack()  # Stack for numbers
    op_stack = Stack()   # Stack for operators

    # Define a helper function to apply an operator to the top two numbers on num_stack
    def apply_operator():
        # Pop the top operator from op_stack
        # Pop the top two numbers from num_stack
        # Perform the operation and push the result back to num_stack
        operator = op_stack.pop()
        num1 = num_stack.pop()
        print(num1)
        num1 = float(num1)
        num2 = num_stack.pop()
        print(num2)
        if num2 is None:
            op_stack.push(operator)
            num_stack.push(num1)
            return
        else:
            num2 = float(num2)
            if operator == '*':
                num = num1 * num2
                num_stack.push(str(num))
                return
            elif operator == '/':
                num = num1 / num2
                num_stack.push(str(num))
                return
            elif operator == '+':
                num = num1 + num2
                num_stack.push(str(num))
                return
            else:
                num = num1 - num2
                num_stack.push(str(num))
                return

    # Loop through each character in the expression
    i = 0
    while i < len(expression):
        char = expression[i]

        # Ignore whitespace characters
        if char == ' ':
            i += 1
            continue

        # Check if the character is a digit
        if char.isdigit():
            # Parse the entire number and push it to num_stack
            num = ''
            # Continue to accumulate digits for multi-digit numbers
            while i < len(expression) and expression[i].isdigit():
                num += expression[i]
                i += 1
            num_stack.push(num)  # Push the entire number to num_stack
            continue  # Skip the increment at the end, since we've already moved the index

        # Check if the character is an opening parenthesis '('
        elif char == '(':
            # Push '(' to op_stack to mark the start of a group
            op_stack.push(char)

        # Check if the character is a closing parenthesis ')'
        elif char == ')':
            # Pop and apply operators until '(' is found
            find = op_stack.pop()
            while find != '(':
               find = op_stack.pop()

        # If it's an operator (+, -, *, /)
        elif char in "+-*/":
            # Apply operators based on precedence, then push current operator to op_stack
            op_stack.push(char)
            '''num1 = num_stack.pop()
            num1 = float(num1)
            num2 = num_stack.pop()
            if num2 is None:
                num_stack.push(num1)
                op_stack.push(char)
            else:
                num2 = float(num2)
                if char == '*':
                    num = num1 * num2
                    num_stack.push(str(num))
                elif char == '/':
                    num = num1 / num2
                    num_stack.push(str(num))
                elif char == '+':
                    num = num1 + num2
                    num_stack.push(str(num))
                else:
                    num = num1 - num2
                    num_stack.push(str(num))'''     

        # Move to the next character
        i += 1

    # After the loop, apply any remaining operators in op_stack
    while not op_stack.is_empty():
        apply_operator()

    # Return the final result from num_stack
    return num_stack.pop()

# Test cases 
expression1 = "(((6+9)/3)*(6-4))"
expression2 = "10 + (2 * (6 + 4))"
expression3 = "100 * (2 + 12) / 4"

# Expected output: 10, 30, 350 respectively
print(evaluate_expression(expression1))
print(evaluate_expression(expression2))
print(evaluate_expression(expression3))
