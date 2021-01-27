nums = list(range(1, 11))
print(nums)

for cube in nums:
    cube = cube**3
    print(cube)

cubed = [c**3 for c in nums]
print(cubed) 