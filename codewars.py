def fake_bin(x):
    zmienna = ""
    for i in range(len(x)):
        if i < 5:
            print("0", end = "")
        else:
            print("1", end = "")
    return zmienna

print(fake_bin("215127"))