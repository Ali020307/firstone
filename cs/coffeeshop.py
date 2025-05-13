class Coffeeshop:
    def init(self):
        self.menu = {
            "Espresso": 30.000,
            "Latte": 40.000,
            "Cappuccino": 45.000,
            "Americano": 25.000,
            "Mocha": 50.000
        }
        self.zakaz = []

    def displayMenu(self):
        print("\nCoffee shop menu:")
        for item, price in self.menu.items():
            print(f"{item}: {price:.2f} sum")

    def zakaz_qilish(self):
        print("\nBuyurtma bering:")
        self.displayMenu()
        while True:
            tanlash = input("Coffeeni turini tanlang (yoki 'keremas' deb yozing): ").strip()
            if tanlash.lower() == 'keremas':
                print("Buyurtma berildi. Rahmat!")
                break
            elif tanlash in self.menu:
                self.zakaz.append(tanlash)
                print(f"{tanlash} buyurtmangizga qo'shildi.")
            else:
                print("Yaroqsiz tanlov. Iltimos, menyudan tanlang.")

    def Buyurtmani_korish(self):
        if not self.zakaz:
            print("\nBuyurtmangiz boʻsh.")
        else:
            print("\nSizning joriy buyurtmangiz:")
            jami = 0
            for order in self.zakaz:
                price = self.menu[order]
                jami += price
                print(f"{order}: {price:.2f} sum")
            print(f"Jami: {jami:.2f} sum")

    def cancel_order(self):
        if not self.zakaz:
            print("\nBuyurtmangiz boʻsh. Bekor qilish uchun hech narsa yo'q.")
            return
        self.Buyurtmani_korish()
        cancel_item = input("O'chirish uchun qahvaning nomini kiriting: ").strip()
        if cancel_item in self.zakaz:
            self.zakaz.remove(cancel_item)
            print(f"{cancel_item} buyurtmangizdan olib tashlandi.")
        else:
            print("Buyurmangiz topilmadi")

    def run(self):
        while True:
            print("\nHush kelibsiz ")
            print("1. Coffeeni turlari")
            print("2. Buyurtma qilish")
            print("3. Buyurtmani korish")
            print("4. Buyurtmani bekor qilish")
            print("5. Chiqish")
            tanlash = input("Variantni tanlang: ").strip()
            if tanlash == '1':
                self.displayMenu()
            elif tanlash == '2':
                self.zakaz_qilish()
            elif tanlash == '3':
                self.Buyurtmani_korish()
            elif tanlash == '4':
                self.cancel_order()
            elif tanlash == '5':
                print("Kelganiz uchun rahmat, salomat boling!")
                break
            else:
                print("Yaroqsiz tanlov. Qayta urinib koʻring.")
if name == 'main':
    shop = Coffeeshop()
    shop.run()



