# Code smell
class Bank:
    def __init__(self):
        self.owners = []
        self.balances = []
        self.ids = []

    def get_new_id(self) -> int:
        if len(self.ids) == 0:
            return 1
        else:
            return self.ids[-1] + 1

    def add_account(self, new_owner: str, new_balance: float) -> int:
        id = self.get_new_id()
        self.owners.append(new_owner)
        self.balances.append(new_balance)
        self.ids.append(id)
        return id

    def withdraw(self, account_number: int, amount: float) -> bool:
        index = self.ids.index(account_number)
        if self.balances[index] < amount:
            return False
        self.balances[index] -= amount
        print(f"Withdrawn {amount}chf from {self.owners[index]}'s account. {self.balances[index]}chf remaining.")
        return True


if __name__ == '__main__':
    account_owner = 'Monica'
    account_balance = 5000

    bank = Bank()
    account_number = bank.add_account(account_owner, account_balance)
    bank.withdraw(account_number, 250)


# Better
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.number = None

    def set_account_number(self, account_number):
        self.number = account_number

    def withdraw(self, amount: float) -> bool:
        if self.balance < amount:
            return False
        self.balance -= amount
        return True


class Bank:
    def __init__(self):
        self._accounts = {}

    def open_account_and_assign_number(self, new_account: Account):
        new_account.set_account_number(self.get_new_account_number())
        self._accounts[new_account.number] = new_account

    def get_new_account_number(self) -> int:
        existing_numbers = list(self._accounts.keys())
        if len(existing_numbers) == 0:
            return 1
        return max(existing_numbers) + 1

    def withdraw_from_account(self, account: Account, amount: float):
        account_number = account.number
        self._accounts[account_number].withdraw(amount)
        print(f"Withdrawn {amount}chf from {account.owner}'s account. {account.balance}chf remaining.")


if __name__ == '__main__':
    bank = Bank()
    account = Account('Monica', 5000)
    bank.open_account_and_assign_number(account)
    bank.withdraw_from_account(account, 250)