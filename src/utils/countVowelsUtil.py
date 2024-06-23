# Função para contar vogais em uma palavra
def count_vowels(word):
    vowels = "aeiou"
    return sum(1 for char in word.lower() if char in vowels)