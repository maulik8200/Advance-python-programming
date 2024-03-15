def find_longest_words(words):
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words

def main():
    words = input("Enter a list of words separated by spaces: ").split()
    longest_words = find_longest_words(words)
    
    if longest_words:
        if len(longest_words) == 1:
            print("The longest word is:", longest_words[0])
        else:
            print("The longest words are:", ', '.join(longest_words))
    else:
        print("No words entered!")

if __name__ == "__main__":
    main()
