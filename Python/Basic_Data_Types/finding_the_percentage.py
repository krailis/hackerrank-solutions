if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        average = sum(scores)/3
        student_marks[name] = average
    query_name = raw_input()
    print(("%.2f")%(student_marks[query_name]))

