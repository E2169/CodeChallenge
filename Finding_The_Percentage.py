'''
This code is solution to the Hackerrank Finding the percentage challenge
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
# My code starts here
    my_list = student_marks[query_name]
    average = sum(my_list)/len(student_marks[query_name])
    print('%.2f' % average)

