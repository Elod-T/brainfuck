from typing import List

pointer = 0
array: List[int] = [0] * 5000
pointer += 1
array[pointer] += 8

while array[pointer] > 0:
    pointer -= 1 if pointer > 0 else 0
    array[pointer] += 9
    pointer += 1
    array[pointer] -= 1 if array[pointer] > 0 else 0

pointer -= 1 if pointer > 0 else 0
print(chr(array[pointer]), end='')
pointer += 1
array[pointer] += 4

while array[pointer] > 0:
    pointer -= 1 if pointer > 0 else 0
    array[pointer] += 7
    pointer += 1
    array[pointer] -= 1 if array[pointer] > 0 else 0

pointer -= 1 if pointer > 0 else 0
array[pointer] += 1
print(chr(array[pointer]), end='')
array[pointer] += 7
print(chr(array[pointer]), end='')
print(chr(array[pointer]), end='')
array[pointer] += 3
print(chr(array[pointer]), end='')
pointer += 2
array[pointer] += 6

while array[pointer] > 0:
    pointer -= 1 if pointer > 0 else 0
    array[pointer] += 7
    pointer += 1
    array[pointer] -= 1 if array[pointer] > 0 else 0

pointer -= 1 if pointer > 0 else 0
array[pointer] += 2
print(chr(array[pointer]), end='')
array[pointer] -= 12 if array[pointer] > 0 else 0
print(chr(array[pointer]), end='')
pointer += 1
array[pointer] += 6

while array[pointer] > 0:
    pointer -= 1 if pointer > 0 else 0
    array[pointer] += 9
    pointer += 1
    array[pointer] -= 1 if array[pointer] > 0 else 0

pointer -= 1 if pointer > 0 else 0
array[pointer] += 1
print(chr(array[pointer]), end='')
pointer -= 1 if pointer > 0 else 0
print(chr(array[pointer]), end='')
array[pointer] += 3
print(chr(array[pointer]), end='')
array[pointer] -= 6 if array[pointer] > 0 else 0
print(chr(array[pointer]), end='')
array[pointer] -= 8 if array[pointer] > 0 else 0
print(chr(array[pointer]), end='')
pointer += 3
array[pointer] += 4

while array[pointer] > 0:
    pointer -= 1 if pointer > 0 else 0
    array[pointer] += 8
    pointer += 1
    array[pointer] -= 1 if array[pointer] > 0 else 0

pointer -= 1 if pointer > 0 else 0
array[pointer] += 1
print(chr(array[pointer]), end='')
