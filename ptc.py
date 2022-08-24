import math
import os
import random
import re
import sys
# Complete the 'gameOfThrones' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
def gameOfThrones(s):
    # Write your code here
    char_dic = {}
    for i in s:
        if i not in char_dic:
            char_dic[i] = s.count(i)
    odd_cont = 0
    for i in char_dic:
        if(char_dic[i]%2 == 1):
            odd_cont += 1
    if(odd_cont > 1):
        return 'NO'
    else:
        return 'YES'     
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = gameOfThrones(s)
    fptr.write(result + '\n')
    fptr.close()
