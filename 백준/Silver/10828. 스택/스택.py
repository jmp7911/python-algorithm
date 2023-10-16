#push X: 정수 X를 스택에 넣는 연산이다.
#pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#size: 스택에 들어있는 정수의 개수를 출력한다.#
#empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
#top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import sys


class Stack:
    def __init__(self):
        self.stack = []
    def push(self, X):
        self.stack.append(X)
    def size(self):
        return len(self.stack)
    def empty(self):
        if len(self.stack) > 0:
            return 0
        else:
            return 1
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return -1
    def pop(self):
      if len(self.stack) > 0:
          n = self.stack[-1]
          del self.stack[-1]
          return n
      else:
          return -1
      

    
stack = Stack()

N = int(input())
for _ in range(N):
    op = sys.stdin.readline().rstrip().split()
    if op[0]=='push':
      stack.push(op[1])
    elif op[0]=='size':
      print(stack.size())
    elif op[0]=='empty':
      print(stack.empty())
    elif op[0]=='top':
      print(stack.top())
    elif op[0]=='pop':
      print(stack.pop())