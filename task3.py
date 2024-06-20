import numpy as np

message = 'tishenko is a bad guy'
print(f"original message: {message}")

def encrypt_message(message, key_matrix):
    message_vector = np.array([ord(char) for char in message])
    print(f'message_vector {message_vector}')
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diagonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))
    encrypted_vector = np.dot(diagonalized_key_matrix, message_vector)
    print(f'encrypted message{encrypted_vector}')
    return encrypted_vector

def decrypt_message(encrypted_vector, key_matrix):
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diagonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(1/eigenvalues)), np.linalg.inv(eigenvectors))
    decrypted_vector = np.dot(diagonalized_key_matrix, encrypted_vector)
    print(np.round(decrypted_vector).astype(int))
    return decrypted_vector




key_matrix = np.random.randint(0, 256, (len(message), len(message)))
#print(key_matrix)

encrypted_vector = encrypt_message(message, key_matrix)
decrypted_vector = decrypt_message(encrypted_vector, key_matrix)

decrypted_message = ''.join([chr(num) for num in np.round(decrypted_vector).astype(int)])
print(f'decrypted message: {decrypted_message}')
