'''

@Author: Palash Gupta

@Date: 2024-02-27 17:15:00

@Last Modified by: Palash gupta

@Last Modified time: 2024-02-27 17:15:00

@Title : Write a Python script to sort (ascending and descending) a dictionary by
value.

'''

def ascending(original_dict):
    sorted_ascending = dict(sorted(original_dict.items(), key = lambda x:x[1])) 
    return sorted_ascending
 
def decending(original_dict):
    sorted_decending = dict(sorted(original_dict.items(), key = lambda x:x[1], reverse = True)) 
    return sorted_decending
 
if __name__ =="__main__":
    original_dict = {'a':1, 'b':4, 'c':3, 'd':9, 'e':6}
    print(ascending(original_dict))
    print(decending(original_dict))

