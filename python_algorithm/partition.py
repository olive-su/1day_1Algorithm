def swap_elements(my_list, index1, index2):
   tmp = my_list[index1]
   my_list[index1] = my_list[index2]
   my_list[index2] = tmp
   return my_list


def partition(my_list, start, end):
   p = end
   b = start
   for i in range(start, end):
      if my_list[i] <= my_list[p]:
         swap_elements(my_list, b, i)
         b += 1
   swap_elements(my_list, b, p)
   p = b
   return p


list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)
