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
    def withdrawal(self,amount):
        if amount>self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return self.balance
    def get_balance(self):
        return self.balance


customer1=Account("101",500)
customer2=Account("102",500)
customer3=Account("103",500)
customer4=Account("104",500)

print(customer1.customer_id,customer1.balance)
customer1.diposite(500)
print(customer1.get_balance())

l=[customer1,customer2,customer3,customer4]

for obj in l:
    print(obj.customer_id,obj.balance)

print(Account.count)
Account.count+=5
customer1.count=10 #it will store count=10 only for customer1,here python wll create local varible for the object
print(customer1.__dict__)#here count variable will be shown
print(customer2.__dict__)
print(Account.__dict__)