"""intervals"""
# Name 1: Swati Misra
# EID 1: SM83264
# Name 2: Sanjitha Venkata
# EID 2: sv28325


# Input: tuples_list is an unsorted list of interval tuples
# Output: A sorted and merged list of interval tuples, where
#         no interval in the merged list has any overlap.
def merge_tuples (tuples_list):
   """merge tuples"""
   output=tuples_list[:]




   #sort list of tuples first (make new list, do not use same one)
   n = len(output)
   for i in range(n - 1):
       # Find index of smallest remaining element
       index_smallest = i
       for j in range(i + 1, len(output)):
           if output[j][0] < output[index_smallest][0]:
               index_smallest = j
       # Swap nums[i] and nums[index_smallest]
       temp = output[i]
       output[i] = output[index_smallest]
       output[index_smallest] = temp




   outputlist= []
   for obj in output:
       outputlist+=list(obj)


   final_list = []
   len_output = len(outputlist)


   i = 0
   index = 0
   while i < len_output: #i is the index that we r on in final list
       if index < len_output: #index is the index we r on in output list
           #adds elements to final list
           final_list.append(outputlist[index])
           final_list.append(outputlist[index+1])
           while index < len_output:
           #if interval completely overlaps
               if outputlist[index] >= final_list[i] and outputlist[index+1] <= final_list[i+1]:
                   #dont add to list, move to next index
                   index += 2
               #if interval partially overlaps
               elif outputlist[index] >= final_list[i] and outputlist[index]<= final_list[i+1] \
                   and outputlist[index+1] > final_list[i+1]:
                   #change the lower bound of interval
                   final_list[i+1] = outputlist[index+1]
                   #move to next index
                   index += 2
               #move to the next itemz
               else:
                   #there are no more interval overlaps in output \
                   # list, add next element to final list
                   i += 2
                   break
       else:
           break
   #turns final list into list of tuples
   final_tuple_list = [(final_list[i],final_list[i+1]) for i in range(0,len(final_list)-1,2)]
   return final_tuple_list


# Input: tuples_list is a list of tuples of denoting intervals
# Output: A list of tuples sorted by ascending order of the size
#         of the interval. If two intervals have the size then it breaks
#         ties putting the interval with the lower starting number first
def sort_by_interval_size (tuples_list):
   """sort by size"""
   rangelist=[]
   len_tuples = len(tuples_list)
   for i in range(len_tuples):
       rangelist.append(tuples_list[i][1]-tuples_list[i][0])


   for i in range(1,len(tuples_list)):
       j=i
       while j > 0 and rangelist[j] < rangelist[j - 1]:
           temp = rangelist[j]
           rangelist[j]=rangelist[j-1]
           rangelist[j-1]=temp
           temp2 = tuples_list[j]
           tuples_list[j]=tuples_list[j-1]
           tuples_list[j-1]=temp2
           j=j-1
   return tuples_list




   #smth swati tried
   # tuples =tuples_list[:]
   # smallest_length = 0
   # smallest_index1 = 0
   # smallest_index2 = 0
   # small1 = 0
   # small2 = 0


   # final_list= []
   # for obj in tuples:
   #     final_list+=list(obj)


   # len_final = len(final_list)
   # for i in range(0, len_final, 2):
   #     smallest_length = final_list[i + 1] - final_list[i]
   #     small1 = final_list[i]
   #     small2 = final_list[i+1]
   #     for j in range(i + 2, len_final,2):
   #         if (final_list[j+1] - final_list[j]) < smallest_length:
   #             smallest_length = final_list[j+1] - final_list[j]
   #             small1 = final_list[j]
   #             small2 = final_list[j+1]
   #             smallest_index1 = j
   #             smallest_index2 = j + 1
   #         elif (final_list[j+1] - final_list[j]) == smallest_length:
   #             if final_list[j]<final_list[i]:
   #                 small1 = final_list[j]
   #                 small2 = final_list[j+1]
   #             else:
   #                 small1 = final_list[i]
   #                 small2 = final_list[i+1]
   #     temp1, temp2 = final_list[i], final_list[i+1]
   #     final_list[i] = small1
   #     final_list[i+1] = small2
   #     final_list[smallest_index1] = temp1
   #     final_list[smallest_index2] = temp2


   # final_tuple_list2 = [(final_list[i],final_list[i+1]) for i in range(0,len(final_list)-1,2)]
   # return final_tuple_list2




   #smth sanjitha tried
   # for x,y in tuples_list:
   #     lengthofrange=y-x
   #     for i in range(len(tuples_list)):
   #         for j in output:
   #             if len(output) == 0:
   #                 output.append((x,y))
   #             elif j<lengthofrange:
   #                 output.append((x,y))
   # return output








def main():
   """
   Uses input redirection to read the data and create a list of tuples
   """
   num_cases = int(input())
   tuples_list = []
   for i in range(num_cases):
       line = input()
       start, end = line.split()
       tuples_list.insert(i, (int(start), int(end)))


   # merge the list of tuples
   merged = merge_tuples(tuples_list)








   # sort the list of tuples according to the size of the interval
   sorted_merge = sort_by_interval_size(merge_tuples(tuples_list))








   # write the output list of tuples from the two functions
   print(merged)
   print(sorted_merge)








if __name__ == "__main__":
   main()


