# Importation de la bibliothèque Numpy
import numpy as np

# Opération de Permutation
def permutation_operation(data):
    return data[::-1] 

# Opération de compression des valeurs ascii en héxadécimal
def compression_hex_operation(data):
    somme = 0
    for i in data:
        somme += i
    hex_unicode = hex(somme)

    return hex_unicode

# Liste des valeurs ascii de chaque caractère
def ascii_list_operation(data):
    char_list = []
    for char in data:
        unicode_char = ord(char)
        char_list.append(unicode_char)

    return char_list

# Opération de compression de la liste des ascii
def ascii_compression(data):
    ascii_list = ascii_list_operation(data)
    total = 0
    for i in ascii_list:
        total -= i
        total *= -1
    return total

# Opération de Rotation
def rotation_operation(data):
    decalage = int(len(data)/2)
    return data[decalage:] + data[:decalage]

# Fonction de hashage
def hash_function(data):
    unicode = ascii_compression(data)
    ascii_list = ascii_list_operation(data)
    hex_comp = compression_hex_operation(ascii_list)
    substituted_value = ''
    positive = 'a01bc'
    negative = 'ef5d9'
    alphabet = 'abcdef02134ghijklmno56789pqrstuvwxyz'
    
    if(unicode > 0):
       substituted_value += positive
       substituted_value += str(unicode)
       substituted_value += str(hex_comp)
       
    elif(unicode < 0):
        substituted_value += negative
        substituted_value += str(unicode)
        substituted_value += str(hex_comp)
    else:
        substituted_value += positive
        substituted_value += negative
        substituted_value += str(hex_comp)
    
    data_len = len(substituted_value)
    # Valeur de hachage de longueur 20
    reste = 20 - data_len
    np.random.seed(101)
    index_elmnts = np.random.randint(0,len(alphabet),reste)
    for i in index_elmnts:
        substituted_value += alphabet[i]
        
    hash_value = permutation_operation(substituted_value)
    hash_value = rotation_operation(hash_value)
    
    return hash_value



# Exemple d'utilisation 
data = input("Entrez la valeur d'entrée : ")
hash_value = hash_function(data)
print(f"La valeur de hachage est : {hash_value}")