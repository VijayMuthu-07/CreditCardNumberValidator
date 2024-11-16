def card_num():
    number = input("Enter your credit card number: ")
    num_list=[]

    for i in number:
        if i.isdigit():
            num_list.append(int(i))
        elif i =="-" or i == " ":
            continue
        else:
            print("Invalid Credit Card Number")
    num_list = num_list[-1::-1]
    return num_list

def odd_sum(num):
    sum_odd = 0
    index = len(num) -1
    for i in range(0, index, 2):
        sum_odd += num[i]
    return sum_odd

def even_sum(num):
    sum_even = 0
    index = len(num) -1
    for i in range(1, index, 2):
        x = 2 * num[i]
        if x >= 10:
            y = 0
            x = str(x)
            for ele in x:
                y += int(x)
            sum_even += y
        else:
            sum_even += x
    return sum_even

def main():
    card_number = card_num()
    sum_odd = odd_sum(card_number)
    sum_even = even_sum(card_number)
    total_sum = sum_odd + sum_even
    if total_sum % 10 == 0:
        print("Valid Credit Card Number")
    else:
        print("Invalid Credit Card Number")

if __name__ == "__main__":
    main()