"""
lec 6
"""
demo_str = 'this is my string'

# for str_item in demo_str:
#     print(str_item)

# for word_item in demo_str.split():
#     print(word_item)


#print(range(5))
# for each_num in range(1,5):
#     print(each_num)

num_list =[213,321,123,312]

max_item = num_list[0]  # max_item is the placeholder, 
                        # and use the first item in the list
                        # as the intial value
                        
for num in num_list:
    if max_item <= num:
        max_item = num 

print(max_item)
