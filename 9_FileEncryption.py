encryption = {
    'A': '@', 'B': '#', 'C': '$', 'D': '%', 'E': '&', 'F': '*', 'G': '(', 'H': ')',
    'I': '1', 'J': '2', 'K': '3', 'L': '4', 'M': '5', 'N': '6', 'O': '7', 'P': '8',
    'Q': '9', 'R': '0', 'S': '!', 'T': '^', 'U': '-', 'V': '_', 'W': '+', 'X': '=',
    'Y': '{', 'Z': '}', 'a': '|', 'b': '[', 'c': ']', 'd': ':', 'e': ';', 'f': '<',
    'g': '>', 'h': '.', 'i': ',', 'j': '?', 'k': '/', 'l': '~', 'm': '`', 'n': '"',
    'o': '?!', 'p': '::', 'q': '@#', 'r': '<>', 's': '><', 't': ':;', 'u': '+=', 'v': '*&',
    'w': '%^', 'x': '!)', 'y': '_=', 'z': '^*',
}

infile = open('info_security.txt', 'r')
outfile = open('encrypted.txt', 'w')


text_to_encrypt = infile.read()

for char in text_to_encrypt:
    encrypted_char = encryption.get(char, char)
    outfile.write(encrypted_char)

infile.close()
outfile.close()
