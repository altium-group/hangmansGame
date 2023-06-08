# Import
import random

# Var

words = [
    "chat", "chien", "maison", "ordinateur", "livre", "jardin", "voiture", "musique", "soleil", "plage", "montagne", "arbre", "café", "vélo", "football", "école", "pizza", "voyage", "famille", "amour"
]

word = random.choice(words)
wordDisplay = ["_"] * len(word)

while True:
    print(" ".join(wordDisplay))
    letter = input("Donne UNE lettre>")
    if len(letter) > 1:
        print("Vous avez mis plus d'une lettre")
    else:
        place = -1
        for i in word:
            place += 1
            if i == letter:
                wordDisplay[place] = letter
    if "_" not in wordDisplay:
        print(f"Vous avez trouvé ! Le mot était : {word}")
        break