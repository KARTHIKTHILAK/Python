from bank_accounts import *

Karthik = BankAccount(1000,"Karthik")
Thilak = BankAccount(2000,"Thilak")

Karthik.get_balance()
Thilak.get_balance()

Karthik.deposits(500)
Thilak.deposits(300)

Karthik.withdraw(100)

Karthik.transfer(200,Thilak)

Kumar = InterestRewardAcct(100, "Kumar")
Kumar.get_balance()
Kumar.deposits(100)

Kalaivani = SavingsAcct(1000,"Kalaivani")
Kalaivani.get_balance()
Kalaivani.withdraw(100)

Kalaivani.transfer(5,Karthik)