baca_ya = open("demofile.txt", "a+") #append
# baca_ya = open("demofile.txt", "w") #replace

baca_ya.write("\ndari pagi sampai sore") #append

baca_ya.close()

baca_ya = open("demofile.txt", "r")

print (baca_ya.read())


# print (baca_ya.readlines( ))  #-> read baca semua line, readliness jadi numpuk harus pake array

# print (baca_ya.read( ))  #-> read baca semua line, readliness jadi numpuk harus pake array


# print ((baca_ya)[0])

# print (baca_ya[1])

# baca_ya.close()
