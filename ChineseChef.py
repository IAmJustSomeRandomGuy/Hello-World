from Chef import Chef


class ChineseChef(Chef):
    def make_special_dish(self):
        print("The chef made noodles")

    def make_rice(self):
        print("The chef made rice")
        print(self)
