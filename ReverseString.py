Sentence = input('Please insert your text: ')
#sequence[start:stop:step]
def ReverseSentence(sentence):
    print(sentence[::-1])

def ReverseWords(sentence:str):
    WordList = sentence.split()
    WordsReverted = [word[::-1] for word in WordList]
    print(''.join(WordsReverted))


ReverseSentence(sentence= Sentence)
ReverseWords(sentence= Sentence)