from statistics import mean

num_list = list()
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        value = float(num)
        num_list.append(value)
    except Exception:
        print("Please enter a real number!")

try:
    max_num = max(num_list)
    min_num = min(num_list)
    avr_num = mean(num_list)
    print(f"Biggest number: {max_num}, Smallest number: {min_num}, Average: {avr_num}")
except Exception:
    print("Error! Please be sure to put a number.")
