sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

text = sentence.replace('.', '').replace(',', '')
charsList = text.split()
ans = [len(chars) for chars in charsList]
print(ans)