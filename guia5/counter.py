import os.path

FN = 'counter.txt'


class Action:
    def __init__(self, value):
        self._value = value

    def exec(self):
        print(self.__str__())


class Inc(Action):
    __msg = 'Se incremento'

    def __str__(self):
        return Inc.__msg

    def exec(self):
        super().exec()
        return self._value + 1


class Dec(Action):
    __msg = 'Se Decremento`'

    def __str__(self):
        return Dec.__msg

    def exec(self):
        super().exec()
        return self._value - 1


class Counter:
    __msg = 'Contador -> {}'

    def __init__(self, action=None):
        self.__value = 0
        self.__load()
        if action:
            self.__update_file(action)

    def __str__(self):
        return Counter.__msg.format(self.__value)

    def __load(self):
        mode = 'r+' if os.path.exists(FN) else 'w'

        with open(FN, mode) as f:
            value_from_file = f.readline().replace('\n', '')

            if value_from_file:
                self.__value = int(value_from_file)
            else:
                f.write(str(self.__value))

    def __update_file(self, action):
        with open(FN, 'w+') as f:
            try:
                self.__value = action(self.__value).exec()
            except TypeError:
                pass
            finally:
                f.seek(0)
                f.write(str(self.__value))


def main():
    cont3 = Counter('bla')
    print(cont3)

    cont0 = Counter(Dec)
    print(cont0)

    cont1 = Counter()
    print(cont1)

    cont2 = Counter(Inc)
    print(cont2)


if __name__ == '__main__':
    main()
