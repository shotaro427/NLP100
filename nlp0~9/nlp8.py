
def cipher(text):
    text = [chr(219 - ord(w)) if 97 <= ord(w) <= 122 else w for w in text]
    return ''.join(text)

anngo = cipher('hello world.')
raw = cipher(anngo)
print(anngo)
print(raw)
