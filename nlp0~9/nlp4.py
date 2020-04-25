# rawText = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

# textList = rawText.replace('.', '').split()
# mappedList = {}

# for i in range(len(textList)):
#     if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
#         text = textList[i][0]
#         mappedList[text] = i
#     else:
#         text = textList[i][:2]
#         mappedList[text] = i
    
# print(mappedList)

def extWord(i, word):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        return (word[0], i)
    else:
        return (word[:2], i)


rawText = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
text = rawText.replace('.', '').replace(',', '')
ans = [extWord(i, w) for i, w in enumerate(text.split(), 1)]
print(dict(ans))