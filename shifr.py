'''Encode and decode string functions by Caesar cipher
'''

def encode(instr, inkey):
    '''Encode input string with input key by Caesar cipher
    instr : str
    inkey : int >= 0
    '''
    num_of_letters = 1 + ord('Z') - ord('A')
    key = inkey % num_of_letters
    outlist = []
    for char in instr:
        if ord('A') <= ord(char) <= ord('Z'):
            if ord(char) + key > ord('Z'):
                outlist.append(chr(ord(char) + key - num_of_letters))
            else:
                outlist.append(chr(ord(char) + key))
        elif ord('a') <= ord(char) <= ord('z'):
            if ord(char) + key > ord('z'):
                outlist.append(chr(ord(char) + key - num_of_letters))
            else:
                outlist.append(chr(ord(char) + key))
        else:
            outlist.append(char)
    return ''.join(outlist)

def decode(instr, inkey):
    '''Decode input string with input key by Caesar cipher
    instr : str
    inkey : int >= 0
    '''
    num_of_letters = 1 + ord('Z') - ord('A')
    key = inkey % num_of_letters
    outlist = []
    for char in instr:
        if ord('A') <= ord(char) <= ord('Z'):
            if ord(char) - key < ord('A'):
                outlist.append(chr(ord(char) - key + num_of_letters))
            else:
                outlist.append(chr(ord(char) - key))
        elif ord('a') <= ord(char) <= ord('z'):
            if ord(char) - key < ord('a'):
                outlist.append(chr(ord(char) - key + num_of_letters))
            else:
                outlist.append(chr(ord(char) - key))
        else:
            outlist.append(char)
    return ''.join(outlist)

if __name__ == '__main__':
    for inp in (('Ivan Antonov!&*', 30),
                ('Svjatoslav Alexeev', 100),
                ('Ekaterinburg', 1),):

        s = inp[0]
        k = inp[1]

        e = encode(s, k)
        d = decode(e, k)

        print(f'Input: {s}')
        print(f'Key: {k}')
        print(f'Encoded: {e}')
        print(f'Decoded: {d}')
        assert s == d
        print()
