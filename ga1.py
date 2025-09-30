�������1
import random

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


arr = [random.randint(2, 103) for _ in range(random.randint(5, 25))]


print("������ �� ����������:", arr)
print("������ ����� ����������:", selection_sort(arr.copy()))

�������2
import random

def generate_random_array(size):
    return [random.randint(0, 100) for _ in range(size)]

def sort_reverse(arr):
    return sorted(arr, reverse=True)

def main():
    arr = generate_random_array(random.randint(5, 25))
    print("�� ����������:", arr)
    print("����� ����������:", sort_reverse(arr))

if __name__ == "__main__":
    main()

�������3
import random


def selection_sort_phones(phone_list):
    n = len(phone_list)
    temp = [(int(phone.replace("-", "")), phone) for phone in phone_list]

    for i in range(n - 1):
        min_pos = i
        for j in range(i + 1, n):
            if temp[j][0] < temp[min_pos][0]:
                min_pos = j
        temp[i], temp[min_pos] = temp[min_pos], temp[i]

    return [item[1] for item in temp]

def main():
    phone_list = [f"{random.randint(0, 99):02d}-{random.randint(0, 99):02d}-{random.randint(0, 99):02d}"
                  for _ in range(random.randint(5, 15))]
    
    
    print("������ ��������� �� ����������:", phone_list)
    sorted_list = selection_sort_phones(phone_list)
    print("������ ��������� ����� ����������:", sorted_list)

if __name__ == "__main__":
    main()
