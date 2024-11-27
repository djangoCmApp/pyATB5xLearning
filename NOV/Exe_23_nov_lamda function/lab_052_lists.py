#list are mutable
amazon_fresh = ["Biscuits", "Rice", "Shampoo", "Conditioner", "Mixture"]
book_store = ["pen", "ink", "books", "colours"]
num_list = [1 , 2, 55, 67, 23, 56, 7, 54, 35, 8, 36]
print(amazon_fresh)
print(book_store)
# length
print(len(amazon_fresh))


# append, length increased after append a value
amazon_fresh.append("tooth brush")
print(len(amazon_fresh))

# insert
book_store.insert(1,'sheets')
print(book_store)

#remove or count
print(len(num_list))
num_list.remove(55)
print(num_list.count(55))
print(len(num_list))


for i in book_store:
    print(i)

book_store.sort()
amazon_fresh.sort()
num_list.sort()

print(book_store)
print(amazon_fresh)
print(num_list)