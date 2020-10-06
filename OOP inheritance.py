class Account:
    # a variable outside the method is called class variable
    count=0 #it like static variable in c++
    #@ ->decorator
    @classmethod
    def incr_count(cls):
        cls.count+=1
    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def print_val():#no need to called with object
        print("static method ")

    def __init__(self,customer_id,balance=0):#if a function have __ in first and last it means it is
        # called implicitly
        self.customer_id=customer_id   #self.__customer_id -> declaring private
        self.balance=balance
        # Account.count+=1  #or
        Account.incr_count()

    def diposite(self,balance):
        self.balance+=balance
        print("Succesfully deposited amount ",balance)
    def withdrawal(self,amount):
        if amount>self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return self.balance
    def get_balance(self):
        return self.balance

#inheritance

class saving_account(Account):
    def __init__(self,id,name,initial_bal=0):
        super().__init__(id,initial_bal) #if we want to call init method in parent class then super keyword is used
        self.limit=5000
    def withdrawal(self,amount):#overriding: it will first search in the child class if the method doesn't exist it will
        #go to the parent class
        if amount<self.limit:
            new_bal=super().withdrawal(amount)
            self.limit-=amount
            return new_bal
        else:
            print("Daily Limit Reached")

#python supports multiple inheritance
class A:
    pass
class B:
    pass
class C(A,B):
    pass

#python follow depth first left to write approach, that means it will search bottom class at first then left to rigth

obj=C()
help(obj)

cust1=saving_account("101","ABC")
print(cust1.diposite(800000))
print(cust1.withdrawal(3000))
print(cust1.withdrawal(3000))
# print(cust1.__dict__)
# print(help(cust1))




