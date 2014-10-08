import data_list from data_load
import pickle


def process_data():
  # assign topple set to
  f = open("raw_data.pickle","br")
  Filepath_list = pickle.load(f)
  f.close()

process_data(

#Create World list to store all searchable words in datalist.
Word_list =[]
  for quote in data_list:
    for word in quote.split():
      Word_list.append(word)

b = set(Word_list)

Word_list = sorted(list(b))

  # Create a dictionary that stores the searchable words as key and the associate value is the quote index that contains that word

Quote_dic = {}
  for xxx in Word_list:
    Quote_dic.setdefault(xxx,[])
      for tople in Filepath:  
        Quote_dic[xxx].append(1)

print(Quote_dic)