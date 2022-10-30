

def check_rule_2(target, numbers):
    for i in range(len(numbers)):
        print(f"i = {i}, numbers[i] = {numbers[i]}")
        for j in range(i+1, len(numbers)):
            total = sum(numbers[i:j])
            if total == target:
                print(numbers[i:j])
                return numbers[i:j]
            elif total > target:
                break

def check_rule_1(num, p25): # 31161678
    for i in range(len(p25)):
        for j in range(i, len(p25)):
            if p25[i] + p25[j] == num:
                return True
    return False

# Read the input data
with open("09.txt", "r") as f:
    content = f.read().splitlines()
# Convert to a list of integers
numbers = []
for item in content:
    numbers.append(int(item))
past25 = []
for num in numbers:
    if len(past25) < 25:
        past25.append(num)
    else:
        result = check_rule_1(num, past25)
        if not result:
            print(f"This number fails: {num}\nData: {past25}")
        # Update the preceding 25
        past25.append(num)
        if len(past25) > 25:
            past25.pop(0)
print("Starting rule 2...")
r = check_rule_2(31161678, numbers)
weakness = min(r) + max(r)
print(r)
print(sum(r))
print(f"Weakness is {weakness}")

