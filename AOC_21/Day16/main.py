class Packet:
    def __init__(self, version, type):
        self.version = version
        self.type = type
        self.value = False
        self.children = []

    def add_child(self, packet):
        self.children.append(packet)

    def get_value(self):
        if self.type == 0:
            return sum(child.get_value() for child in self.children)
        elif self.type == 1:
            ans = 1
            for child in self.children:
                ans *= child.get_value()
            return ans
        elif self.type == 2:
            return min(child.get_value() for child in self.children)
        elif self.type == 3:
            return max(child.get_value() for child in self.children)
        elif self.type == 4:
            return self.value
        elif self.type == 5:
            return self.children[0].get_value() > self.children[1].get_value()
        elif self.type == 6:
            return self.children[0].get_value() < self.children[1].get_value()
        elif self.type == 7:
            return self.children[0].get_value() == self.children[1].get_value()

    def get_versions(self):
        return self.version + sum(child.get_versions() for child in self.children)


def decode_packet(packet, length, num):
    if (num is not None and num == 0) or (length is not None and length <= 0):
        return [], 0
    i = 6
    new_packet = Packet(int(packet[:3], 2), int(packet[3:6], 2))
    if new_packet.type == 4:
        bin_string = ""
        while bin_string == "" or packet[i - 5] == "1":
            bin_string += packet[i + 1:i + 5]
            i += 5
        new_packet.value = int(bin_string, 2)
    else:
        if packet[i] == "0":
            ans, di = decode_packet(packet[i + 16:], int(packet[i + 1:i + 16], 2), None)
            i += 16
        else:
            ans, di = decode_packet(packet[i + 12:], None, int(packet[i + 1:i + 12], 2))
            i += 12
        new_packet.children = ans
        i += di
    if length is not None or num is not None:
        ans2, di = decode_packet(packet[i:], length - i, None) if length is not None else \
                   decode_packet(packet[i:], None, num - 1)
        return [new_packet] + ans2, i + di
    return [new_packet], i


inp = [bin(int(d, 16))[2:] for d in open("input").readline()]
bin_string = ''.join([''.join(["0"] * (4 - len(bin_string)) + list(bin_string)) for bin_string in inp])
packet = decode_packet(bin_string, None, None)[0][0]
print("Part 1:", packet.get_versions())
print("Part 2:", packet.get_value())
