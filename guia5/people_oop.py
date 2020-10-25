FILENAME = 'people.txt'
FILE_ENCODING = 'utf-8'
FIELDS = ['id', 'first_name', 'last_name', 'birthdate']
FIELD_SEP = ';'


class Person:
    __data_display = '{} {} nació el {}'

    def __init__(self, id='', first_name='', last_name='', birthdate=''):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate

    def __str__(self):
        return Person.__data_display.format(self.first_name,
                                            self.last_name,
                                            self.birthdate)


class TxtFileEntityMapping:
    def __init__(self, filename, fields, fsep, entity_cls):
        self.filename = filename
        self.fields = fields
        self.fsep = fsep
        self.entity_cls = entity_cls
        self.entities = []
        self.__generate_entities()

    def display(self):
        for entity in self.entities:
            print(entity)

    def __generate_entities(self):
        with open(self.filename, encoding=FILE_ENCODING) as f:
            for line in f:
                self.entities.append(self.__create_entity(line.strip()))

    def __create_entity(self, line):
        values = line.split(self.fsep)
        data = zip(self.fields, values)
        entity = self.entity_cls()
        for k, v in data:
            entity.__dict__[k] = v
        return entity


def main():
    personas = TxtFileEntityMapping(FILENAME, FIELDS, FIELD_SEP, Person)
    personas.display()


if __name__ == '__main__':
    main()
