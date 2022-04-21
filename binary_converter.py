binary_list = []

def binary_convert(num):
    if num > 0:
        total = num // 2
        r = num % 2
        binary_list.append(r)
        num = total
        return binary_convert(num)

binary_convert(13)
sorted_binary = binary_list[::-1]
join_list = []
for i in sorted_binary:
    join_list.append(str(i))
binary_string = ''.join(join_list)
print(binary_string)

