from itertools import permutations
import re

def solution(expression):
    op = ["*", "+", "-"]
    
    op_orders = list(permutations(op,3))
    
    tokens =  re.split('([*+-])', expression)

    answer = 0
    
    for order in op_orders:
        temp_tokens = tokens[:]
        for operator in order:
            while operator in temp_tokens:
                idx = temp_tokens.index(operator)
                
                result = eval(str(temp_tokens[idx-1]) + operator + str(temp_tokens[idx+1]))
                
                temp_tokens = temp_tokens[:idx-1] + [result] + temp_tokens[idx+2:]
        answer = max(answer, abs(temp_tokens[0]))
    
    return answer