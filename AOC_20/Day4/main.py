import re

passport = {}
total_1 = total_2 = 0
for line in open("input").readlines():
    if line == "\n":
        if all([f in passport for f in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']]):
            total_1 += 1
            valid = True

            if not (1920 <= int(passport["byr"]) <= 2002):
                valid = False
            if not (2010 <= int(passport["iyr"]) <= 2020):
                valid = False
            if not (2020 <= int(passport["eyr"]) <= 2030):
                valid = False

            hgt = passport["hgt"]
            if hgt.endswith("cm"):
                if not (150 <= int(hgt[:-2]) <= 193):
                    valid = False
            elif hgt.endswith("in"):
                if not (59 <= int(hgt[:-2]) <= 76):
                    valid = False
            else:
                valid = False

            if re.match(r"#[0-9a-f]{6}$", passport["hcl"]) is None:
                valid = False

            ecl = passport["ecl"]
            if passport["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                valid = False

            if re.match(r"^[0-9]{9}$", passport["pid"]) is None:
                valid = False

            if valid:
                total_2 += 1
        passport = {}
    else:
        fields = line.strip().split()
        for field in fields:
            param, value = field.split(":")
            passport[param] = value

print(total_1)
print(total_2)

