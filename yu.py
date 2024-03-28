1.
def ans(num):
    n = len(nums)
    ans = num * 2
    return ans
nums = [1,2,3,4,5]
ans = ans(nums)
print(ans)

2.
def ans(nums):
    ans = [nums[num(i) for i in range(len(nums))]]
    return ans
nums = [0,2,1,5,3,4]
ans = ans(nums)
print(ans)

3.
def temperature_conversion(celsius):
    kelvin = round(celsius + 273.15, 5)
    fahrenheit = round(celsius * 1.8 + 32.0, 5)
    return [kelvin, fahrenheit]

celsius1 = 36.50
print(temperature_conversion(celsius1))

celsius2 = 122.11
print(temperature_conversion(celsius2))
