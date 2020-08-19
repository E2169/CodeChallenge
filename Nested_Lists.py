'''
Solution to the Hackerrank code challenge 'Nested_Lists'
'''
if __name__ == '__main__':
    n = int(input())
    grades = [[input(), float(input())] for _ in range(n)]
    second_lowest = sorted(list(set([score for name, score in grades])))[1]
    print('\n'.join([name for name,score in sorted(grades) if score == second_lowest])) 
