"""
The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:

byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789
Here are some invalid passports:

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
Here are some valid passports:

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?
"""

with open("04.txt", "r") as f:
    content = f.read().splitlines()
valid = 0
i = 0

def ishex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def check(info):
    if info.count(" byr:") == 1 and \
        info.count(" iyr:") == 1 and \
        info.count(" eyr:") == 1 and \
        info.count(" hgt") == 1 and \
        info.count(" hcl") == 1 and \
        info.count(" ecl") == 1 and \
        info.count(" pid") == 1:
        byr = info[ info.index(" byr:")+5 : ]
        iyr = info[ info.index(" iyr:")+5 : ]
        eyr = info[ info.index(" eyr:")+5 : ]
        hgt = info[ info.index(" hgt:")+5 : ]
        hcl = info[ info.index(" hcl:")+5 : ]
        ecl = info[ info.index(" ecl:")+5 : ]
        pid = info[ info.index(" pid:")+5 : ]
        byr = byr[ : byr.index(" ") ]
        iyr = iyr[ : iyr.index(" ") ]
        eyr = eyr[ : eyr.index(" ") ]
        hgt = hgt[ : hgt.index(" ") ]
        hcl = hcl[ : hcl.index(" ") ]
        ecl = ecl[ : ecl.index(" ") ]
        pid = pid[ : pid.index(" ") ]
        if not byr.isnumeric() or not iyr.isnumeric() or not eyr.isnumeric() or not pid.isnumeric():
            return False
        if int(byr) < 1920 or int(byr) > 2002 or int(iyr) < 2010 or int(iyr) > 2020 or int(eyr) < 2020 or int(eyr) > 2030:
            return False
        if len(pid) != 9:
            return False
        if ecl not in ('amb','blu','brn','gry','grn','hzl','oth'):
            return False
        if hcl[0] != "#":
            return False
        if not ishex("0x"+hcl[1:]):
            return False
        if hgt[-2:] == "cm" and hgt[:-2].isnumeric():
            val = int(hgt[:-2])
            if val < 150 or val > 193:
                return False
        elif hgt[-2:] == "in"  and hgt[:-2].isnumeric:
            val = int(hgt[:-2])
            if val < 59 or val > 76:
                return False
        else:
            return False
        return True
    else:
        return False

this_passport = ""
while i < len(content):
    if content[i] == "":
        if check(this_passport):
            valid +=1
        this_passport = ""
    else:
        this_passport += " " + content[i] + " "
    i += 1
if check(this_passport):
    valid +=1

print(valid)

