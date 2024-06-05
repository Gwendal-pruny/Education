# Définition de la classe Rotor
class Rotor:
    # Initialisation du rotor avec son câblage, sa position de coche et sa position actuelle
    def __init__(self, wiring, notch, position=0):
        self.wiring = wiring  # Câblage interne du rotor
        self.notch = notch  # Position de la coche où le rotor suivant doit tourner
        self.position = position  # Position actuelle du rotor
        self.ring_setting = 0  # Réglage de l'anneau (par défaut à 0)
    
    # Méthode pour encoder un caractère en passant par le rotor dans le sens normal
    def encode_forward(self, c):
        # Calcul de l'index après ajustement de la position et du réglage de l'anneau
        index = (ord(c) - ord('A') + self.position - self.ring_setting) % 26
        # Encodage du caractère selon le câblage du rotor
        encoded_c = self.wiring[index]
        # Retour du caractère encodé après ajustement inverse
        return chr((ord(encoded_c) - ord('A') - self.position + self.ring_setting) % 26 + ord('A'))
    
    # Méthode pour encoder un caractère en passant par le rotor dans le sens inverse
    def encode_backward(self, c):
        # Calcul de l'index après ajustement de la position et du réglage de l'anneau
        index = (ord(c) - ord('A') + self.position - self.ring_setting) % 26
        # Recherche de la position du caractère dans le câblage du rotor
        encoded_c = chr((self.wiring.index(chr(index + ord('A'))) - self.position + self.ring_setting) % 26 + ord('A'))
        return encoded_c
    
    # Méthode pour faire avancer le rotor d'une position
    def step(self):
        self.position = (self.position + 1) % 26  # Incrément de la position
        return self.position == self.notch  # Retourne True si la position atteint la coche

# Définition de la classe Reflector
class Reflector:
    # Initialisation du réflecteur avec son câblage
    def __init__(self, wiring):
        self.wiring = wiring  # Câblage du réflecteur
    
    # Méthode pour réfléchir un caractère
    def reflect(self, c):
        index = ord(c) - ord('A')  # Calcul de l'index du caractère
        return self.wiring[index]  # Retourne le caractère réfléchi selon le câblage

# Définition de la classe Plugboard
class Plugboard:
    # Initialisation du plugboard avec les paires de câblage
    def __init__(self, wiring):
        self.wiring = {k: v for k, v in zip(wiring[::2], wiring[1::2])}  # Création d'un dictionnaire des connexions
        self.wiring.update({v: k for k, v in self.wiring.items()})  # Ajout des connexions inverses
    
    # Méthode pour échanger un caractère selon le câblage du plugboard
    def swap(self, c):
        return self.wiring.get(c, c)  # Retourne le caractère échangé ou le caractère original s'il n'est pas câblé

# Définition de la classe EnigmaMachine
class EnigmaMachine:
    # Initialisation de la machine Enigma avec ses rotors, son réflecteur et son plugboard
    def __init__(self, rotors, reflector, plugboard):
        self.rotors = rotors  # Liste des rotors
        self.reflector = reflector  # Réflecteur
        self.plugboard = plugboard  # Plugboard
    
    # Méthode pour avancer les rotors correctement
    def step_rotors(self):
        rotate_next = self.rotors[0].step()  # Faire avancer le premier rotor
        if rotate_next:  # Si le premier rotor atteint sa coche
            rotate_next = self.rotors[1].step()  # Faire avancer le deuxième rotor
            if rotate_next:  # Si le deuxième rotor atteint sa coche
                self.rotors[2].step()  # Faire avancer le troisième rotor
    
    # Méthode pour encoder un texte
    def encode(self, text):
        encoded_text = []  # Liste pour stocker le texte encodé
        for char in text:
            if char.isalpha():  # Vérifier si le caractère est une lettre
                self.step_rotors()  # Faire avancer les rotors
                char = self.plugboard.swap(char)  # Échanger le caractère selon le plugboard
                for rotor in self.rotors:  # Passer le caractère à travers les rotors dans le sens normal
                    char = rotor.encode_forward(char)
                char = self.reflector.reflect(char)  # Réfléchir le caractère
                for rotor in reversed(self.rotors):  # Passer le caractère à travers les rotors dans le sens inverse
                    char = rotor.encode_backward(char)
                char = self.plugboard.swap(char)  # Échanger de nouveau le caractère selon le plugboard
            encoded_text.append(char)  # Ajouter le caractère encodé à la liste
        return ''.join(encoded_text)  # Retourner le texte encodé sous forme de chaîne

# Configuration des rotors et du réflecteur pour la machine Enigma C
rotor_I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 16)  # Rotor I avec son câblage et sa coche
rotor_II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", 4)  # Rotor II avec son câblage et sa coche
rotor_III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", 21)  # Rotor III avec son câblage et sa coche
reflector_B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")  # Réflecteur B avec son câblage
plugboard = Plugboard("AMBOCNDPEQFGRHISJKTULWVZYX")  # Plugboard avec son câblage (exemple)

# Création de la machine Enigma avec les rotors, le réflecteur et le plugboard
enigma = EnigmaMachine([rotor_I, rotor_II, rotor_III], reflector_B, plugboard)

# Encodage d'un message
message = "HELLOENIGMA"  # Message à encoder
encoded_message = enigma.encode(message)  # Encodage du message
print(f"Message encodé : {encoded_message}")  # Affichage du message encodé
