import re

def solution(new_id):

    # 1.
    new_id = new_id.lower()

    # 2.
    findall = re.findall('\.|[0-9]+|[a-z]+|\-|\_', new_id)
    new_id = "".join(findall)

    # 3.
    new_id = re.sub("\.+", ".", new_id)

    while True:
        # 4.
        while new_id and new_id[0] == '.':
            new_id = new_id[1:]
        while new_id and new_id[-1] == '.':
            new_id = new_id[:-1]

        # 5.
        if not new_id:
            new_id = "a"

        # 6.
        if len(new_id) >= 16:
            new_id = new_id[0:15]
        # 7.
        elif len(new_id) <= 2:
            while len(new_id) < 3:
                new_id += new_id[-1]

        if len(new_id) >= 3 and new_id[0] != '.' and new_id[-1] != '.':
            return new_id

    return new_id