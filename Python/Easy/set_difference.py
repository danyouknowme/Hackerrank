s1 = int(input())
student1 = set(map(int, input().split()))
s2 = int(input())
student2 = set(map(int, input().split()))
diff_set = student1.difference(student2)
print(len(diff_set))
