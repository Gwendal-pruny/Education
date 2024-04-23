import functools
import random

# Cache la fonction b64 pour qu'elle ne soit calculée qu'une seule fois
@functools.lru_cache()
def b64():
    # Retourne la chaîne des caractères utilisés en Base64
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def shuffle_b64(base, seed):
    # Initialise le générateur de nombres aléatoires
    random.seed(seed)
    # Transforme la chaîne en liste pour pouvoir la mélanger
    lst = list(base)
    # Mélange la liste aléatoirement
    random.shuffle(lst)
    # Convertit la liste en chaîne et la retourne
    return ''.join(lst)

def increment_b64(base, shift):
    # Effectue une rotation des caractères de la base selon le décalage spécifié
    return base[-shift:] + base[:-shift]

def fixed_shift_b64(base, shift):
    # Effectue une rotation fixe des caractères de la base
    return base[-shift:] + base[:-shift]

def encode(s_to_encode, base):
    # Convertit chaque caractère en chaîne en représentation binaire de 8 bits
    binary = ''.join(format(char, '0>8b') for char in s_to_encode.encode())
    # Ajoute des zéros à la fin pour compléter les groupes de 6 bits
    padded_binary = binary + '0' * ((6 - len(binary) % 6) % 6)
    # Découpe la chaîne binaire en segments de 6 bits et convertit en entiers
    indices = [int(padded_binary[i:i+6], 2) for i in range(0, len(padded_binary), 6)]
    # Convertit les indices en caractères selon la base fournie
    return ''.join(base[index] for index in indices) + '=' * ((4 - len(s_to_encode) % 3) % 4)

def decode(s_to_decode, base):
    # Crée un dictionnaire pour retrouver l'index de chaque caractère dans la base
    base_dict = {char: i for i, char in enumerate(base)}
    # Enlève les éventuels caractères '=' à la fin
    encoded = s_to_decode.rstrip('=')
    # Convertit la chaîne encodée en une chaîne de bits
    binary = ''.join(format(base_dict[char], '06b') for char in encoded)
    # Assure que la longueur de la chaîne binaire soit multiple de 8
    byte_length = len(binary) - len(binary) % 8
    # Convertit les segments de 8 bits en bytes et les décode en chaîne
    return bytes(int(binary[i:i+8], 2) for i in range(0, byte_length, 8)).decode('utf-8', errors='ignore')

def main():
    print('Encodeur/décodeur Base64')
    base = b64()  # Charge la base64 initiale
    seed = random.randint(0, 1000)  # Génère une graine aléatoire pour le mélange
    shift = 1  # Définit le décalage initial pour les rotations

    while True:
        print("\nBase actuelle:", base)
        print("1. Mélanger la base\n2. Incrémenter la base\n3. Décalage fixe\n4. Quitter")
        choice = input("Choisissez le mode d'encodage ou quittez: ")
        
        if choice == '4':
            print('Fin du programme!')
            break
        
        if choice not in ('1', '2', '3'):
            print('Choix invalide!')
            continue

        if choice == '1':
            base = shuffle_b64(base, seed)
        elif choice == '2':
            base = increment_b64(base, shift)
        elif choice == '3':
            base = fixed_shift_b64(base, shift)
        
        print("Base modifiée pour l'itération:", base)

        while True:
            action = input("Tapez (E)ncode, (D)ecode, ou (X) pour changer de mode: ").upper()
            if action == 'X':
                break
            user_input = input("Entrez votre chaîne: ")
            if action == 'E':
                print('Chaîne encodée:', encode(user_input, base))
            elif action == 'D':
                try:
                    print('Chaîne décodée:', decode(user_input, base))
                except Exception as e:
                    print("Erreur de décodage:", str(e))

if __name__ == '__main__':
    main()
