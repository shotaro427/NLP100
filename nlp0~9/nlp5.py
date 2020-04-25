def sliceNGram(target, n):
    return [target[i:i + n] for i in range(len(target) -n + 1)]
 
rawText = 'I am an NLPer'
words = rawText.split()
print(sliceNGram(rawText, 2))
print(sliceNGram(words, 2))