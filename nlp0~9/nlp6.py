
def createNGram(target, n):
    return [target[i:i + n] for i in range(len(target) - n + 1)]

rawTextX = 'paraparaparadise'
rawTextY = 'paragraph'

setX = set(createNGram(rawTextX, 2))
setY = set(createNGram(rawTextY, 2))

targetSet = {'se'}

print(setX | setY)
print(setX & setY)
print(setX - setY)
print(setY - setX)
print(targetSet <= setX)
print(targetSet <= setY)
