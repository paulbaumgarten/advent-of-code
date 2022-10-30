from pprint import pprint

def check_compliance(rules, message, rule_id):
    result = True
    for paths in rules[rule_id]:
        sub_paths = paths.split(" ")
        for sub_path in sub_paths:
            if sub_path.isnumeric():
                r = check_compliance(rules, message, int(sub_path))
                if not r:
                    result = False
                    break
            else:
                
    return result


def part1(rules, messages):
    count = 0
    for message in messages:
        r = check_compliance(rules, message, 0)
        if r:
            count += 1
    return count


## Main ##
with open("19-messages.txt") as f:
    messages = f.read().splitlines()
with open("19-rules.txt") as f:
    rules_list = f.read().splitlines()
    rules = {}
    for rule in rules_list:
        rule_id, rule_content = rule.split(": ")
        rule_content_list = rule_content.split(" | ")
        rules[int(rule_id)] = rule_content_list
#pprint(rules)
r = part1(rules, messages)
print(f"Part 1 result: {r}")