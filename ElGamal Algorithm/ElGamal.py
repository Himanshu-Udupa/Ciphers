import math  #importing math module to use pow() method

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def group(p):
    #generating group G=<Zp*,X>
    #it is called as finite multiplicative group. the group contains elements from 1 to p-1 that are relatively prime to p
    L=[]
    for i in range(1,p):
        if gcd(i,p)==1:
            L.append(i)
    return L

def generate_factors(a):
    #generating factors of a number a
    L=[]
    for i in range(1,a+1):
        if a%i==0:
            L.append(i)
    return L

#method to generate primitive roots
def primitive_root(G,p):
    #order of group G=<Zp*,X> is number of elements in that group
    #order of element,a, is smallest integer i such that (a^i mod p) = 1
    #and it is to be noted that order of element always divides order of group thus i should be factors of p-1(because order of group is p-1)
    #primitive roots are numbers in group G=<Zp*,X> such that order of element is same as phi(p)[order of group] and as p is prime number, phi(p)=p-1
    phi=p-1   #because p is prime number order of group G is p-1
    factors=generate_factors(p-1)
    roots=[] #empty list
    for i in G:
        for j in factors:
            if math.pow(i,j)%p==1:
                roots.append(i) #primitive roots are added to list
                break
    return roots 

#method to generate public key and private key
def key_generation():
    p=int(input("Choose a prime number p:"))  #choose a prime number p
    G=group(p)  #generating group G=<Zp*,X> to choose d.
    print(G[:len(G)-1])
    d=int(input("Choose a value for d from above list:"))  #choosing a value for d. 1<=d<=p-2
    l=primitive_root(G,p)  #calling primitive root() method which returns the set of primitive roots in group G
    print("primitive roots are:\n",l)
    e1=int(input("choose a primitive root(e1) from above list:"))  #choosing a primitive root e1.
    e2=math.pow(e1,d)%p  #calculating e2
    return [e1,e2,p], d, G  #returning both public key, private key and Finite multiplicative group G

#method for encryption
def encryption(public_key, G):
    P=int(input("Enter the plain text:"))  #plain text is taken as input
    print(G)
    r=int(input("Choose a value for r from above list:"))  #choose a random integer r from the group G=<Zp*,X>
    C1=math.pow(public_key[0],r)%public_key[2]  #cipher_text1=(e1^r)mod p
    C2=(P*math.pow(public_key[1],r))%public_key[2]  #cipher_text2=(P*e2^r)mod p
    return C1, C2

#method for decryption
def decryption(d, p, C1, C2):
    return (C2*math.pow(C1,p-1-d))%p  #plain_text=(C2*(C1^p-1-d))mod p


print("KEY GENERATION")
public_key, private_key, G=key_generation()  #key generation method called which returns public key and private key
print("Public key is ",public_key)
print("\nENCRYPTION")
cipher_text1, cipher_text2=encryption(public_key, G)  #encryption method called
print(f"Cipher text is: {(cipher_text1, cipher_text2)}")
print("\nDECRYPTION")
plain_text=decryption(private_key,public_key[2],cipher_text1, cipher_text2)  #decryption method is called
print(f"Plain text is: {plain_text}")
