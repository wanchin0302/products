products = []
while True:
    name = input("請輸入商品名稱: ")
    if name == "q":
        break	
    price = input("請輸入價格: ")
    price = int(price)
    products.append([name,price])
print(products)

for p in products: #for loop 搞清楚每個東西是什麼
	print(p)
	print(p[0], "的價格是", p[1])
