def sum_big_num(num1, num2):
    reverse_num1 = num1[len(num1)::-1]
    reverse_num2 = num2[len(num2)::-1]

    total = 0
    list = []
    if len(reverse_num1) < len(reverse_num2):
        temp = reverse_num1
        reverse_num1 = reverse_num2
        reverse_num2 = temp

    num_of_zeros_tobe_added = reverse_num1[len(reverse_num2):]
    number_after_zeros_added = reverse_num2.ljust(
        len(num_of_zeros_tobe_added) + len(reverse_num2), '0')

    real_value1 = reverse_num1
    real_value2 = number_after_zeros_added

    total = 0
    carry = 0
    for i in range(len(real_value1)):
        total = int(real_value1[i]) + int(real_value2[i]) + carry
        if total < 10:
            carry = 0
            list.append(total)
        elif total >= 10:
            # if total < 10:
            #     carry = 0
            rem = total % 10
            to_list = total // 10
            list.append(rem)
            carry = to_list

    list.reverse()
    str_ints = [str(int) for int in list]
    print("".join(str_ints))


large_value1 = str(10 ** 1000)
large_value2 = str(10 ** 1000)

sum_big_num(large_value1, large_value2)
print("\n")
sum_big_num('123432343', '12323254532')
