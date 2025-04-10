from stats import count_words, count_chars, sort_chars
import sys

def get_book_text(path):
    contents = None
    with open(path) as f:
        contents = f.read()
    return contents

# gives a well-structured report to the user on the given book: Word Count, & Character Count greatest to least.
def report():
    pass

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    input_path = sys.argv[1]
    book_text = get_book_text(input_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {input_path}")
    print("----------- Word Count ----------")

    word_count = count_words(book_text)
    print(f"Found {word_count} total words")
    
    print("--------- Character Count -------")

    char_counts_list = sort_chars(count_chars(book_text))
    for e in char_counts_list:
        if e["character"].isalpha():
            print(f"{e["character"]}: {e["count"]}")
    
    print("============= END ===============")



main()