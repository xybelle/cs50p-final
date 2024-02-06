f = input("File name: ").lower().lstrip().rstrip()

if f.count('.') >= 2 or f.count('.') == 0:
    print("application/octet-stream")

f = f.split('.')

if f[len(f) - 1] == 'gif' or f[len(f) - 1] == 'png':
    print(f"image/{f[len(f) - 1]}")
elif f[len(f) - 1] == 'jpg' or f[len(f) - 1] == 'jpeg':
    print("image/jpeg")
elif f[len(f) - 1] == 'pdf' or f[len(f) - 1] == 'zip':
    print(f"application/{f[len(f) - 1]}")
elif f[len(f) - 1] == 'txt':
    print("text/plain")
else:
    print("application/octet-stream")
