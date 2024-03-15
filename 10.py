def count_word_frequency(file_name):
    word_freq = {}
    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                word = word.strip('.,!?;:"')
                if word:
                    if word in word_freq:
                        word_freq[word] += 1
                    else:
                        word_freq[word] = 1

    return word_freq

def main():
    file_name = input("Enter the file name: ")
    word_freq = count_word_frequency(file_name)
    print("\nWord Frequency:")
    for word, freq in sorted(word_freq.items()):
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()