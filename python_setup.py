print("hello from inside a file!")

def hello():
    print("greetings user!")

hello()

def pack(x, y, z):
    return([x, y, z])

print(pack(1, 6, 7))

def eat_lunch(list):
    for i in range(0, len(list)):
        if i == 0:
            print("First I eat" + {list[0]})
        else:
            print("Next I eat" + {list[i]})

eat_lunch(["soup", "bread", "apple"])
