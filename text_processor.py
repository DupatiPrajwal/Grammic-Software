def count_characters(text):
    character_count = len(text)
    return character_count

def count_words(text):
    word_count = text.split()
    count = len(word_count)
    return count

def count_sentences(text):
    count = 0
    for i in text:
        if i == "?" or i == "!" or i == ".":
            count += 1
    return count

def count_paragraphs(text):
    paragraphs = text.split("\n\n")
    paragraphs_count = len(paragraphs)
    return paragraphs_count

def count_lines(text):
    lines = text.split("\n")
    count = len(lines)
    return count

def count_unique_words(text):
    word_count = text.split()
    word_count = set(word_count)
    word_count = len(word_count)
    return word_count


