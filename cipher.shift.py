import random
def generateCode(a,z):
    numA=ord(a)
    numZ=ord(z)
    alp=range(numA,numZ+1,1)
    code=''
    while len(code) < len(alp) :
        c = chr(random.choice(alp))
        if not c in code :
            code += c
    src=list()
    for c in alp:
        src += chr(c)
    print ('last alphabet letter: ' +chr(alp[len(alp)-1]))
    return str.maketrans(''.join(src),code)

def encode(text, code):
    return text.translate(code)

code = generateCode('a', 'z')
#print(code)
txt=''
while 1==1:
    txt=input('enter text: ')
    if txt=='':
        break
    print(encode(txt,code))

