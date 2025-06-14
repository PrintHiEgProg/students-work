# 1. В последовательности на n целых чисел найти и вывести:
#    1. максимальный среди положительных
#    2. минимальный среди отрицательных
#    3. произведение элементов

def process_sequence(seq):
    positives = [x for x in seq if x > 0]
    negatives = [x for x in seq if x < 0]
    
    max_pos = max(positives) if positives else None
    min_neg = min(negatives) if negatives else None
    product = 1
    for num in seq:
        product *= num
    
    print(f"Максимальный среди положительных: {max_pos}")
    print(f"Минимальный среди отрицательных: {min_neg}")
    print(f"Произведение элементов: {product}")

sequence = [3, -2, 5, -1, 4, -5, 2]
print("Исходная последовательность:", sequence)
process_sequence(sequence)