# just for fun, no usage for this

from argparse import ArgumentParser
from os import remove, path, getcwd
from itertools import groupby

parser = ArgumentParser()
parser.add_argument("-f", "--file", help="your .bf file that you want to interpret")
args = parser.parse_args()


def main():
    filename = ""
    if args.file.count("."):
        filename, extension = args.file.split(".")
        if extension != "bf":
            print(f"{args.file} is not a Brainfuck file! Please select a Brainfuck(.bf) file!")
            exit()
    else:
        print(f"{args.file} is not a Brainfuck file! Please select a Brainfuck(.bf) file!")
        exit()

    with open(args.file, "r") as file:
        contents = file.read()

    code = ""
    for c in contents:
        if c in "+-><.,[]":
            code += c
    code = ["".join(map(str, list(j))) for i, j in groupby(code)]

    remove(f"{getcwd()}/brainfuck.py") if path.exists(f"{getcwd()}/brainfuck.py") else None
    with open(f"{filename}.py", "a") as file:
        file.write("from typing import List\n\n"
                   "pointer = 0\n"
                   "array: List[int] = [0] * 5000\n")

        indent = 0
        for command in code:
            if indent and command != "]":
                file.write("    "*indent)
            if command[0] == ">":
                file.write(f"pointer += {len(command)}\n")
            elif command[0] == "<":
                file.write(f"pointer -= {len(command)} if pointer > 0 else 0\n")
            elif command[0] == "+":
                file.write(f"array[pointer] += {len(command)}\n")
            elif command[0] == "-":
                file.write(f"array[pointer] -= {len(command)} if array[pointer] > 0 else 0\n")
            elif command[0] == ".":
                file.write(f"print(chr(array[pointer]), end='')\n"*len(command))
            elif command[0] == ",":
                file.write(f"array[pointer] = int(input())\n"*len(command))
            elif command[0] == "[":
                file.write(f"\nwhile array[pointer] > 0:\n")
                indent += 1
            elif command[0] == "]":
                file.write("\n")
                indent -= 1


if __name__ == "__main__":
    main()

