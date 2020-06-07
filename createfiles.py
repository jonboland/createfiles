import os


cwd = os.getcwd()
names = ("fivemb", "fiftymb", "fivehundredmb", "onegb", "twogb")
nums = (5, 50, 500, 1024, 2048)
multi = 1024 * 1024
sizes = [num * multi for num in nums]

for name, size in zip(names, sizes):
    with open(name, "wb") as out:
        out.seek(size - 1)
        out.write(b"0")
    filesize = os.stat(f"{cwd}\\{name}").st_size
    if name[-2:] == "mb":
        print(filesize / multi, "MB")
    else:
        print(filesize / (1024 * multi), "GB")
