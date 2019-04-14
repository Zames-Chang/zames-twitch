import re
from hashlib import sha256


class Account(object):

    def __init__(self,account,password1,password2):
        self.account = account
        self.password1 = password1 
        self.password2 = password2
        self.hash_password = self.__to_sha256(password1)
        self.errors = {
            -1 : 'account contain invaild word',
            -2 : 'password contain invaild word',
            -3 : 'password not match',
        }

        self.__account_rule = "^([0-9]|[[a-zA-Z]])*$" #acceptable account patten
        self.__password_rule = "^([0-9]|[[a-zA-Z]])*$" #acceptable password patten
    def is_valid(self):
        """
        @ return : True if account password1, password2 are same and contain only number and char
        """
        account_rule = self.__account_rule
        password_rule = self.__password_rule
        if(not re.match(account_rule,self.account)):
            return -1
        elif(not re.match(password_rule,self.password1)):
            return -2
        elif(self.password1 != self.password2):
            return -3
        return 0

    def __to_sha256(self,password):
        salt = "Ztex"
        return sha256((password+salt).encode('utf-8')).hexdigest()