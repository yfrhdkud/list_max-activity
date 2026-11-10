def list_max(lst):
    if len(lst) == 0:
        return lst[0]
    rest = list_max(lst[1:])
    return lst[0] if lst[0] > rest else rest

#n = int(input("Enter a number(try 6 or 15): "))
lst = [72,4,9,2]
guess = int(input(f"What is the largest in {lst}?: "))
print(f"Largest: {list_max(lst)}")