import random
list=["mango","banana","peach"];
# print(list[0])
pc=random.randint(0,len(list)-1)
print(list[pc])
fruit=list[pc]
word=[]
for i in range (len(fruit)):
  w = '_'
  word.append(w)
# print(fruit[0])
print(word)
# for i in range (len(list)):
#  arr[]=list[i];
tries=0
# while tries<len(fruit)+4:
#     x=input("enter a letter: ");
#     if x in fruit:
#     #     for i in range (fruit) :
#     #         if(x==fruit[i]):
#     #         word[i]=x;
#     #         print(word)
#     #         if(word==fruit):
#     #             print(word);
#     #             print("WINNER")
#         for i in range(len(fruit)):
#             if x == fruit[i]:
#                 word[i] = x
#         print(word)
#         if "_" not in word:
#             print("Congratulations, you guessed the word!")
#             break
#     else:
#         tries += 1
#         print("Incorrect guess. You have", len(fruit) + 4 - tries, "tries left.")
# else:
#     print("Sorry, you ran out of tries. The word was", fruit)

while tries < len(fruit) + 4:
    x = input("Enter a letter: ")
    if x in fruit:
        tries += 1
        for i in range(len(fruit)):
            if x == fruit[i]and word[i] == "_":
                word[i] = x
                break;
        print( word ," . You have", len(fruit) + 4 - tries, "tries left.")
        if "_" not in word:
            print("Congratulations, you guessed the word!")
            break
    else:
        tries += 1
        print("Incorrect guess. You have", len(fruit) + 4 - tries, "tries left.")
else:
    print("Sorry, you ran out of tries. The word was", fruit)   

           
    
