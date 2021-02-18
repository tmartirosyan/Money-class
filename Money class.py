class Money:
    AMOUNT = 0
    CURRENCY = ""

    def __init__(self, amount: int, currency: str):
        self.AMOUNT = amount
        self.CURRENCY = currency

    def report_about_money(self):
        print(f"You have {self.AMOUNT} {self.CURRENCY}")

    def sum(self, money: int):
        self.AMOUNT += money
        self.report_about_money()

    def sub(self, money: int):
        if not self.AMOUNT - money < 0:
            self.AMOUNT -= money
            self.report_about_money()
        else:
            print("You have not such money!")

    def __repr__(self):
        return f"You have {self.AMOUNT} {self.CURRENCY}"


Aram = Money(500, 'USD')
print(Aram)

Aram.sum(10)
Aram.sub(100)
Aram.sub(520)
