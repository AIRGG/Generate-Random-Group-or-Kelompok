import os, random, sys, time, datetime

#buka daftar nama orang orang
f = open("nama.txt", "r")
#tampung dulu
a = f.read().split("\n")
f.close()
#buat tampungan acak nanti
b = []
#buat tampungan sisa nama
c = []

def typeWriter(strNya, isi=False):
	print(strNya, end="")
	sys.stdout.flush()
	if isi:
		time.sleep(random.uniform(0.01, 0.05))
	else:
		time.sleep(random.uniform(0.05, 0.1))

banyak = int(input("Banyaknya Kelompok: "))
bagi = round(len(a)/banyak)
bagiFlt = float(len(a)/banyak)

os.system("cls")
bg = str(bagi).split(".")
isiTxt = "\n Banyak Kelompok: {}\n Perkelompok: {} Orang".format(banyak, bg[0])
print(isiTxt, end="")
# for x in isiTxt:
# 	typeWriter(x)
print("\n")
kel = 1
#baca daftar namanya
for x in range(len(a)):
	#ambil acak sama si python nya
	acak = random.choice(a)
	b.append(acak)
	a.remove(acak)
	# if len(a)+1 < bagi:
	#ambil sisa orang
	if bagiFlt % 1 != 0 and len(a)+1 < bagi:
		c.append(acak)
	#ambil orang dalam kelompok
	if len(b) == bagi:
		txtNya = " Kelompok {}:\n".format(kel)
		#langusng print
		# print(txtNya)
		#biar Typing
		for y in txtNya:
			typeWriter(y)
		#Sorting
		# b.sort()
		no=1
		#tampil orang orangnya
		for z in b:
			txx = " {}. {}".format(no, z)
			#langusng print
			# print(txx)
			#biar Typing
			for q in txx:
				typeWriter(q, True)
			print("")

			no+=1
		print("")
		kel+=1
		#hapus data di b
		b[:] = []

#ada sisa?, tampilkan!!
if len(c) != 0:
	no = 1
	print(" Sisa :")
	for x in c:
		txtt = " {}. {}".format(no, x)
		# langusng print
		# print(" {}. {}".format(no, x))
		#biar Typing
		for q in txtt:
			typeWriter(q, True)
		print("")

		no+=1
	print("")
for x in " Thanks... ":
	typeWriter(x, True)
print()