amountOfStudents1 = int(input())
student1 = set(map(int, input().split()))
amountOfStudents2 = int(input())
student2 = set(map(int, input().split()))
union_set = student1.union(student2)
print(len(union_set))
