def encrypt(sequence: bytes, shift: int) -> bytes:
    new_seq = [(x + shift) % 256 for x in sequence]
    return bytes(new_seq)


def decrypt(sequence: bytes, shift: int) -> bytes:
    return encrypt(sequence, -shift)


def encrypt_file(filename, shift):
    with open(filename, 'rb') as f:
        seq = f.read()

    seq = encrypt(seq, shift)

    with open(filename, 'wb') as f:
        f.write(seq)


def decrypt_file(filename, shift):
    encrypt_file(filename, -shift)


decrypt_file('2.txt', 100)