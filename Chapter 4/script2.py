s = 'spam'
print(len(s))

print(s[0], s[2], s[-1])

print(s*5)

# s[0] = 'z' is not possible however this is:
s = 'z' + s[1:]     # new object though
print(s)


s2 = 'shrubbery'
L = list(s2)                # Expand to a list: [...]
print(L)
L[1] = 'c'                  # Change it in place
print(''.join(L))           # join with empty delimiter

B = bytearray(b'spam')      # A bytes/list hybrid (ahead)
B.extend(b'eggs')           # 'b' needed in 3.X, not 2.X
print(B)                    # B[i] = ord(x) works here too
print(B.decode())           # Translate to normal string
