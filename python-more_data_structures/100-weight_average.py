#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weight_score = 0
    weight_sum = 0
    for score,weight in my_list:
        weight_score += weight * score
        weight_sum += weight
    result = weight_score / weight_sum
    return result
