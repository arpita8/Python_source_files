def solution(a):
    sum_left, sum_right = 0, sum(a)
    for index,value in enumerate(a):
        sum_right -= value
        if sum_left == sum_right:
            yield index
        sum_left += value




print(list(solution([-1, 3, -4, 5, 1, -6, 2, 1])))        