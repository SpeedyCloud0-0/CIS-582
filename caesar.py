# charMap = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
alphaBet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def encrypt(key, plaintext):
    ciphertext = ""
    for char in plaintext:
        char_index = (ord(char) - ord('A') + 26 - key%26) % 26
        ciphertext += alphaBet[char_index]
    return ciphertext


def decrypt(key, ciphertext):
    plaintext = ""
    for char in ciphertext:
        char_index = (ord(char) - ord('A') + key) % 26
        ciphertext += alphaBet[char_index]
    return plaintext
