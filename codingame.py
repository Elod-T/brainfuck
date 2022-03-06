# solution to the brainfuck puzzle on codingame.com
# https://www.codingame.com/training/medium/what-the-brainfuck

lines, s, inputcount = map(int,input().split())
array = [0] * s
codepointer = 0
arraypointer = 0

dirtycode = ""
for i in range(lines):
    line = input()
    dirtycode += line

inputs = []
for i in range(inputcount):
    inp = int(input())
    inputs.append(inp)

code = ""
for c in dirtycode:
    if c in list("+-><.,[]"):
        code += c

if code.count("[") != code.count("]"): print("SYNTAX ERROR"); exit()

stack = []
jump = [None] * len(code)
for i,c in enumerate(code):
    if c == "[":
        stack.append(i)
    elif c == "]":
        jump[i] = stack.pop()
        jump[jump[i]] = i


while codepointer < len(code):
    command = code[codepointer]
    if command == ">":
        arraypointer += 1
        if arraypointer >= s:
            print("POINTER OUT OF BOUNDS"); exit()
    elif command == "<":
        arraypointer -= 1
        if arraypointer < 0:
            print("POINTER OUT OF BOUNDS"); exit()
    elif command == "+":
        array[arraypointer] += 1
        if array[arraypointer] > 255:
            print("INCORRECT VALUE"); exit()
    elif command == "-":
        array[arraypointer] -= 1
        if array[arraypointer] < 0:
            print("INCORRECT VALUE"); exit()
    elif command == ".":
        print(chr(array[arraypointer]),end="")
    elif command == ",":
        array[arraypointer] = inputs.pop(0)
    elif command == "[" and not array[arraypointer]:
        codepointer = jump[codepointer]
    elif command == "]" and array[arraypointer]:
        codepointer = jump[codepointer]
    codepointer += 1
