import random
low='abcdefghijklmnopqrstuvwxyz'
upp='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dig='0123456789'
sig='~!@#$%&*()_-+={}[]:;<>,./?|'

all=low+upp+dig+sig
length=int(input("Enter the desired length of password :"))
pas=random.sample(all,length)
password="".join(pas)
print(f"the generated password of length {length} is :{password}")