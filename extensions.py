f = input("File name: ").lower().lstrip().rstrip()
c = f.count('.')
print(c)

if c > 1:
    print("application/octet-stream")

if f[2] == 'gif' or f[2] == 'jpg' or f[2] == 'jpeg' or f[2] == 'png':
    if f[2] == 'jpg' or f[2] == 'jpeg':
        print("image/jpeg")
    print(f"image/{f[2]}")
if f[2] == 'pdf' or f[2] == 'zip':
    print(f"application/{f[2]}")
if f[2] == 'txt':
    print("text/plain")

