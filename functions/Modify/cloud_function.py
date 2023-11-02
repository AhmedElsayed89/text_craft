def cloud_function(json_input):
    text = json_input["textStr"]
    pattern = json_input["patternStr"]
    m = json_input["occurrenceHolderInt"]
    
    # Processing
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

    result = ' '.join(modified_text)
    # return the result
    res = {
        "modifiedText": result
    }
    return res
