print(f"\n\n{'A':<4}{'B':<3}{'|':<3}{'& and':<4}")
print("-" * 11)
for a, b in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    q = a & b
    print(f"{a:<4}{b:<3}{'|':<3}{q:<4}")

print(f"\n\n{'A':<4}{'B':<3}{'|':<3}{'| or':<4}")
print("-" * 11)
for a, b in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    q = a | b
    print(f"{a:<4}{b:<3}{'|':<3}{q:<4}")

print(f"\n\n{'A':<4}{'B':<3}{'|':<3}{'^ xor':<4}")
print("-" * 11)
for a, b in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    q = a ^ b
    print(f"{a:<4}{b:<3}{'|':<3}{q:<4}")



def displayRow(val, msb, label=""):
    for i in range(msb, -1, -1):
        bit = (val >> i) & 1
        print(f"{bit:<6}", end='')
    print(label)

msb = 9
n = 1000
mask = 0x0f0

print()
for i in range(msb, -1, -1):
    print(f"2^{i:<4}", end='')
print()

for i in range(msb, -1, -1):
    print(f"{2**i:<6}", end='')
print()

displayRow(n, msb, "data")
displayRow(mask, msb, "mask")
result = ~n
displayRow(result, msb, "not")
result = n & mask
displayRow(result, msb, "and")
result = n | mask
displayRow(result, msb, "or")
result = n ^ mask
displayRow(result, msb, "xor")
result = n<<3
displayRow(result, msb, "left shift 3")
result = n>>3
displayRow(result, msb, "right shift 3")
