from datetime import datetime
from indexer import Quote_dic

#Place users input in a set to prevent duplicates
user_input = input("Enter query: ")
b = user_input.split()
user_input =  set(b)

dt1 = datetime.now()

# Perform AND search..
if ((("and") in user_input) and (("or") in user_input)) or (("and") in user_input):
    if(("or") not in  user_input):
        user_input.remove("and")
    else:
        user_input.remove("and")
        user_input.remove("or")
        
    
    print("Performing AND search for :", user_input)
    list1 = []
    n = 0
    for word in user_input:
        if(word in Quote_dic):
            list1.append(Quote_dic.get(word))
            n += 1
       
    # Find common element for a maximum of 6 separate list        
    if(n == 2):
        g = set(list1[0]) & set(list1[1]) 

    elif(n == 3):
        g = set(list1[0]) & set(list1[1]) & set(list1[2]) 

    elif(n == 4):
        g = set(list1[0]) & set(list1[1]) & set(list1[2]) & set(list1[3])

    elif(n == 5): 
        g = set(list1[0]) & set(list1[1]) & set(list1[2]) & set(list1[3]) & set(list1[4]) 

    elif(n == 6):  
        g = set(list1[0]) & set(list1[1]) & set(list1[2]) & set(list1[3]) & set(list1[4]) & set(list1[5])
   
    if (g != 0):
        print("\nFound at", len(g),"places in data list. Quotes indexes are:",g)
        dt2 = datetime.now() 
        print("\nExecution time:",(dt2 - dt1),"s") 

#Perform OR search
elif(("or") in user_input):
    user_input.remove("or")
    print("Performing OR search for : ", user_input)
    for word in user_input:
        if(word in Quote_dic):
            print("\nFound ",word,"at", len(Quote_dic[word]),"places in data list. Quotes indexes are:",Quote_dic.get(word))
            dt2 = datetime.now() 
            print("\nExecution time:",(dt2 - dt1),"s") 
           
