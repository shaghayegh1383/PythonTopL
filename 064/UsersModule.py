class Users:
    activeUsers = 0
    #login
    def __init__(self , name , family):
        self.name = name
        self.family = family
        Users.activeUsers +=1
        print (f"{self.name}logged in")
        
        #logout
    def logout(self):
        Users.activeUsers -=1
        print (f"{self.name}has logged out")
        
print (Users.activeUsers)
me = Users('shaghayegh' , 'mousavi')
print (Users.activeUsers)
        