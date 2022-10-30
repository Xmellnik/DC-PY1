def delete(list_, index=None):
   if index is None:  # None по умолчанию
       list_ = list_[:-1]
   else:
       left_part = list_[:index]  # часть слева до индекса не включая его
       right_part = list_[index + 1:]  # часть справа, уже без удаляемого значения
       list_ = left_part + right_part
   return list_

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
