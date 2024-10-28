# Portofolio
**Data Structure Array And Tree**

**1. Structure Data Linier Array**

Array adalah kumpulan data yang memiliki tipe data yang sama dan diakses melalui indeks. Indeks setiap elemen dalam larik memiliki indeks yang unik, mulai dari 0.Operasi Array dapat menambah, menghapus, mengakses dan mengubah elemen.

**Fungsi Pencarian Linier :**
  1. Mengulangi larik secara berurutan.
  2. Membandingkan setiap elemen dengan target.
  3. Mengembalikan indeks jika ditemukan, jika tidak mengembalikan -1.
     
**Fungsi Pencarian Biner :**
  1.  Mengasumsikan larik sudah diurutkan.
  2.  Menggunakan pendekatan bagi-dan-taklukkan.
  3.  Membandingkan target dengan elemen tengah.
  4.  Menyesuaikan rentang pencarian berdasarkan perbandingan.
     
**Kelebihan:**
*	Akses cepat: Elemen array dapat diakses secara langsung dengan indeksnya, sehingga waktu akses sangat cepat.
*	Efisiensi memori: Array biasanya menggunakan memori secara berurutan, sehingga pengelolaan memori relatif sederhana.
*	Sederhana: Konsep array mudah dipahami dan diimplementasikan.
*	Operasi dasar efisien: Operasi seperti mencari, menambahkan, dan menghapus elemen pada posisi tertentu umumnya cukup efisien.

**Kekurangan:**
*	Ukuran tetap: Setelah dideklarasikan, ukuran array biasanya tidak dapat diubah secara dinamis. Jika ingin menambah atau menghapus elemen secara signifikan, seringkali diperlukan alokasi ulang memori.
*	Tipe data homogen: Semua elemen dalam array harus memiliki tipe data yang sama.
*	Tidak fleksibel untuk struktur data hierarkis: Array kurang cocok untuk merepresentasikan data yang memiliki hubungan hirarkis seperti pohon atau graf.

**Gunakan array jika:** 
  * Anda membutuhkan akses cepat ke elemen berdasarkan indeks.
  * Data Anda memiliki ukuran yang tetap dan tidak sering berubah.
  *	Anda tidak membutuhkan struktur data yang hierarkis.

**2. Structure Data Non Linier Tree**

Tree struktur data hierarkis yang terdiri dari node-node (simpul). Setiap node memiliki hubungan parent-child dengan node lainnya. Node paling atas disebut root, node yang tidak memiliki anak disebut leaf, dan node yang memiliki anak disebut internal node.
   
**Jenis-Jenis trees :**
1. Binary Tree: Setiap node maksimal memiliki dua anak (kiri dan kanan).
2. Binary Search Tree: Binary tree yang terurut, nilai anak kiri lebih kecil 
  dari parent, dan nilai anak kanan lebih besar dari parent.
3. Balanced Tree: tree di mana tinggi sub-pohon kiri dan kanan setiap node tidak berbeda terlalu jauh.
4. AVL Tree: Jenis binary search tree yang selalu seimbang.
5. Red-Black Tree: Jenis binary search tree yang juga selalu seimbang, menggunakan warna (merah atau hitam) untuk menjaga keseimbangan.

**Keuntungan Menggunakan tree:**
  * Representasi hierarki: Sangat baik untuk merepresentasikan data yang memiliki hubungan hierarkis (misal: struktur organisasi, file system).
  *	Pencarian efisien: Pohon biner pencarian memungkinkan pencarian data secara efisien.
  *	Fleksibel: Dapat digunakan untuk berbagai macam aplikasi.
  *	Mendukung banyak operasi: Penyisipan, penghapusan, pencarian, traversal.

**Kekurangan Menggunakan tree:**
  *	Memori: Membutuhkan lebih banyak memori dibandingkan array karena setiap node menyimpan pointer ke anak-anaknya.
  *	Kompleksitas implementasi: Implementasi pohon bisa lebih kompleks dibandingkan struktur data lain.
  *	Waktu operasi: Waktu operasi dapat bervariasi tergantung pada bentuk pohon dan operasi yang dilakukan. Pohon yang tidak seimbang dapat menyebabkan waktu operasi yang lambat.
    
**Pencarian biner :** 

*sebuah algoritma efisien untuk mencari suatu nilai dalam sebuah data yang telah terurut. Ketika diimplementasikan dalam struktur data pohon, metode ini disebut Binary Search Tree (BST).*

**Gunakan tree jika:** 
  *	Data Anda memiliki hubungan hierarkis.
  *	Anda sering melakukan operasi pencarian, penambahan, dan penghapusan.
  *	Anda membutuhkan struktur data yang fleksibel dan dapat tumbuh secara dinamis.

**Kesimpulan :**
Pilihan antara array dan tree tergantung pada sifat data yang akan disimpan dan operasi yang akan dilakukan. Tidak ada struktur data yang "paling baik" untuk semua kasus. Penting untuk memilih struktur data yang paling sesuai dengan kebutuhan spesifik masalah yang sedang Anda hadapi.
Faktor-faktor yang perlu dipertimbangkan:
  *	Ukuran data: Jika data Anda kecil dan statis, array mungkin lebih cocok. Jika data Anda besar dan dinamis, tree mungkin lebih baik.
  *	Jenis operasi: Jika Anda sering melakukan akses acak, array lebih efisien. Jika Anda sering melakukan pencarian, penambahan, dan penghapusan, tree mungkin lebih efisien.
  *	Hubungan antar data: Jika data Anda memiliki hubungan hierarkis, tree adalah pilihan yang lebih baik.




