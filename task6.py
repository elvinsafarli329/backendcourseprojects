# İlk classımızda bizim hesab nömrəsi (int) və balans argumentlərimiz olacaq.
# Metod olaraq 3 fərqli metoddan istifadə edəcəyik Balansı artırmaq,  Pul çıxarmaq  və balansı göstərmək üçün metodlar.
# İkinci classımız isə kreditlə bağlıdır. İlk classımızı bu classa inheritance eliyəcəyik və  super initdən  istifadə edəcəyik. 
# Bu classda bizim 2 metodumuz olacaq.
# Kredit vermək və kredit ödənişi. Bu səbəbdən classımızın əlavə kimi 1 argumenti olacaq.
# Kredit götürüləcək məbləğ. Kredit sadəcə 1 il müddəti üçündür və faiz yoxdur (kreditinməbləği / 12=aylıq ödəniş).

import datetime 

class bank_details():
    def __init__(self, acc_num, amount: float,):
        self.acc_num = acc_num
        self.amount = amount
        self.time = datetime.datetime.now()

    def set_money(self, dollar):
        self.amount += dollar
        print(f" at {self.time.strftime("%B" "%Y")} {dollar} balansiniza medaxil odlu, hesab: {self.amount}")

    def get_money(self, dollar):
        if self.amount > 0 and dollar <= self.amount:
            self.amount -= dollar
            print(f"{dollar} hesabdan cixdi, qaliq: {self.amount}")
        else:
            print("hesabda yeterli mebleg yoxdur")

    def show_amount(self):
        print(f" at {self.time} Balansiniz: {self.amount}")

class loans(bank_details):
    def __init__(self, acc_num, amount: float, credit_amount):
        super().__init__(acc_num, amount)
        self.credit_amount = credit_amount

    def get_loan(self):
        if self.amount >= self.credit_amount:
            self.amount -= self.credit_amount/12
            print(f"{self.credit_amount} goturulmus kreditin {self.credit_amount/12} her ay odenilecek")
        else:
            print("credit verilecek mebleg coxdur")

    def set_loan(self):
        self.amount += self.credit_amount 
        print(f"{self.credit_amount} qaytarildi, borcunuz qalmadi ")



exampe_num = bank_details(10001000, 4000)
kredit_num = loans(10001000, 10000, 1200)
exampe_num.show_amount()
exampe_num.get_money(30)
exampe_num.set_money(555)
kredit_num.get_loan()
kredit_num.set_loan()