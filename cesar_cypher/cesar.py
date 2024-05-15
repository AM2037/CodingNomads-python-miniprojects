''' Note: Wrote the majority of this myself but used Windows Copilot to help me
debug some minor issues i.e. an incorrect variable reference, etc.'''
# Try looping, conditional statements, string methods, and indexing
# Preserve capitalization of the original text

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7

def encrypt(secret, char, cipher):
    # Initialize empty result string
    message = ""

    for letter in secret:
        if letter.lower() in char:
            # Find index of the letter in lowercase_letters
            index = lowercase_letters.index(letter.lower())
            # Calculate shifted index
            shifted_index = (index + cipher) % 26
            # Preserve capitalization
            if letter.isupper():
                message += lowercase_letters[shifted_index].upper()
            else:
                message += lowercase_letters[shifted_index]
        else:
            # Leave unchanged if not a letter
            message += letter

    return message

result = encrypt(secret, lowercase_letters, cipher)
print("Encrypted message: " + result)

# Decrypt back to original secret
def decrypt(encrypted_message, char, cipher):
    # Initialize an empty result string
    result = ""

    for letter in encrypted_message:
        if letter.lower() in char:
            # Find index of the letter in lowercase_letters
            index = lowercase_letters.index(letter.lower())
            # Calculate shifted index in reverse
            shifted_index = (index - cipher) % 26
            # Preserve capitalization
            if letter.isupper():
                result += lowercase_letters[shifted_index].upper()
            else:
                result += lowercase_letters[shifted_index]
        else:
            # Leave unchanged if not a letter
            result += letter

    return result

decrypted_message = decrypt(result, lowercase_letters, cipher)
print("Decrypted message: " + decrypted_message)