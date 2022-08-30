import shutil
with open("eski.txt", encoding='utf-8') as eskif:
    eski = eskif.readlines()
leneski = len(eski)
with open("yeni.txt", encoding='utf-8') as yenif:
    yeni = yenif.readlines()
lenyeni = len(yeni)
for gg in range(leneski):
    eski[gg] = eski[gg].strip()
for gg in range(lenyeni):
    yeni[gg] = yeni[gg].strip()
yenis = set(yeni)
eskis = set(eski)
yeniss = yenis.difference(eskis)
eskiss = eskis.difference(yenis)
print("Duyuru Listesinden Silinecek Kullanıcılar\n")
for qq in eskiss:
    print(f"{qq}")
print("\nDuyuru Listesine Eklenecek Kullanıcılar")
for qq in yeniss:
    print(f"{qq}")
Onay = input("Ekleme silme işlemlerini tamamladınız mı? E/H\n")
if Onay == "E" or Onay == "e":
    shutil.copyfile('eski.txt', 'eneski.txt')
    print("Eski Liste Yedeklendi.")
    shutil.copyfile('yeni.txt', 'eski.txt')
    print("Yeni Liste Eski Lisyete Kopyalandı.")
