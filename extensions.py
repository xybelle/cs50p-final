f = input("File name: ").lower().partition('.')

if f[2] == 'gif' or f[2] == 'jpg' or f[2] == 'jpeg' or f[2] == 'png':
    print(f"image/{f[2]}")
if f[2] == 'pdf' or f[2] == 'zip':
    print(f"application/{f[2]}")
if f[2] == 'txt':
    print(f"txt/{f[2]}")
