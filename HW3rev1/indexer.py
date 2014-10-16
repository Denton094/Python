
import pickle
import shelve

def process_data():
  # read pickle to Filepath_list
  f = open("raw_data.pickle","br")
  Filepath_list = pickle.load(f)
  f.close()
#Create World list to store all searchable words in datalist.
  Word_list =[]
  for tople_list in Filepath_list:
    for elem in tople_list[1].split():
      Word_list.append(elem)

  Word_list = sorted(list(set(Word_list)))

# list created to store file path.
  a = []
# Find key value pair and shelve readings
  for xxx in Word_list:
   # Quote_dic.setdefault(xxx,[]) #set key in dictionary
    for tople_list in Filepath_list:  
      if xxx in tople_list[1].split():
        a.append(tople_list[0]) #amend file path to tuple a

# put files to shelve
    s=shelve.open("fortunes")
    b = tuple(a)
    s["xxx"] = b

    print(Word_list)
    s.close()  

process_data()