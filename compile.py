code = input("Enter a Brainfuck script: ")
tape = [0] * 30000
ptr = 0
pc = 0
bracket_map = {}
stack = []

# Build a map of matching brackets for quick jump
for i, cmd in enumerate(code):
    if cmd == "[":
        stack.append(i)
    elif cmd == "]":
        start = stack.pop()
        bracket_map[start] = i
        bracket_map[i] = start

# Run the brainfuck code
while pc < len(code):
    cmd = code[pc]
    
    if cmd == ">":
        ptr += 1
    elif cmd == "<":
        ptr -= 1
    elif cmd == "+":
        tape[ptr] = (tape[ptr] + 1) % 256
    elif cmd == "-":
        tape[ptr] = (tape[ptr] - 1) % 256
    elif cmd == ".":
        print(chr(tape[ptr]), end="")
    elif cmd == ",":
        tape[ptr] = ord(input("Input a character: ")[0])
    elif cmd == "[":
        if tape[ptr] == 0:
            pc = bracket_map[pc]
    elif cmd == "]":
        if tape[ptr] != 0:
            pc = bracket_map[pc]
    
    pc += 1

for i in range(0, 5):
    print(tape[i])
