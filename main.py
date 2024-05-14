#1
# a = int(input("Enter the number you want to remove: "))
# b = {1,2,3,4,5,6,12,24}
# b.remove(a)
# print(b)

#2
# a = (input("What do you want to add? "))
# b = {1,2,3,'Apple','John'}
# b.add(a)
# print(b)

#3
# a = {1,2,3,4}
# b = {'Gosht', 'Timur', 'Baloon'}
# a.update(b)
# print(a)

#4

c = {'Uzbekistan', 'Russia', 'Germany'}
while True:
    def main():
        user = input("Write 1 - add or 0 - delete: ")
        def add():
            a = input("Add new country: ")
            c.add(a)
            print(c)

        def delete():
            b = input("Delete country: ")
            c.remove(b)
            print(c)
        if user == '1':
            add()
        elif user == '0':
            delete()
        else:
            print("Go fuck your self, are you serious")
    main()




