def fft(signal, offset=False):
    old_signal = signal.copy()
    start = offset if offset else 0
    partial_sum = None
    for i in range(start, len(signal)):
        if i > len(signal) / 2:
            if partial_sum is None:
                partial_sum = sum(signal[i:])
            t = partial_sum
            partial_sum -= signal[i]
            signal[i] = abs(t) % 10
            continue
        total = 0
        j = i
        neg = False
        while j < len(signal):
            if neg:
                total -= sum(old_signal[j:j+i+1])
            else:
                total += sum(old_signal[j:j+i+1])
            neg = not neg
            j += (i + 1) * 2
        signal[i] = abs(total) % 10
    return signal


signal = [int(x) for x in open("input").readline()]
for i in range(1, 101):
    signal = fft(signal)
print("Part 1:", ''.join([str(x) for x in signal[:8]]))

signal = [int(x) for x in open("input").readline()]*10000
offset = int(''.join([str(x) for x in signal[:7]]))
for i in range(100):
    signal = fft(signal, offset)
print("Part 2:", ''.join([str(x) for x in signal[offset:offset+8]]))
