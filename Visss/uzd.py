# def split(list_a, chunk_size):

#   for i in range(0, len(list_a), chunk_size):
#     yield list_a[i:i + chunk_size]

# chunk_size = 3
# my_list = [1,2,3,4,5,6,7,8,9]
# print(list(split(my_list, chunk_size)))
karlis=[]
liene=[]
x=int(input('Karlis'))

while x!=0:
    karlis.append(x)
    x=int(input('Karlis'))
y=int(input('Liene'))

while y!=0:
    liene.append(y)
    y=int(input('Liene'))
print(karlis)
print(liene)
