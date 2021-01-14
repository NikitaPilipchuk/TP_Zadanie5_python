import re


def read_cow(path):
    with open(path) as f:
        return re.findall(r'\b[mMoO]{3}\b', f.read())


def get_blocks(source):
    stack = []
    blocks = {}
    for i, op in enumerate(source):
        if op == "MOO":
            stack.append(i)
        if op == "moo":
            blocks[i] = stack[-1]
            blocks[stack.pop()] = i
            
    return blocks 


def eval_cow(source):
    buffer = [0 for _ in range(200)]
    ptr = 0
    i = 0
    blocks = get_blocks(source)
    while i < len(source):
        while i < len(source):
            op = source[i]
            if op == "moO": ptr += 1
            if op == "mOo": ptr -= 1
            if op == "MoO": buffer[ptr] = buffer[ptr] + 1
            if op == "MOo": buffer[ptr] = buffer[ptr] - 1
            if op == "Moo": 
                 if buffer[ptr] > 0: print(chr(buffer[ptr]), end='')
                 else: buffer[ptr] = ord(input())   
            if op == "OOM": print(buffer[ptr], end='')
            if op == "oom": buffer[ptr] = int(input())
            if op == "OOO": buffer[ptr] = 0
            if op == "MOO": 
                 if buffer[ptr] == 0: i = blocks[i]
            if op == "moo": 
                 if buffer[ptr] != 0: i = blocks[i]
                     
            i += 1


if __name__ == "__main__":

    chars = read_cow("hello.cow")
    eval_cow(chars)
