charMap = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
alphaBet = ["A", "B", "C", "D", "E", "F", "G"]


def encrypt(key, plaintext):
    ciphertext = ""
    for char in plaintext:
        char_index = (charMap[char] + key % 26) % 26
        ciphertext += alphaBet[char_index]
    return ciphertext


def decrypt(key, ciphertext):
    plaintext = ""
    for char in ciphertext:
        char_index = (charMap[char] - key % 26) % 26
        ciphertext += alphaBet[char_index]
    return plaintext
