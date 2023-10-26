#შექმენით სია, ამ სიაში ჩაწერეთ სხვადასხვა ციფრები (1, 2, 3, 4, ასე არა, რამე მაგ: 45, 23, 87, 55,) და გამოიტანეთ ამ სიაში ყველა რიცხვის ჯამი, ასევე ამავე სიიდან უნდა დაპრინტოთ ყველა რიცხვი ცალ ცალკე, და მიუწეროთ ლუწია თუ კენტი


my_arr = [15,23,9,15,33,3,57]
i = 0
while i < len(my_arr):
    print(my_arr[i] + my_arr[i])
    i += 1

my_arr = [15,23,9,15,33,3,57]
    
my_sum = 0
for num in my_arr:
    my_sum += num
print(my_sum)
        
my_arr = [15,23,9,15,33,3,57]
for num in my_arr:
    if num in my_arr:
        print(str(num) + " number is odd")
    else:

        print(str(num) + "number is even")