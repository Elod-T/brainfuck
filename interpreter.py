# a basic brainfuck interpreter

import argparse
from typing import List

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="your .bf file that you want to interpret")
args = parser.parse_args()


def main():
    if args.file.count("."):
        _, extension = args.file.split(".")
        if extension != "bf":
            print(f"{args.file} is not a Brainfuck file! Please select a Brainfuck(.bf) file!")
            exit()
    else:
        print(f"{args.file} is not a Brainfuck file! Please select a Brainfuck(.bf) file!")
        exit()

    array: List[int] = [0]
    codepointer: int = 0
    arraypointer: int = 0

    with open(args.file, "r") as file:
        contents = file.read()

    code = ""
    for c in contents:
        if c in "+-><.,[]":
            code += c

    if code.count("[") != code.count("]"):
        print("SYNTAX ERROR")
        exit()

    stack = []
    jump = [None] * len(code)
    for i, c in enumerate(code):
        if c == "[":
            stack.append(i)
        elif c == "]":
            jump[i] = stack.pop()
            jump[jump[i]] = i

    while codepointer < len(code):
        command = code[codepointer]
        if command == ">":
            arraypointer += 1
            if arraypointer == len(array):
                array.append(0)
        elif command == "<":
            arraypointer -= 1 if arraypointer > 0 else 0
        elif command == "+":
            array[arraypointer] += 1
            if array[arraypointer] > 255:
                print("INCORRECT VALUE")
                exit()
        elif command == "-":
            array[arraypointer] -= 1
            if array[arraypointer] < 0:
                print("INCORRECT VALUE")
                exit()
        elif command == ".":
            print(chr(array[arraypointer]), end="")
        elif command == ",":
            array[arraypointer] = ord(input()[0])
            if array[arraypointer] > 255:
                print("INCORRECT VALUE")
                exit()
        elif command == "[" and not array[arraypointer]:
            codepointer = jump[codepointer]
        elif command == "]" and array[arraypointer]:
            codepointer = jump[codepointer]
        codepointer += 1


if __name__ == "__main__":
    main()
