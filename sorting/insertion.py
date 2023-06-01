import time
import random
def insertion_sort(nums):
    # Начнем со второго элемента, так как мы предполагаем, что первый элемент отсортирован
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # И сохранить ссылку на индекс предыдущего элемента
        j = i - 1
        # Переместить все элементы отсортированного сегмента вперед, если они больше, чем элемент для вставки
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Вставляем элемент
        nums[j + 1] = item_to_insert

