#coding:utf-8

userInput = input("Enter a sequence of integers separete by white space : ")
sequence  = userInput.split(" ")

max_length = 1
current_length = 1

start_index = 0
max_start_index = 0

for i in range(1, len(sequence)) :
    if sequence[i] > sequence[i - 1] :
        current_length += 1

    else :

        if current_length > max_length :
            max_length = current_length
            max_start_index = start_index

        current_length = 1
        start_index = i

if current_length > max_length :

    max_length = current_length
    max_start_index = start_index

lics = sequence[max_start_index:max_start_index + max_length]

print("Longest Increasing Continuous Subsequence :", lics)

print("Length :", max_length)