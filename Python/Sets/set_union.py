_ = int(input())
english = set(map(int, input().strip().split()))
_ = int(input())
french = set(map(int, input().strip().split()))
at_least_one = english.union(french)
print(len(at_least_one))