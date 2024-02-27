from itertools import permutations

def generate_permutations(input_list):
    perms = permutations(input_list)
    perms_list = list(perms)
    return perms_list


input_list = [1, 2, 3]
permutations_list = generate_permutations(input_list)
print("All permutations of the list:", permutations_list)
