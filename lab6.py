"""
lab6
"""
#3.1

# for num in range(6):
#     if num != 3:
#         print(num)

#3.5

# result=0

# for num in range(1,6):
#     result= result + num
    
# print(result)

#3.5

# top_result = 1
# for num in range(1,9):
#     top_result = top_result *num
# print(top_result)

# bottom_result = 1
# for num in range(1,4):
#     bottom_result = bottom_result *num
# print(bottom_result)

# print(top_result/bottom_result)

#3.6

# result = 0

# for word in 'this is my 6th string'.split():
#     # print(word)
#     result = result+1
    
# print(result)

#3.7

my_tweet = {
        'favorite_count':1138,
        'lang':'en',
        'coordinates':(-75,40),
        'entities':{
                    'hashtags':['Preds','Pens','SingintoSpring']
                    }
           }
           
result= 0 
for hahtag in my_tweet['entities']['hashtags']:
    result = result+1
print(result)
