"""
Write a class called Password_manager. The class should have a list called old_passwords
that holds all of the user’s past passwords. The last item of the list is the user’s current password. There should be a method called get_password that returns the current password
and a method called set_password that sets the user’s password. The set_password
method should only change the password if the attempted password is different from all
the user’s past passwords. Finally, create a method called is_correct that receives a string
and returns a boolean True or False depending on whether the string is equal to the current
password or not
"""
class Password_manager:
    def __init__(self,name,pass_passwords,current_password):
        self.name=name
        self.pass_passwords=pass_passwords
        self.current_password=current_password
        self.old_passwords=pass_passwords+[current_password]
    def set_password(self):
        new_password=input("Enter new password: ")
        while new_password in self.old_passwords:
           new_password=input("please enter another password: ")
        else:
            self.current_password=new_password
            print("{}'s password has been changed".format(self.name))
        return self.current_password
    def is_correct(self):
        enter_password=input("enter your password: ")
        if enter_password==self.current_password:
            return True
        else:
            return False
pass_password=["iloveyou","123456","123456789"]
current_pass="Khanhle"
Khanh=Password_manager("Khanh",pass_password,current_pass)
Khanh.set_password()
Khanh.is_correct()


