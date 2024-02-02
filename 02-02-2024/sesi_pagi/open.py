# f= open("demofile.txt")

baca_ya = open("demofile.txt", "r")


# print (baca_ya.readlines( ))  #-> read baca semua line, readliness jadi numpuk harus pake array

print (baca_ya.read( ))  #-> read baca semua line, readliness jadi numpuk harus pake array


# print ((baca_ya)[0])

# print (baca_ya[1])

baca_ya.close()
