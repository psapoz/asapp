import unittest


class Person:
    __legal_age = 18
    __dni_min, __dni_max = 0, 99999999
    __age_min = 0
    __age_error_msg = 'La edad ingresada es inválida.'
    __dni_error_msg = 'El dni ingresado es inválido.'
    __display_msg = 'Nombre: {} - Edad: {} - DNI: {}'

    def __init__(self, dni, fullname='', age=0):
        self.__dni(dni)
        self.fullname = fullname
        self.age = age

    @property
    def fullname(self):
        return self.__fullname

    @property
    def age(self):
        return self.__age

    @property
    def dni(self):
        return self.__dni

    @fullname.setter
    def fullname(self, fullname):
        self.__fullname = fullname.strip()

    @age.setter
    def age(self, age):
        if age < Person.__age_min:
            raise ValueError(Person.__age_error_msg)
        self.__age = age

    def __dni(self, dni):
        if dni < Person.__dni_min or dni > Person.__dni_max:
            raise ValueError(Person.__dni_error_msg)
        self.__dni = dni

    def display(self):
        print(Person.__display_msg.format(self.fullname,
                                          self.age,
                                          self.dni))

    def is_legal_age(self):
        return self.age >= Person.__legal_age

    @staticmethod
    def legal_age():
        return Person.__legal_age


class Account:
    __new_balance_msg = 'Su nuevo balance es de {}$'
    __unmodified_balance_msg = 'Su balance de {}$ no se ha modificado.'

    def __init__(self, holder, amount=0.0):
        self.holder = holder
        self.__balance = amount

    def display(self):
        self.holder.display()

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(Account.__new_balance_msg.format(self.__balance))
        else:
            print(Account.__unmodified_balance_msg.format(self.__balance))

    def withdraw(self, amount):
        self.__balance -= amount
        print(Account.__new_balance_msg.format(self.__balance))


class YoungAccount(Account):
    __age_max = 24
    __allowance_min = 0
    __account_description = 'Cuenta Joven con bonificación del {}%'
    __age_req_msg = 'el titular debe tener entre {} y {} años inclusive.'
    __account_req_msg = f'Para crear una Cuenta Young, {__age_req_msg}'
    __withdrawal_req_msg = f'Para retirar dinero, {__age_req_msg}'
    __allowance_error_msg = 'La bonificación ingresada es inválida.'

    def __init__(self,
                 tentative_holder,
                 allowance,
                 amount= 0.0):
        if not self.__is_valid_acc_age(tentative_holder.age):
            raise ValueError(
                YoungAccount.__account_req_msg.format(Person.legal_age(),
                                                      self.__age_max))
        super().__init__(tentative_holder, amount)
        self.allowance = allowance

    @property
    def allowance(self):
        return self.__allowance

    @allowance.setter
    def allowance(self, percentage):
        if percentage < YoungAccount.__allowance_min:
            raise ValueError(YoungAccount.__allowance_error_msg)
        self.__allowance = percentage

    def display(self):
        super().display()
        print(YoungAccount.__account_description.format(self.allowance))

    def is_valid_holder(self):
        return self.__is_valid_acc_age(self.holder.age)

    def withdraw(self, amount):
        if not self.is_valid_holder():
            raise ValueError(
                YoungAccount.__withdrawal_req_msg.format(Person.legal_age(),
                                                         self.__age_max))
        super().withdraw(amount)

    @staticmethod
    def __is_valid_acc_age(age):
        print(age)
        return Person.legal_age() <= age <= YoungAccount.__age_max


class TestYoung(unittest.TestCase):

    def test_data_setup(self):
        juana = Person(12345678, 'Juana', 18)
        juana_acc = YoungAccount(juana, 20, 5000.20)
        self.assertEqual(juana_acc.holder.dni, 12345678)
        self.assertEqual(juana_acc.holder.fullname, 'Juana')
        self.assertEqual(juana_acc.holder.age, 18)
        self.assertEqual(juana_acc.allowance, 20)
        self.assertEqual(juana_acc.balance, 5000.20)

    def test_account_creation(self):
        juana = Person(12345678, 'Juana', 18)
        juana_acc = YoungAccount(juana, 20, 1000)
        self.assertEqual(juana_acc.holder, juana)
        self.assertEqual(juana_acc.allowance, 20)

        pedro = Person(12345679, 'Pedro', 17)
        self.assertRaises(ValueError, YoungAccount, pedro, 20)

    def test_withdrawal(self):
        pepe = Person(123456, 'Pepe', 22)
        pepe_acc = YoungAccount(pepe, 10, 2000)
        pepe_acc.withdraw(100)
        self.assertEqual(pepe_acc.balance, 1900)

        pepe_acc.holder.age = 32
        self.assertRaises(ValueError, pepe_acc.withdraw, 100)

    def test_deposit(self):
        pepe = Person(123456, 'Pepe', 22)
        pepe_acc = YoungAccount(pepe, 10, 2000)
        pepe_acc.deposit(500)
        self.assertEqual(pepe_acc.balance, 2500)

        pepe_acc.deposit(-100)
        self.assertEqual(pepe_acc.balance, 2500)

    def test_is_optional_initial_balance(self):
        pepe = Person(123456, 'Pepe', 22)
        pepe_acc = YoungAccount(pepe, 10)
        self.assertEqual(pepe_acc.balance, 0)


if __name__ == '__main__':
    unittest.main()
