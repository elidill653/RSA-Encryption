"""
#   Encrypts strings to int values
#   using RSA encryption
#
#
#
"""

def encrypt(M, PU):  # M list PU List
    C = []
    for i in M:
        a = (i**PU[0])%PU[1]
        
        C.append(a)
        
    return C

def decrypt(C, PR):

    M = []
    for i in C:
        a = (i**PR[0])%PR[1]

        M.append(a)
     
    return M

def keygen(p , q):
    
    n = p*q
    phi_n = (p-1)*(q-1)

    e = 2
    E = []                 #need to find 5 e

    for i in range(5):
        while gcd(phi_n, e) != 1:   # this will search for an e that is prime
           e+=1
        E.append(e)        #store the prime e
        e+=1
    
    #Find all d Values
    D = []

    for i in range(5):
        D.append(euc(phi_n,E[i]))



    #return E D n and phi n

    keys = (E,D, n, phi_n)
    return keys
    
#end

def euc(a, b):
    #phi_n = a, e = b
    dd, dv = a, b

    r = [a, b, 0]
    x = [1, 0, 0]
    y = [0, 1, 0]
    i = 2
    q = dd/dv #divisor/ dividend

    r[i] = a - q*b

    while(r[i] != 0):
        q = dd/dv #divisor/ dividend


        r[i] = r[i-2]-r[i-1] * q
        y[i] = y[i-2]-y[i-1] * q
        x[i] = x[i-2]-x[i-1] * q
        
        
        r[i-2] = r[i-1]
        r[i-1] = r[i]
        y[i-2] = y[i-1]
        y[i-1] = y[i]
        x[i-2] = x[i-1]
        x[i-1] = x[i]

        dd, dv = dv, r[i]
    return ((y[i-2])%a)

def gcd(a, b):
    while(b != 0):
        rem = a%b
        
        a = b
        b = rem
    return a


def to_int(M):
    alphaL = 'abcdefghijklmnopqrstuvwxyz'
    alphaU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numPlus ='0123456789 .,:?'
    
    rsaBlock = alphaL +alphaU +numPlus  # rsa list
    newM = []
    for i in M:
        if i in rsaBlock:
            newM.append(rsaBlock.find(i))

    m = [] #array grouped into pairs
    
    i = 0
    while i < len(newM):
        tmp = newM[i]*100 + newM[i+1]
        m.append(tmp)
        i+=2
    return m


def to_char(M):
    alphaL = 'abcdefghijklmnopqrstuvwxyz'
    alphaU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numPlus ='0123456789 .,:?'
    
    rsaBlock = alphaL +alphaU +numPlus

    newM = []
    i = 0
    while i < len(M):
        tmp = M[i]/100
        newM.append(tmp)
        newM.append(M[i]-tmp*100)
        i+=1
        
    pt =''
    for i in newM:
        pt+=rsaBlock[i]
    return pt


def main():
    
    p = 73
    q = 151
    plaintext = "How are you?"

    M = to_int(plaintext)
    
    keys = keygen(p,q)
    
    E = keys[0]
    D = keys[1]
    n = keys[2]
    phi_n = keys[3]
    
    print "RSA Key info:"
    print "Original plain text: %s" % plaintext
    print "n: %d, Phi(n): %d" %(n, phi_n)
    print "List of e's: ", E
    print "List of d's", D

    print "\n"
    
    for i in range(5):
                
        PU = [E[i], n]
        PR = [D[i], n]
        cipher = encrypt(M ,PU)
        pt = decrypt(cipher, PR)

        print "Public key: ", PU        
        print "Cipher text :" ,cipher
        print "Private key: ", PR
        print "Plain text :" ,pt

        print "\n"
        
    dec = to_char(M)
    print "Decrypted cipher text: %s" % dec


    
main()
