FILENAME = 'people.txt'
FILE_ENCODING = 'utf-8'
FIELDS = ['id', 'first_name', 'last_name', 'birthdate']
FIELD_SEP = ';'
PERSON_INFO_MSG = '{} {} nació el {}'


def create_person(line):
    values = line.split(FIELD_SEP)
    return dict(zip(FIELDS, values))


def display_person_info(person):
    print(PERSON_INFO_MSG.format(person[FIELDS[1]],
                                 person[FIELDS[2]],
                                 person[FIELDS[3]]))


def load_people():
    people = []
    with open(FILENAME, encoding=FILE_ENCODING) as f:
        for line in f:
            person = create_person(line.rstrip())
            people.append(person)
    return people


def main():
    people = load_people()
    for person in people:
        display_person_info(person)


if __name__ == '__main__':
    main()
