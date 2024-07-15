def count_words(text):
    words = text.strip().split()
    return len(words)

def main():
    user_input = input("Please enter a sentence or paragraph: ").strip()
    
    if not user_input:
        print("Error: You entered an empty input. Please enter some text.")
    else:
        word_count = count_words(user_input)
        print(f"The number of words in the given text is: {word_count}")

if __name__ == "__main__":
    main()
