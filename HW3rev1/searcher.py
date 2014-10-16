# GEORGE DENTON
#I couldnt retrieve data from fortunes.db using shelve command. Everything else works



from datetime import datetime
import shelve

def search():
#Place users input in a set to prevent duplicates
    user_input = input("Enter query: ")
    b = user_input.split()
    user_input =  set(b)

    dt1 = datetime.now()

    # Perform AND search..removing AND and OR from query
    if ((("and") in user_input) and (("or") in user_input)) or (("and") in user_input):
        if(("or") not in  user_input):
            user_input.remove("and")
        else:
            user_input.remove("and")
            user_input.remove("or")
        
        print("Performing AND search for :", user_input)
        list1 = []
    # looping thru shelve and creating list of the values. Each value turn to set to perform interesection
        
        for word in user_input:
            s = shelve.open("fortunes.db")
            if("word" in s):
                print(s["word"])
                list1.append(set(s["word"]))

            elif(word not in s):
                print("Query words cant do AND search")
                break  
            s.close()    
            
        result = set.intersection(*list1) #intersecton cmd line       
    # print intersection result as list
        for b in result:
            print("\nFound at ",b )                        
            dt2 = datetime.now() 
            print("Execution time:",(dt2 - dt1),"s")     

    #Perform OR search ......removing OR from query
    elif(("or") in user_input):
        user_input.remove("or")
        print("Performing OR search for : ", user_input)
        s = shelve.open("fortunes.db")
        print(s["broke"])
        for word in user_input:

            if(word in s):
                result = s[word]# As match list is found loop thru content and print all of its conten
                for b in result:
                    print("\nFound at ",b)        
                    dt2 = datetime.now() 
                    print("Execution time:",(dt2 - dt1),"s") 
        s.close()                    
search()           