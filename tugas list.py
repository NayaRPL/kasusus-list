# study kasus list
# buatlah satu program barang dengan ketentuan minimal barang tersebut :
#1.gunakan list untuk menampung barang yang diinput
#2. program dapat menambahkan barang 
#3.program dapat menghapus barang 
#4.program dapat mengedit barang 
#5.progam dapat menampilkan semua barang 
#6. program dapat mengetahui apakah berang sudah ada dalam list atau belum
# 7. program dapat menaplikan index barang tertentu
print(''' pilihan :
            1.apabila ingin menghapus barang 
          2.apabila ingin manambah barang 
          3.apabila ingin menggedit barang 
          4.ingin mengetahui apakah barang sudah ada dalam list atau blm
          5.ingin menampilkan index barang tertentu''')
jumlah_barang=int(input("masukkan jumlah barang :"))
list=[]
for i in range (jumlah_barang):
    barang=input("masukkan barang :")
    list.append(barang) 
    print(list)
nilai=int(input("masukkan pilihan anda : "))
if nilai == 1 :
    hapus=input("masukkan barang : ")
    barang=hapus
    list.remove(hapus)
    print(list)
elif nilai == 2:
    tambah=input("masukkan barang yang ingin di tambah :")
    list.append(tambah)
    print(list)
elif nilai == 3:
    input_index=int(input("masukkan index ke berapa yang ingin di rubah atau di edit:"))
    ganti_barang=input("masukkan nama barang yang ingin menggantikan :")
    list[input_index]= ganti_barang
    print(list)
elif nilai == 4:
    barang_yang_ingin_dicari=input("masukkan barang yang ingin di cari :")
    if barang_yang_ingin_dicari in list:
        print("barang ini tedapat dalam list")
    elif barang_yang_ingin_dicari not in list :
        print("barang ini tidak terdapat dalam list ")
elif nilai == 5:
    print(list)
    barang_yang_ingin_dicari = input("masukkan barang yang di cari :")
    print(barang_yang_ingin_dicari,"berada pada indeks",list.index(barang_yang_ingin_dicari))



    
    
    
    