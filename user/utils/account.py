import re
from hashlib import sha256


class Account(object):

    def __init__(self,account,password1,password2):
        self.account = account
        self.password1 = password1 
        self.password2 = password2
        
        self.__account_rule = "^([0-9]|[[a-zA-Z]])*$" #acceptable account patten
        self.__password_rule = "^([0-9]|[[a-zA-Z]])*$" #acceptable password patten
        self.__salt = "Ztex"

    def is_valid(self):
        """
        @ return : True if account password1, password2 are same and contain only number and char
        """
        account_rule = self.__account_rule
        password_rule = self.__password_rule
        if(self.password1 != self.password2):
            return False
        if(not re.match(rule,self.account)):
            return False
        if(not re.match(rule,self.password1)):
            return False
        return True

    def to_sha256(self):
        return sha256(self.password1+self.__salt).hexdigest()