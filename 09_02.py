puzzle: list[int] = []
with open('09.data') as file:
    for char in file.readline().strip():
        puzzle.append(int(char))

disk: list[int] = []
files: list[tuple[int, int, int]] = []  # start, len, value
spans: list[tuple[int, int]] = []  # start, len
curr = 0
for idx, block in enumerate(puzzle):
    disk.extend([0 if idx % 2 else idx // 2] * block)
    if not idx % 2:
        files.append((curr, block, idx // 2))
    elif block:
        spans.append((curr, block))
    curr = curr + block

for idx in range(len(files) - 1, -1, -1):
    file_start, file_len, file_value = files[idx]
    for span_idx, (span_start, span_len) in enumerate(spans):
        if span_start > file_start:
            break
        if span_len >= file_len:
            for span_pos, file_pos in zip(
                range(span_start, span_start + file_len),
                range(file_start, file_start + file_len)
            ):
                disk[span_pos], disk[file_pos] = disk[file_pos], disk[span_pos]
            spans.pop(span_idx)
            if span_len > file_len:
                spans.insert(
                    span_idx, (span_start + file_len, span_len - file_len))
            break

print(sum(idx * num for idx, num in enumerate(disk)))
