def shoppingList(cls, input1, input2, input3, inputa, inputs, input6):
    '''    
	input1 : int
	input2 : int
	input3 : int
	input4 : string[]
	Inputs : string[]
	input6 : string[]l
	Expected return type : string[]
    '''
	# Read only region endi
	# Wre code heroi
    all_items = input4 + input5 + input6
    item_counts = {}
    for item in all_items:
        item_counts[item] = item_counts.get(item, 0) + 1

    common_items = [item for item, count in item_counts.items() if count >= 2]

    if not common_items:
        return ["-1"]
    else:
        common_items.sort()
        return common_items

# Example 1:
input1_1 = 3
input2_1 = 4
input3_1 = 5
input4_1 = ["A", "B", "C"]
input5_1 = ["B", "C", "D", "E"]
input6_1 = ["B", "C", "D", "E", "F"]

output_1 = find_common_groceries(input1_1, input2_1, input3_1, input4_1, input5_1, input6_1)
print(output_1)  # Output: ['B', 'C', 'D', 'E']

# Example 2: No common items
input1_2 = 1
input2_2 = 1
input3_2 = 1
input4_2 = ["A"]
input5_2 = ["B"]
input6_2 = ["C"]

output_2 = find_common_groceries(input1_2, input2_2, input3_2, input4_2, input5_2, input6_2)
print(output_2) # Output: ['-1']
# 
# #Example 3: all lists are the same.
# input1_3 = 3
# input2_3 = 3
# input3_3 = 3
# input4_3 = ["A","B","C"]
# input5_3 = ["A","B","C"]
# input6_3 = ["A","B","C"]
# 
# output_3 = find_common_groceries(input1_3, input2_3, input3_3, input4_3, input5_3, input6_3)
# print(output_3) #output: ['A', 'B', 'C']
# 
# #Example 4: only two lists have common elements.
# input1_4 = 3
# input2_4 = 3
# input3_4 = 3
# input4_4 = ["A","B","C"]
# input5_4 = ["A","B","D"]
# input6_4 = ["E","F","G"]
# 
# output_4 = find_common_groceries(input1_4, input2_4, input3_4, input4_4, input5_4, input6_4)
# print(output_4) #output: ['A', 'B']