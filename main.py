def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(book_path)
    character_counts = get_character_counts(book_path)
    character_count_list = convert_character_counts_to_list(character_counts)
    character_analysis = analyse_character_list(character_count_list)
    report = (
        f"""--- Begin report of {book_path} ---\n"""+
        f"""{word_count} words found in the document \n"""+
        character_analysis +
        "--- End report ---"
        )
    
    print (report)
    


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(path):
    with open(path) as f:
        text = f.read()
        words = text.split()
        return len(words)

def get_character_counts(path):
    with open(path) as f:
        text = f.read()
        character_counts = {}
        for character in text:
            lowered_character = character.lower()
            if lowered_character in character_counts:
                character_counts[lowered_character] += 1
            else:
                character_counts[lowered_character] = 1
        return character_counts

def convert_character_counts_to_list(dictionary):
    char_list = []
    for char, count in dictionary.items():
        if char.isalpha():
            char_list.append({"character": char, "count": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on (dictionary):
    return dictionary["count"]

def analyse_character_list(list):
    analysis = f""
    for dict in list:
        chara_name = dict["character"]
        chara_count = dict["count"]
        character_analyzed = f"The '{chara_name}' character was found '{chara_count}' times"
        analysis = analysis + character_analyzed + "\n"
    return analysis
    




main()