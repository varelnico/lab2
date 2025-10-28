# README - Praktikum Kondisional dan Perulangan

## Nama : Varel Nico Ramadhan
## Nim : 312510156

---

## LAB 2 – KONDISIONAL (IF)

### Latihan 1 – Bilangan terbesar dari 4 input

**Dengan cara:**

1. Minta pengguna memasukkan empat bilangan:

   ```python
   a = float(input("Masukkan bilangan 1: "))
   b = float(input("Masukkan bilangan 2: "))
   c = float(input("Masukkan bilangan 3: "))
   d = float(input("Masukkan bilangan 4: "))
   ```
2. Jadikan bilangan pertama sebagai nilai terbesar sementara:

   ```python
   maks = a
   ```
3. Bandingkan bilangan berikutnya satu per satu menggunakan `if`:

   ```python
   if b > maks: maks = b
   if c > maks: maks = c
   if d > maks: maks = d
   ```
4. Tampilkan hasil bilangan terbesar:

   ```python
   print("Bilangan terbesar adalah:", maks)
   ```

---

### Latihan 2 – Mengurutkan data (bubble sort)

**Dengan cara:**

1. Tentukan jumlah data yang akan diinput:

   ```python
   n = int(input("Jumlah data: "))
   ```
2. Buat list kosong untuk menampung nilai:

   ```python
   values = []
   ```
3. Masukkan data dengan perulangan `for`:

   ```python
   for i in range(n):
       values.append(float(input(f"Masukkan data ke-{i+1}: ")))
   ```
4. Gunakan perulangan bersarang untuk mengurutkan data:

   ```python
   for i in range(len(values)):
       for j in range(0, len(values)-1-i):
           if values[j] > values[j+1]:
               values[j], values[j+1] = values[j+1], values[j]
   ```
5. Cetak hasil data yang sudah terurut:

   ```python
   print("Data terurut:", values)
   ```

---

## LAB 2 – PERULANGAN

### Latihan 1 – Pola segitiga bintang

**Dengan cara:**

1. Masukkan tinggi pola:

   ```python
   n = int(input("Masukkan tinggi pola: "))
   ```
2. Gunakan perulangan `for` untuk mencetak baris:

   ```python
   for i in range(1, n+1):
       print("*" * i)
   ```

---

### Latihan 2 – Bilangan acak < 0.5

**Dengan cara:**

1. Import modul `random`:

   ```python
   import random
   ```
2. Minta jumlah angka acak yang ingin ditampilkan:

   ```python
   n = int(input("Jumlah angka acak (<0.5): "))
   ```
3. Gunakan perulangan `while` untuk menghasilkan angka acak:

   ```python
   count = 0
   while count < n:
       x = random.random()
       if x < 0.5:
           print(x)
           count += 1
   ```

---

### Latihan 3 – Mengurutkan input dengan perulangan

**Dengan cara:**

1. Input jumlah data:

   ```python
   n = int(input("Jumlah data: "))
   ```
2. Simpan setiap data ke list:

   ```python
   values = []
   for i in range(n):
       values.append(int(input(f"Masukkan data ke-{i+1}: ")))
   ```
3. Urutkan data dengan perulangan bersarang:

   ```python
   for i in range(len(values)):
       for j in range(0, len(values)-1-i):
           if values[j] > values[j+1]:
               values[j], values[j+1] = values[j+1], values[j]
   ```
4. Cetak hasil urutan:

   ```python
   print("Data urut:", values)
   ```

---

### Latihan 4 – Tabel perkalian

**Dengan cara:**

1. Masukkan batas angka:

   ```python
   n = int(input("Masukkan batas tabel: "))
   ```
2. Gunakan dua perulangan bersarang untuk menampilkan hasil perkalian:

   ```python
   for i in range(1, n+1):
       for j in range(1, n+1):
           print(f"{i*j:4}", end="")
       print()
   ```

---
