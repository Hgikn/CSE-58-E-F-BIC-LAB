numbers = input().strip()
if not numbers:
    print(-1)
else:
    nums = list(map(int, numbers.split()))
    unique_nums = list(set(nums))

    if len(unique_nums) < 2:
        print(-1)
    else:
        unique_nums.sort(reverse=True)
        print(unique_nums[1])
