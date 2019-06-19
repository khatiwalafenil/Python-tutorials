class SecretClass :
    __secretVar  = 10

    def __init__ (self) :
        print ("constructor of secret class")
    
 

 
secretObj = SecretClass ()
print (secretObj.__secretVar)
