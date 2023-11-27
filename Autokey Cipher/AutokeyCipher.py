characters={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
text={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

def encryption(plain_text, key):
    cipher_text=""
    i=0
    for ch in plain_text:
        if i==0:
            num=(characters[ch]+key)%26
        else:
            num=(characters[ch]+characters[plain_text[i-1]])%26
        cipher_text+=text[num]
        i+=1
    return cipher_text

def decryption(cipher_text, key):
    plain_text=""
    i=0
    for ch in cipher_text:
        if i==0:
            num=(characters[ch]-key)%26
        else:
            num=(characters[ch]-characters[plain_text[i-1]])%26
        num=num+26 if num<0 else num
        plain_text+=text[num]
        i+=1
    return plain_text

#Encryption
print("ENCRYPTION:")
plain_text=input("Enter the plain text for encryption:")
key=int(input("Enter the key"))
cipherText=encryption(plain_text.replace(" ","").upper(),key)
print("The cipher text is "+cipherText)

#Decryption
print("\nDECRYPTION:")
cipher_text=input("Enter the cipher text for decryption")
key=int(input("Enter the key"))
plainText=decryption(cipher_text.replace(" ","").upper(),key)
print("The cipher text is "+plainText)
