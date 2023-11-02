def cloud_function(json_input):
    text = json_input["givenInputStr"]
    batch_size = json_input["batchSizeInt"]
    
    # Processing
    result = [' '.join(words[i:i + batch_size]) for i in range(0, len(words), batch_size)]
    # return the result
    res = {
        "splitBatches": result
    }
    return res
