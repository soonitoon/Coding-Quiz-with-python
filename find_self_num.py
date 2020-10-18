generated_list = []
count = 1

while True:
    if count < 10:
        result = count + count
        generated_list.append(result)
    else:
        result = eval("+".join(str(count))) + count
        if result >= 5000:
            break
        else:
            generated_list.append(result)
    count += 1

num_list = [x for x in range(1, 5000)]

print(sum(set(num_list) - set(generated_list)))