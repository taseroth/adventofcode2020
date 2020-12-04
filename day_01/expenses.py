# solution for day 1.
# direct loading from url does not work, as it requires login
# hence the expense file is downloaded and provided

def find_match(*argv):
    aggregate = 0
    product = 1
    for arg in argv:
        aggregate = aggregate + arg
        product = product * arg
    if aggregate == 2020:
        print(argv, ' add up to 2020, product is: ', product)
        return True
    return False


expenses = []
with open('expenses.txt', 'r') as expenses_file:
    for line in expenses_file:
        expenses.append(int(line))

number_expenses = len(expenses)
print('read ', number_expenses, ' expenses from file')

print('solving part 1 (finding 2 lines that add up to 2020)')
for i in range(number_expenses):
    for j in range(i + 1, number_expenses):
        if find_match(expenses[i], expenses[j]):
            break

print('solving part 2 (finding 3 lines that add up to 2020)')
for i in range(number_expenses):
    for j in range(i + 1, number_expenses):
        for k in range(j + 1, number_expenses):
            if find_match(expenses[i], expenses[j], expenses[k]):
                break
