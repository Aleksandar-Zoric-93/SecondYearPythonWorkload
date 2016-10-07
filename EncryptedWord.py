from Tools.Scripts.treesync import raw_input

__author__ = 'Aleksandar'
# T00166011

ord_of_a = 97
encryp_value = 5
encrypted_word = ""
decrypted_word = ""
SIZE_OF_ALPHABET = 26

word = raw_input("Please enter a word you wish to use: ")

print("Encrypting word...")

for letter in word:
    ord_value = ord(letter)
    position = ord_value - ord('a')
    encrypt_position = (position + encryp_value)
    adjusted_position = encrypt_position % SIZE_OF_ALPHABET
    ascii_position = adjusted_position + ord_of_a
    encrypted_letter = chr(ascii_position)
    encrypted_word += encrypted_letter

print("Encrypted Word: ", encrypted_word)

print()

print("Decrypting Word...")

for letter in encrypted_word:
    ord_value = ord(letter)
    position = ord_value - ord('a')
    encrypt_position = (position - encryp_value)
    adjusted_position = encrypt_position % SIZE_OF_ALPHABET
    ascii_position = adjusted_position + ord_of_a
    encrypted_letter = chr(ascii_position)
    decrypted_word += encrypted_letter

print("Decrypted Word: ", decrypted_word[:-1])



