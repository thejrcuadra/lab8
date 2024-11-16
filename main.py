class Stack:
    def __init__(self):
        # Initialize an empty list to store stack items
        self.items = []
        return

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



def evaluate_expression(expression):
    # Initialize two stacks: one for numbers and one for operators
    num_stack = Stack()  # Stack for numbers
    op_stack = Stack()   # Stack for operators

    # Define a helper function to apply an operator to the top two numbers on num_stack
    def apply_operator():
        # Pop the top operator from op_stack
        # Pop the top two numbers from num_stack
        # Perform the operation and push the result back to num_stack
        

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
            

        # Check if the character is an opening parenthesis '('
        elif char == '(':
            # Push '(' to op_stack to mark the start of a group
            

        # Check if the character is a closing parenthesis ')'
        elif char == ')':
            # Pop and apply operators until '(' is found
           

        # If it's an operator (+, -, *, /)
        elif char in "+-*/":
            # Apply operators based on precedence, then push current operator to op_stack
            
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
