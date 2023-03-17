import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the recieved arguments
        assert price >= 0, f"Price {price} is not greater or equal to than zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("the name is too long")
        else:
            self.__name = value
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)        

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero
        # for ie: 5.0, 10.0
        if isinstance(num, float):
            # count out the floats that are piont zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr___(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def connect(self, smpt_server):
        pass

    def connect(self, smpt_server):
        pass

    def prepare_body(self):
        return f"""
        Hellof eoawfjow
        fjoiawefjaewoifjaweoif
        eifjaweofiajfoia
        regards sam
        """
        def send(self):
            pass

    def send_email(self):
        self.connect()
        self.prepare_body()
        self.send()

    