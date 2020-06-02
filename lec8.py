"""
lec 8 
functions
"""
# def my_function(a,b=0):
    
#     print('a is ',a)
#     print('b is ',b)
    
#     return a+b

    
# print(my_function(a=1))

#ex1

def calculate_abs(a):
    '''
    return the abs value of imput numbers
    '''
    
    if type(a) is str:
        return ('wrong data type')
        
    elif a >=0:
        return a
    else:
        return -a 
    
# print(calculate_abs('a'))

#ex2

def cal_sigma(m,n):

    result = 0
    for i in range(n,m+1):
        result = result +i 

    return result

# print(cal_sigma(m=5,n=3))

def cal_pi(m,n):

    result = 1
    for i in range(n,m+1):
        result = result*i
        # print('i:',i)
        # print('result:',result)
    
    return result
# print(cal_pi(5,3))

#ex3

def cal_f(m):
    if m ==0:
        return 1 
    else:
        return m * cal_f(m-1)

# print(cal_f(3))

def cal_p(m,n):
    return  cal_f(m)/cal_f(m-n)
# print(cal_p(5,3))
    