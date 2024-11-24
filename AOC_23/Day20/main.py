from MiscFiles.library import *

modules = dict()
receive_from = defaultdict(dict)

FLIP_FLOP = 1
CONJUNCTION = 2
ans = 0
for line in get_input(2023, 20).split("\n"):
    label, out = line.split(" -> ")
    typ = 0
    if label[0] == "%":
        typ = FLIP_FLOP
        label = label[1:]
    elif label[0] == "&":
        typ = CONJUNCTION
        label = label[1:]
    modules[label] = (typ, out.split(", "))
    for out_n in out.split(", "):
        receive_from[out_n][label] = False

lows = 0
highs = 0
flip_stat = defaultdict(lambda: False)
conj_stat = {lbl: {lbl_1: False for lbl_1 in receive_from[lbl]} for lbl in modules.keys()}
buttons = 0
high_buttons = defaultdict(int)
while buttons < 5000:
    buttons += 1
    q = deque()
    q.append(("broadcaster", False, "button"))
    while q:
        label, pulse, from_lbl = q.popleft()
        highs += pulse
        lows += not pulse
        if pulse:
            high_buttons[from_lbl] = buttons
        if label not in modules:
            continue
        typ, send_to = modules[label]
        if typ == 0:
            for elt in send_to:
                q.append((elt, pulse, label))
        elif typ == FLIP_FLOP:
            if pulse:
                continue
            flip_stat[label] = not flip_stat[label]
            for elt in send_to:
                q.append((elt, flip_stat[label], label))
        elif typ == CONJUNCTION:
            conj_stat[label][from_lbl] = pulse
            for elt in send_to:
                q.append((elt, not all(conj_stat[label].values()), label))
    if buttons == 1000:
        print("Part 1:", lows * highs)


ans = 1
for lbl in receive_from[list(receive_from["rx"])[0]]:
    ans *= high_buttons[lbl]
print("Part 2:", ans)