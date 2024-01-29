students = {
            "Alice": {"id": "ID0001", "age":26, "grade":"A"}, # each key in this dict has it's own dictionary
            "Bob": {"id": "ID0002", "age":27, "grade":"B"},
            "Claire": {"id": "ID0003", "age":17, "grade":"C"},
            "Dan": {"id": "ID0004", "age":21, "grade":"D"},
            "Emma":{"id": "ID0005", "age":22, "grade":"E"}
            }

print(students["Dan"]["age"])

print(students["Emma"]["id"], students["Emma"]["grade"])

print(students["Claire"])

print(students["Bob"]["grade"])
