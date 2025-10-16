def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():  
            stack.append(int(token))
        else: 
            right = stack.pop()
            left = stack.pop()

            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                stack.append(left / right)
            elif token == '^':
                stack.append(left ** right)
            else:
                raise ValueError(f"Unknown operator: {token}")

    return stack.pop()

# Example usage:
expr1 = "3 4 +"
expr2 = "5 1 2 + 4 * + 3 -"
expr3 = "2 3 ^"

print(f"{expr1} = {evaluate_postfix(expr1)}")  
print(f"{expr2} = {evaluate_postfix(expr2)}")
print(f"{expr3} = {evaluate_postfix(expr3)}")  



#2
class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = []  
        self.stack2 = [] 

    def enqueue(self, item):
        """Add an element to the queue"""
        self.stack1.append(item)

    def dequeue(self):
        """Remove and return the front element"""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            raise IndexError("Queue is empty")

        return self.stack2.pop()

    def peek(self):
        """Return the front element without removing it"""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def is_empty(self):
        """Check if queue is empty"""
        return not self.stack1 and not self.stack2


# Example usage:
q = QueueUsingTwoStacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())  
print(q.dequeue())  
q.enqueue(40)
print(q.dequeue())  
print(q.peek())     


#3
from collections import deque
import time

class TaskScheduler:
    def __init__(self):
        self.queue = deque()

    def add_task(self, task_name, duration):
        """Add a task with a name and a simulated duration"""
        self.queue.append((task_name, duration))
        print(f"Task added: {task_name} (duration: {duration}s)")

    def run(self):
        """Run tasks in the order they were added"""
        print("\n--- Starting Task Scheduler ---\n")
        while self.queue:
            task_name, duration = self.queue.popleft()
            print(f"Running task: {task_name} ...")
            time.sleep(duration)  
            print(f"Task completed: {task_name}\n")
        print("--- All tasks completed ---")

# Example usage
scheduler = TaskScheduler()
scheduler.add_task("Download File", 1)
scheduler.add_task("Process Data", 2)
scheduler.add_task("Upload Results", 1)

scheduler.run()


#4
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []  
    output = [] 

    for token in expression:
        if token.isalnum():  
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':

            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  
        else:  
            while (stack and stack[-1] != '(' and
                   precedence.get(token, 0) <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return ''.join(output)


# Example usage
expr1 = "A+B*C"
expr2 = "(A+B)*C"
expr3 = "A+B*(C^D-E)^(F+G*H)-I"

print(f"Infix: {expr1}  -->  Postfix: {infix_to_postfix(expr1)}")
print(f"Infix: {expr2}  -->  Postfix: {infix_to_postfix(expr2)}")
print(f"Infix: {expr3}  -->  Postfix: {infix_to_postfix(expr3)}")

