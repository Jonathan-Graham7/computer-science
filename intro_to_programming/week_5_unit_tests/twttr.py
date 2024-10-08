def main():
    tweet = input("Input: ")
    tweet = shorten(tweet)
    print("Output:", tweet)

def shorten(word):
    vowels = ["A","E","I","O","U","a","e","i","o","u"]
    for letter in vowels:
        word = word.replace(letter, "")
    return word

if __name__ == "__main__":
    main()