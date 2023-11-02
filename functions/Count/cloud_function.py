def cloud_function(json_input):
    text = json_input["batchStr"]
    pattern = json_input["patternStr"]
    # Processing
    result = sum(1 for word in text.split() if word == pattern)
    # return the result
    res = {
        "count": result
    }
    return res
