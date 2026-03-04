#============================================
#Nama   : Muhammad Aditya Firmansyah
#NIM    : J0403251035
#Kelas  : B2
#============================================

#============================================
#Merge Sort dengan tracing
#============================================

def merge_sort(data,depth=0):
    indent = " " * depth #indentasi berdasarkan level rekursif
    print(f"{indent}merge_sort({data})")

    if len(data) <= 1:
        return data

    #Divide membagi data menjadi 2 bagian
    mid = len(data) // 2
    left = data[:mid] #slicing bagian kiri
    right = data[mid:] #slicing bagian kanan

    print(f"{indent}divide -> left = {left} | right = {right}")


    #8 ==> left 4  right 4
    #left 4 ==> mergesort ==> left 2 dan right 2 ==> mergesort

    #recursive call
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    merged = merge(left_sorted, right_sorted)
    print(f"{indent}merge -> {left_sorted} + {right_sorted} = {merged}")

    return merged

def merge(left, right):

    result = []
    i = 0
    j = 0

    #Membandingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    #Menambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])

    return result

angka = [1,4,8,9,2,0,5,6,8,9,5]
print("Hasil sorting: ", merge_sort(angka))