"""
lab 8
"""

#3.1

def cal_words(input_str):
    
    return len(input_str.split())
    
#3.2
demo_str='hello world!'
# print(cal_words(demo_str))

#3.3
def find_min(inpu_list):
    min_item = inpu_list[0]  
    for num in inpu_list:
        if type(num) is not str:
            if min_item >= num:
                min_item = num 
    return min_item
#3.4
demo_list = [1,2,3,4,5,6]
print(find_min(demo_list))

#3.5
mix_list = [1,2,3,4,'a',6]
print(find_min(mix_list))