def multiple_3number(num_list):
    for i in range(len(num_list)):
        str_list = [str(x) for x in num_list[:i] + num_list[i+1:]]
        print(eval("*".join(str_list)))

num_list = [1,2,3,4]
multiple_3number(num_list)
