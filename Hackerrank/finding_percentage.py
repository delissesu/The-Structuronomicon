if __name__ == "__main":
    m = int(input())
    student_score = {}
    
    for _ in range (m):
        name, *line = input().split()
        scores = list(map(float, line))
        
        student_score[name] = scores
        
    query_name = input()
    
    for key, value in student_score.items():
        if key == query_name:
            average = sum(value) / len(value)
            print(f"{average:.2f}")        