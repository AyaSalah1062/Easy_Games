import random
pcnum=random.randint(1, 99);
win =0
turns=8
#print(pcnum)
while turns!=0 :
 # print (i)
  x=int(input("Guess the number: "))
  if x == pcnum:
    print("Winner!")
    win=1
    break
  elif x < pcnum:
    print("Greater number.")
  else:
    print("Smaller number.")
  turns-=1
if(win==0):
  print("LOSER!") 

