# coding:utf-8
# @Time : 2021/6/10 19:54 
# @Author : lxd
# @File : 动态规划.py
# @Software: PyCharm
# @E-mail: 1355087842@qq.com

# 动态规划

def get_max_sub(num_list):
    max_score = num_list[0]
    max_score_i = [num_list[0], num_list[0]]
    for num in num_list[1:]:
        max_score_i[1] = max(num + max_score_i[0], num)
        max_score = max(max_score, max_score_i[1])
        max_score_i[0] = max_score_i[1]
    return max_score


if __name__ == '__main__':
    # pass
    result = get_max_sub([1,2,-3,4,5,-6,7,8,9])
    result = get_max_sub([-2,1,-3,4,-1,2,1,-5,4])
    print(result)