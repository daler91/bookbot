def sort_characters(characterDict):
    charList = []
    for key, value in characterDict.items():
        newDict = {"char": key, "num": value}
        charList.append(newDict)

    def sort_on(items):
        return items["num"]

    charList.sort(reverse = True, key = sort_on)
    return charList




def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characterDict = {}
    count = 0
    lowerCaseText = text.lower()

    for character in lowerCaseText:
        if character in characterDict:
            characterDict[character] += 1
        else: 
            characterDict[character] = 1

    return characterDict