class Users:
    activeUsersCount = 0
    
    def __init__(self , userName , userFamily):
        self.name = userName
        self.family = userFamily
        Users.activeUsersCount += 1
        
        