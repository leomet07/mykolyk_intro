print("CW25 By Lenny Metlitsky PD9 3/27/2023")

def alphabetical_order(a : str, b : str, c: str):
    arr =  [a.lower(), b.lower(), c.lower()]
    arr.sort()
    return arr

print(alphabetical_order(input("Enter the first word: "), input("Enter the second word: "), input("Enter the third word: ")))

print("Challenge Problem:")

def split_words_and_sort(sentence : str):
    words = sentence.split(" ")
    words = [word.lower() for word in words]
    words.sort()
    return " ".join(words)

print('"the quick brown fox" in alphabetical order: ', split_words_and_sort("the quick brown fox"))