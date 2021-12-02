import math


def rotate(img):
    if len(img) == 5:
        return img[3] + img[0] + "/" + img[4] + img[1]
    if len(img) == 11:
        return img[8] + img[4] + img[0] + "/" + img[9] + img[5] + img[1] + "/" + img[10] + img[6] + img[2]
    assert False


def flip(img):
    if len(img) == 5:
        return img[1] + img[0] + "/" + img[4] + img[3]
    if len(img) == 11:
        return img[2] + img[1] + img[0] + "/" + img[6] + img[5] + img[4] + "/" + img[10] + img[9] + img[8]
    assert False


def pos(img):
    ans = []
    for _ in range(4):
        ans.append(img)
        ans.append(flip(img))
        img = rotate(img)
    return ans


def breakup(img):
    length = img.index("/")
    rows = img.split("/")
    ans = []
    size = 2 if length % 2 == 0 else 3
    num = length // size
    for i in range(num):
        for j in range(num):
            new_img = rows[i * size][j * size:(j + 1) * size] + "/" + rows[i * size + 1][j * size:(j + 1) * size]
            if size == 3:
                new_img += "/" + rows[i * size + 2][j * size:(j + 1) * size]
            ans.append(new_img)
    return ans


def combine(imgs):
    length = int(math.sqrt(len(imgs)))
    imgs = [img.split("/") for img in imgs]
    ans = ""
    for r in range(length):
        for sub_r in range(len(imgs[0])):
            for c in range(length):
                ans += imgs[r * length + c][sub_r]
            ans += "/"
    return ans[:-1]


def step(img):
    global rules
    if len(img) in (5, 11):
        for p in pos(img):
            if p in rules:
                return rules[p]
        print("No matching rule")
        assert False
    new_imgs = breakup(img)
    for i in range(len(new_imgs)):
        new_imgs[i] = step(new_imgs[i])
    return combine(new_imgs)


rules = dict()

for line in open("input").readlines():
    line = line.strip().split(" => ")
    rules[line[0]] = line[1]

image = ".#./..#/###"
for i in range(18):
    image = step(image)
    if i == 4:
        print("Part 1:", image.count("#"))

print("Part 2:", image.count("#"))
