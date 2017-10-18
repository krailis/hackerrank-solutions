k = int(input())
room_list = sorted(list(map(int, input().strip().split())))
room_set_a = set([room_list[i] for i in range(0, len(room_list), 2)])
room_set_b = set([room_list[i] for i in range(1, len(room_list), 2)])
print(list(room_set_a.symmetric_difference(room_set_b))[0])

