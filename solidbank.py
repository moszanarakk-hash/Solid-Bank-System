class Depositable:
    def deposit(self, amount):
        raise NotImplementedError

class Withdrawable:
    def withdraw(self, amount):
        raise NotImplementedError

class Transferable:
    def transfer(self, target_account, amount):
        raise NotImplementedError


class BankAccount(Depositable, Withdrawable, Transferable):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{self.owner} ฝากเงิน {amount} บาท สำเร็จ")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{self.owner} ถอนเงิน {amount} บาท สำเร็จ")
        else:
            print(f"{self.owner} ยอดเงินไม่เพียงพอ")

    def transfer(self, target_account, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            target_account.__balance += amount
            print(
                f"{self.owner} โอนเงิน {amount} บาท "
                f"ให้ {target_account.owner} สำเร็จ"
            )
        else:
            print(f"{self.owner} ยอดเงินไม่เพียงพอสำหรับการโอน")

    def show_balance(self):
        print(f"ยอดเงินของ {self.owner} = {self.__balance} บาท")


acc1 = BankAccount("สมชาย", 1000)
acc2 = BankAccount("สมหญิง", 500)

acc1.deposit(500)
acc1.withdraw(300)
acc1.transfer(acc2, 400)

acc1.show_balance()
acc2.show_balance()