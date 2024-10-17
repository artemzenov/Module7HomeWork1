class Shop:

    def __init__(self):
        self.__file_name = 'product.txt'

    def add(self, *products):
        file = open(self.__file_name, 'a')
        for i_product in products:
            if i_product.name in self.get_products():
                print(f'Продукт {i_product.name} уже есть в магазине')
            else:
                file.write(f'{i_product}\n')
        file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        info = file.read()
        file.close()
        return info