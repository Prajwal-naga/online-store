class store:
    storename = 'BANASHANKARI CLOTH STORES'
    owner = 'jagannath'
    phno = 9382934298

    def __init__(self, name, age, phno, total):
        self.name = name
        self.age = age
        self.phno = phno
        self.total= total

    def catalog(self):
        order = {'pant': ['cotton', 'jeans', 'cottonjeans'], 'shirt' : ['cotton' , 'jeans', 'palister']}
        print(f'select the items as shown here {order}')
        o = int(input('enter 1 for pant , 2 for shirt and 3 for others'))
        if o == 1:
            t = int(input('enter 1 for cotton , 2 for jeans and 3 for cottonjeans'))
            if t == 1:
                print('available')
            elif t == 2 :
                print('available')
            elif t == 3:
                print('available')
            else:
                print('not available')
        elif o == 2:
            t2 = int(input('enter 1 for cotton , 2 for jeans and 3 for palister'))
            if t2 == 1:
                print('available')
            elif t2 == 2 :
                print('available')
            elif t2 == 3:
                print('available')
            else:
                print('not available')
    
    def bill(self, amount):
        self.total = self.total+amount

class online(store):
    email_id = 'SBCSonline@gmail.com'
    website = 'www.sbcs.com'

    def __init__(self, name, age, phno, total,email_id):
        super().__init__(name, age, phno, total)
        self.email_id = email_id
    
    def catalog(self):
        super().catalog()
        spant = (28, 30,32,34,36)
        sshirt = ('s','m','l','xl')
        sp = int(input(f'enter the size {spant}'))
        if sp in spant:
            print('order selected')
        ss = input(f'enter the size {sshirt}')
        if ss in sshirt:
            print('order selected')
            

c1 = online('payal', 22,9028439028, 0 , 'payal2@gamil.com')
c1.catalog()
c1.bill(1000)
print(c1.__dict__)

# from abc import abstractmethod, ABC
# class bank: 
#     @abstractmethod
#     def deposit():
#         pass

#     @abstractmethod
#     def withdra():
#         pass
# class banl_:
#     def deposit(self):
#         print('amount credited')
#     def withdra(self):
#         print('amount removed')

# c1 = banl_()
# c1.deposit()
# c1.withdra()
