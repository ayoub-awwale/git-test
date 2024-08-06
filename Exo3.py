import string

def nettoyer_chaine(input_string):
    """Nettoie la chaîne en supprimant les caractères non alphanumériques et en convertissant en minuscules."""
    return ''.join(char.lower() for char in input_string if char.isalnum())

def is_palindrome_while(input_string):
    """Vérifie si une chaîne est un palindrome en utilisant une boucle while."""
    cleaned_string = nettoyer_chaine(input_string)
    left, right = 0, len(cleaned_string) - 1
    
    while left < right:
        if cleaned_string[left] != cleaned_string[right]:
            return False
        left += 1
        right -= 1
    
    return True

def is_palindrome_for(input_string):
    """Vérifie si une chaîne est un palindrome en utilisant une boucle for."""
    cleaned_string = nettoyer_chaine(input_string)
    length = len(cleaned_string)
    
    for i in range(length // 2):
        if cleaned_string[i] != cleaned_string[length - 1 - i]:
            return False
    
    return True

# Test des fonctions avec des exemples d'entrées
test_phrases = [
    "A man, a plan, a canal, Panama",
    "No 'x' in Nixon",
    "racecar",
    "hello",
    "Madam, in Eden, I'm Adam"
]

for phrase in test_phrases:
    print(f"Phrase: {phrase}")
    print(f"Palindrome (while loop) : {is_palindrome_while(phrase)}")
    print(f"Palindrome (for loop) : {is_palindrome_for(phrase)}")