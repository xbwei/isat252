"""
lab 9

classes
"""
#3.2 
class my_stat():
    
    def cal_sigma(self,m,n):
        self.result = 0
        for i in range(n,m+1):
            self.result = self.result +i 
        return self.result 
        
    def cal_pi(self,m,n):
    
        self.result = 1
        for i in range(n,m+1):
            self.result = self.result*i
        return self.result
        
    def cal_f(self,m):
        if m ==0:
            return 1 
        else:
            return m * self.cal_f(m-1)
            
    def cal_p(self,m,n):
        return  self.cal_f(m)/self.cal_f(m-n)

#3.3
my_cal = my_stat()
print(my_cal.cal_sigma(5,3))
print(my_cal.cal_pi(5,3))
print(my_cal.cal_f(5))
print(my_cal.cal_p(5,3))