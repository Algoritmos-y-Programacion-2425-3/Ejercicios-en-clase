table = int(input("Please enter a table: "))
cont = 1
max_table = 10
print(f"************** TABLE of {table} **************")
while cont <= max_table:
    print(f"{table} x {cont} = {table*cont}")
    cont += 1