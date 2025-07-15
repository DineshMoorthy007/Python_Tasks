def count_words_in_file(filename):
    word_count = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.lower().split()
                for word in words:
                    word = ''.join(char for char in word if char.isalnum())
                    if word:
                        word_count[word] = word_count.get(word, 0) + 1

        for word in sorted(word_count):
            print(f"{word}: {word_count[word]}")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", e)

filename = input("Enter the filename (with path if needed): ")
count_words_in_file(filename)