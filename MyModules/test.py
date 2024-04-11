class Users:
    userName = "shaghayegh"
    userFamily = "mousavi"
    userAge = 20

    def showfullname(self):
        return self.userName + self.userFamily
person=Users()
print(person.userFamily)