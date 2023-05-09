class Node:
    def __init__(self, vl, prev):
        self.vl = vl
        self.prev = prev
        self.next = None


def run(p1):
    nums = list(map(int, open("input").read().strip().split("\n")))
    if not p1:
        nums = [x * 811589153 for x in nums]
    nodes = [Node(nums[0], None)]
    for num in nums[1:]:
        next_node = Node(num, nodes[-1])
        nodes[-1].next = next_node
        nodes.append(next_node)
    nodes[-1].next = nodes[0]
    nodes[0].prev = nodes[-1]

    for _ in range(1 if p1 else 10):
        for n in nodes:
            n.prev.next = n.next
            n.next.prev = n.prev
            vl_to_move = n.vl % (len(nodes) - 1)
            for _ in range(vl_to_move):
                n.next = n.next.next
            n.prev = n.next.prev
            n.prev.next = n
            n.next.prev = n

    ans = 0
    for n in nodes:
        if n.vl == 0:
            ptr = n
            for _ in range(3):
                for _ in range(1000):
                    ptr = ptr.next
                ans += ptr.vl
            return ans


print("Part 1:", run(True))
print("Part 2:", run(False))
