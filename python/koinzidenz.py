def koinzidenz(msg: str): 
    koinzidenzIndex: float = 0
    alpabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letterCount: dict(int) = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for char in msg.upper():
        if char in alpabet: 
            letterCount[char] += 1
    for letter in letterCount:
        if (letterCount[letter] != 0):
            print("Häufigkeit von " + letter + ": " + str(letterCount[letter]/len(msg)*100) + "%")
        koinzidenzIndex += (letterCount[letter]/len(msg))**2
    return koinzidenzIndex

input = input("Gebe deinen Satz ein:")
print("Kooinzidenz Index: " + str(koinzidenz(input)))