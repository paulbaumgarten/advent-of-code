
"""
striped tan bags contain 2 light silver bags, 1 drab black bag, 2 clear tan bags, 2 mirrored tan bags.
dark black bags contain 1 vibrant indigo bag, 5 muted gold bags, 4 bright tomato bags, 3 dull tan bags.
dim silver bags contain 1 vibrant black bag, 3 muted cyan bags, 4 plaid turquoise bags, 4 faded orange bags.
faded maroon bags contain 3 pale aqua bags.
"""
class Bag:
    def __init__(self, rules):
        my_colour, can_contain = rules.split(" bags contain ")
        self.my_color = my_colour
        self.contains = {}
        inner_bags = can_contain.replace(" bags","").replace(" bag","").replace(".","").split(", ")
        #print(inner_bags)
        if inner_bags[0] != "no other":
            for inner_bag in inner_bags:
                qty = int(inner_bag[0])
                colour = inner_bag[2:]
                self.contains[colour] = qty
    
    def can_bag_contain(self, color):
        for k,v in self.contains.items():
            if k == color:
                return True
        return False
    
    def get_name(self):
        return self.my_color
    
    def __str__(self):
        o = f"Bag[{self.my_color}]\n"
        for k,v in self.contains.items():
            o += f"  - {k} ({v})\n"
        return o
    
    def __repr__(self):
        return f"Bag[{self.get_name()}]"

def get_available_bags_for(bags, my_bag, solution):
    for bag_obj in bags:
        if bag_obj.can_bag_contain(my_bag):
            #print(bag_obj)
            bag_name = bag_obj.get_name()
            if bag_name not in solution:
                solution.append(bag_name)
                get_available_bags_for(bags, bag_name, solution)

def get_inner_bags(bags, my_bag):
    total = 0
    my = bags[my_bag]
    if len(my.contains) == 0:
        print(f"{my_bag} has no other bags")
        return 0
    for k,v in my.contains.items():
        print(f"{my_bag} can have {v} of {k}")
        inner_bags = get_inner_bags(bags, k)
        total = total + v + v * inner_bags
    print(f"Total for {my_bag} is {total}")
    return total

# Read the file data
with open("07.txt", "r") as f:
    content = f.read().splitlines()
# Create all the bag objects
bags = []
for i in range(len(content)):
    bags.append(Bag(content[i]))
print(f"There are {len(bags)} types of bags available")
my_bag = "shiny gold"
solution = []
get_available_bags_for(bags, my_bag, solution)
# print(solution)
print(f"There are {len(solution)} types of bags that can ultimately contain a {my_bag} bag.")
# PART 2
bag_dict = {}
for b in bags:
    bag_dict[ b.get_name() ] = b
#print(bag_dict)
print("\n"*3)
#my_bag = "dark brown"
#my_bag = "light magenta"
total = get_inner_bags(bag_dict, my_bag)
print(total)

# 4166, 3701, 3700, 
# 4165 - is correct

"""
function get_bags_inside(me)
    get the list of bags my bag type contains
    if (my bag type contains no bags)
        return 0
    else
        // for every type of bag i contain
        for (each `sub_bag` i contain)
            // add the count of bags i contain
            total += sub_bag_qty
            // recuesive call: for a bag i contain, how many bags does it contain?
            sub_bag_sub_count = get_bags_insde( sub-bag )
            // add the count of bags contained by the bags i contain 
            total += (sub_bag_qty) * (sub_bag_sub_count)
        end-for
    end-if
end-function

total = get_bags_inside("shiny gold bag")
"""
