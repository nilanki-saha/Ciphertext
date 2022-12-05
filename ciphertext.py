def encr(s):
    x=""
    for i in range(len(s)):
        x+=chr(ord(s[i])+5)
    return x

def decr(c):
    y=""
    for i in range(len(c)):
        y+=chr(ord(c[i])-5)
    return y

s=input("Text to be encrypted: ")
c=encr(s)
cc=decr(c)
print("Text to be decrypted:",c)
print("Encrypted Text:",c)
print("Decrypted Text:",cc)