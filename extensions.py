f = input("File name: ").lower().lstrip().rstrip()

if f.count('.') >= 2 or f.count('.') == 0:
    print("application/octet-stream")

f = f.split('.')

if f[len(f)] == 'gif' or f[len(f)] == 'png':
    print(f"image/{f[len(f)]}")
elif f[len(f)] == 'jpg' or f[len(f)] == 'jpeg':
    print("image/jpeg")
elif f[len(f)] == 'pdf' or f[len(f)] == 'zip':
    print(f"application/{f[len(f)]}")
elif f[len(f)] == 'txt':
    print("text/plain")
else:
    print("application/octet-stream")
