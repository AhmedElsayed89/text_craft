def split_text_into_batches(text, batch_size):
    words = text.split()
    return [' '.join(words[i:i + batch_size]) for i in range(0, len(words), batch_size)]


def count_occurrences(text, pattern):
    return sum(1 for word in text.split() if word == pattern)


def modify_text(text, pattern, m):
    words = text.split()
    modified_text = []
    pattern_count = 0

    for word in words:
        if word == pattern:
            pattern_count += 1
            if pattern_count <= m:
                modified_text.append(word)
        else:
            modified_text.append(word)

    return ' '.join(modified_text)


class TextCraft:
    pass


# Example with fixed inputs:
text_craft = TextCraft()
input_text = "one two two one two three one one four"
desired_batch_size = 3
occurrence_threshold = 2
print("Occurrences:", count_occurrences(input_text, "one"))
print("Modified Text:", modify_text(input_text, "one", occurrence_threshold))
print("Batches:", split_text_into_batches(input_text, desired_batch_size))
