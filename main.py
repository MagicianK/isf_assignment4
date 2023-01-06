import numpy as np
# Matrix for encryption
c = [[1, 2, 3],
     [1, 4, 2],
     [4, 2, 1]]

# Russian alphabet
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# List of indexes of Russian alphabet
X = [alphabet.index(x) + 1 for x in 'огород']
print('X initial: ', X)
# Encrypt X using matrix c
Y = [0, 0, 0, 0, 0, 0]
for i in range(3):
    for j in range(3):
        Y[i] += c[i][j] * X[j]

newX = []
for i in range(3, 6):
    newX.append(X[i])
    
for i in range(3):
    for j in range(3):
        Y[i+3] += c[i][j] * newX[j]
        
inverse_c = np.linalg.inv(c)
print('Inverse c: ', inverse_c)
encrypted_X = [0,0,0,0,0,0]
for i in range(3):
    for j in range(3):
        encrypted_X[i] += inverse_c[i][j] * Y[j]

newY = []
for i in range(3, 6):
    newY.append(Y[i])
    
for i in range(3):
    for j in range(3):
        encrypted_X[i+3] += inverse_c[i][j] * newY[j]
# Print encrypted list Y
print(f'Y: {Y}')
print(f'X_decrypted: {X}')
