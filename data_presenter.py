cupcake = open('CupcakeInvoices.csv')

# for items in cupcake :
#     print(items)

flavor = None
for items in cupcake :
    flavor = items.split(',')[2]
    print(flavor)

cupcake.seek(0,0)

price = 0
total_price = 0

for things in cupcake :
    price = int(things.split(',')[3])
    print(price)
    total_price = float(things.split(',')[4])
    print(total_price)
    total_price *= price
    print(total_price)

cupcake.close()


