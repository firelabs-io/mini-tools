import sys

filename = sys.argv[1]
program = []

with open(filename, 'rb') as file:
    while (byte := file.read(1)):
        # Convert each byte to its 8-bit binary representation
        binary_byte = f"{ord(byte):08b}"
        program.append(binary_byte)

# Print the resulting binary program
with open("test", 'w') as Ofile:
    for binary in program:
        Ofile.write(str(binary) + ' ')
