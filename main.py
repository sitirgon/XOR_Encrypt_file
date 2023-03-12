from sys import argv, path
import random


def from_bits_to_bytes(count_binary, file):
    barray = []
    byte = 8
    for l in range(0, int(count_binary / 8)):
        barray.append(int(file[byte - 8:byte], 2))
        byte += 8
    return barray

def random_key(lenght):
    key = ""
    for i in range(0, lenght):
        key += str(random.randint(0,1))
    return key

def xor(key, xor):
    if key == xor:
        return 0
    else:
        return 1

def checkArgv(first):
    if first == '-e' or first == '-d':
        for index in range(1, len(argv)):
            if argv[index] == '-k':
                key_path = path[0] + '\\' + argv[index + 1]
            if argv[index] == '-op':
                orginal_path = argv[index + 1]
            if argv[index] == '-ep':
                encode_path = argv[index + 1]
        return orginal_path, key_path, encode_path
    if first == '-help':
        print('''Requirement arguments (-e or -d, -k, -op, -ep)
        -e      Encode mode
        -d      Decode mode
        -k      Key name (in the same folder where script)
        -op     Orginal path file before coding (include name file)
        -ep     Encoded path file after coding (include name file)''')

binary_content = ""
newFile = ""
if argv[1] == '-e':
    orginal_path, key_path, encode_path =  checkArgv(argv[1])
    with open(orginal_path, 'rb') as fd:
        container = fd.read()
        count = len(container)
        for i in range(0, count):
            binary_content += bin(container[i])[2:].zfill(8)
        count_binary = len(binary_content)
        key = random_key(count_binary)
        with open(key_path, 'wb') as key_file:
            key_file.write(bytearray(from_bits_to_bytes(count_binary, key)))
        for k in range(0, count_binary):
            newFile += str(xor(key[k], binary_content[k]))
        with open(encode_path, 'wb') as fd_save:
            fd_save.write(bytearray(from_bits_to_bytes(count_binary, newFile)))
if argv[1] == '-d':
    pass

if argv[1] == '-help':
    checkArgv(argv[1])


