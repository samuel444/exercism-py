
def is_pangram(sentence):
    sentence=sentence.upper()
    count = 0
    result = False
    for testchar in range (0,26):
        if chr(65+testchar) in sentence:
            count+=1
    if count == 26:
        result = True 
    return result
    pass

is_pangram("abcdefghijklmnopqrstuvwxyz")
