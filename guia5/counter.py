import os.path
import sys

FN = 'counter.txt'


class Counter:
    __msg = 'Contador -> {}'
    __actions = {
        'inc': (1, 'Se incrementó'),
        'dec': (-1, 'Se decrementó')
    }

    def __init__(self):
        self.__value = 0
        self.__load()

    def display(self):
        print(Counter.__msg.format(self.__value))

    def update(self, arg):
        action = arg.lower()
        if action in Counter.__actions.keys():
            self.__value += Counter.__actions[action][0]
            print(Counter.__actions[action][1])
            self.__store()

    def __load(self):
        mode = 'r+' if os.path.exists(FN) else 'w'

        with open(FN, mode) as f:
            value_from_file = f.read().rstrip()

            if value_from_file:
                self.__value = int(value_from_file)
            else:
                f.write(str(self.__value))

    def __store(self):
        with open(FN, 'w+') as f:
            f.seek(0)
            f.write(str(self.__value))


def main():
    counter = Counter()

    if len(sys.argv) == 2:
        counter.update(sys.argv[1])

    counter.display()


if __name__ == '__main__':
    main()
