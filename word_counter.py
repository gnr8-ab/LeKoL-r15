def count_characters():
    # Ask the user for a word
    word = input("Ange ett ord: ")
    
    # Count the number of characters
    character_count = len(word)
    
    # Print the result
    print(f"Ordet '{word}' har {character_count} tecken.")

if __name__ == "__main__":
    count_characters() 