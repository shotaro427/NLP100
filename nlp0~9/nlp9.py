
import random

def to_typoglycemia(word):
    if len(word) > 4:
        start = word[0]
        end = word[-1]
        middle_text = word[1:-1]
        return ''.join([start] + random.sample(middle_text, len(middle_text)) + [end])
    else:
        return word

rawText = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
ans = [to_typoglycemia(word) for word in rawText.split()]
print(' '.join(ans))