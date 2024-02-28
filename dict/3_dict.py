'''

@Author: Palash Gupta

@Date: 2024-02-27 17:15:00

@Last Modified by: Palash gupta

@Last Modified time: 2024-02-27 17:15:00

@Title :Write a Python script to concatenate following dictionaries to create a new
one..
'''
def Merge(dic1, dic2, dic3):
    res = {}
    res.update(dic1)
    res.update(dic2)
    res.update(dic3)
    return res


if __name__ == "__main__":
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50, 6:60}

    print(Merge(dic1, dic2, dic3))
    