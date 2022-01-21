"""
n number of studets' records
choose 1 student to query its values
get the average score
round to 2 decimals
print the output
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}  #Dictionary with key/value pairs
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg = (sum(student_marks.get(query_name))/(len(student_marks.get(query_name))))
    print(format(avg, ".2f"))