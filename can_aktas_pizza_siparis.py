import csv
import datetime

# Pizza Üst Sınıfı


class Pizza:
    def get_description(self):
        return self.__class__.__name__

    def get_cost(self):
        return self.__class__.cost

# Pizza Alt Sınıfı


class Klasik(Pizza):
    cost = 60.0

    def __init__(self):
        # Her alt sınıf için özellikler
        self.description = "Klasik Pizza Malzemeler: Sucuk, Salam, Mozzarella"
        print(self.description + "\n")


class Margarita(Pizza):
    cost = 65.0

    def __init__(self):
        self.description = "Margarita Pizza Malzemeler: Domates, Fesleğen, Mozarella"
        print(self.description + "\n")


class TurkPizza(Pizza):
    cost = 65.0

    def __init__(self):
        self.description = "Türk Pizza Malzemeler: Kavurma, Soğan, Biber, Kaşar"
        print(self.description + "\n")


class SadePizza(Pizza):
    cost = 50.0

    def __init__(self):
        self.description = "Sade Pizza Malzemeler: Salam, Sucuk, Zeytin, Mozarella"
        print(self.description + "\n")


# Decorator üst sınıfı
class Decorator(Pizza):
    def __init__(self, topping):
        self.component = topping

    def get_cost(self):
        return self.component.get_cost() + \
            Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
            ' ; Seçilen Malzeme: ' + Pizza.get_description(self)

# Decorator Alt Sınıfı


class Zeytin(Decorator):
    cost = 5.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Mantar(Decorator):
    cost = 5.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Peynir(Decorator):
    cost = 5.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Et(Decorator):
    cost = 10.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Sogan(Decorator):
    cost = 2.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Misir(Decorator):
    cost = 3.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)

# Main fonksiyonu


def main():
    with open("Menu.txt") as mus_menu:
        for i in mus_menu:
            print(i, end="")

    class_dict = {1: Klasik,
                  2: Margarita,
                  3: TurkPizza,
                  4: SadePizza,
                  5: Zeytin,
                  6: Mantar,
                  7: Peynir,
                  8: Et,
                  9: Sogan,
                  10: Misir}

    code = input("Lütfen Pizza Çeşitlerinden Birini Seçin: ")
    while code not in ["1", "2", "3", "4"]:
        code = input("Yanlış Tuşlama Yaptınız: ")

    order = class_dict[int(code)]()

    while code != "*":
        code = input(
            "Ek Malzeme Almak İçin Tuşlama Yapın (Malzeme Eklemeden Siparişi Sonuçlandırmak İçin '*' Tuşuna Basın): ")
        if code in ["5", "6", "7", "8", "9", "10"]:
            order = class_dict[int(code)](order)
            print("Seçilen Malzeme Eklendi")

    print("\n Seçilen Pizza: " + order.get_description().strip() + "\n Toplam Tutar: "+str(order.get_cost()) +
          ";"" TL")
    print("\n")

# Sipariş Bilgi Kartı oluşturuyoruz.
    print("----------Sipariş Bilgileri----------\n")
    ad = input("İsminiz: ")
    id = input("TC Kimlik Numaranız: ")
    kk_no = input("Kredi Kartı Numaranız: ")
    kk_sif = input("Kredi Kartı Şifreniz: ")
    kayit_zamani = datetime.datetime.now()

    with open('Orders_Database.csv', 'a') as orders:
        orders = csv.writer(orders, delimiter=',')
        orders.writerow(
            [ad, id, kk_no, kk_sif, order.get_description(), kayit_zamani])
    print("Siparişiniz Onaylandı.")


main()
