class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1
    
    def pop(self):
        if not self.top:
            return None
        poppped_node = self.top
        self.top = self.top.next
        poppped_node.next = None
        self.size -= 1
        return poppped_node.data
    
    def peek(self):
        if not self.top:
            return None
        return self.top.data
    
    def is_empty(self):
        return self.size==0

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    ops = Stack()
    output = ""

    for token in expression:
        if token.isalnum():
            output += token
        elif token == "(":
            ops.push(token)
        elif token == ")":
            while not ops.is_empty() and ops.peek() != "(":
                output += ops.pop()
            ops.pop()
        else:
            while (not ops.is_empty() and precedence(ops.peek()) >= precedence(token)):
                output += ops.pop()
            ops.push(token)
    
    while not ops.is_empty():
        output += ops.pop()

    return output


def postfix_to_infix(expression):
    stack = Stack()
    operators = set(['+', '-', '*', '/'])

    for token in expression:
        if token not in operators:
            stack.push(token)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            new_expr = f"({op1}{token}{op2})"
            stack.push(new_expr)

    return stack.pop()

if __name__ == "__main__":
    expr = "AB+C*"
    print(postfix_to_infix(expr))
    expr = "a*(b+c)/d"
    postfix = postfix_to_infix(expr)
    print(f"Infix: {expr}")
    print(f"Postfix: {postfix}")