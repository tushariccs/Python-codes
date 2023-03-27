st = input("Enter a number: ")
st = st.split('0')
print(st)

for i in range(0, len(st)):
    st[i] = int(st[i])

print(st)
