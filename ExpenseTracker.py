# --- EXPENSE TRACKER (KİŞİSEL BÜTÇE TAKİP) ---

# Dosya adı sabiti (Verilerin kaydedileceği dosya)
FILE_NAME = "expenses.txt"

# 1. YÜKLEME FONKSİYONU (LOAD)
def load_expenses():
    """
    Program açıldığında dosyayı okur ve verileri bir listeye geri yükler.
    """
    expense_list = []
    try:
        # Dosyayı okuma modunda ('r') açıyoruz
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                # Dosyadaki satır şöyledir: "Market,2025-01-12,150\n"
                clean_line = line.strip()  # Satır sonundaki \n ve boşlukları temizle
                parts = clean_line.split(",") # Virgüllerden böl -> ["Market", "2025...", "150"]
                
                # Veriyi tekrar Sözlük (Dictionary) yapısına çeviriyoruz
                data = {
                    "category": parts[0],       # Kategori
                    "date": parts[1],           # Tarih
                    "amount": int(parts[2])     # Tutar (İşlem yapabilmek için sayıya çevir)
                }
                expense_list.append(data) # Listeye ekle
    except FileNotFoundError:
        # Eğer dosya yoksa (ilk kez çalışıyorsa), hata verme, boş liste döndür
        return []
        
    return expense_list

# 2. KAYDETME FONKSİYONU (SAVE)
def save_expenses(data_list):
    """
    Güncel listeyi dosyaya yazar (Eski verileri silip güncel halini yazar).
    """
    # Dosyayı yazma modunda ('w') açıyoruz
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for item in data_list:
            # Sözlüğü tekrar "Market,2025,150" formatına çevirip yazıyoruz
            line_to_write = f"{item['category']},{item['date']},{item['amount']}\n"
            file.write(line_to_write)

# --- ANA PROGRAM (MAIN PROGRAM) ---

# 1. Adım: Eski verileri yükle
monthly_expenses = load_expenses()

print("--- PERSONAL EXPENSE TRACKER (Kişisel Harcama Takibi) ---")

while True:
    # Kullanıcıya durumu ve menüyü göster
    print(f"\nTotal Records (Toplam Kayıt): {len(monthly_expenses)}")
    print("1) Add Expense (Ekle)")
    print("2) List & Delete (Listele ve Sil)")
    print("3) Exit (Çıkış)")
    
    choice = input("Select (Seçiminiz): ")

    # --- 1. EKLEME İŞLEMİ (ADD) ---
    if choice == "1":
        cat = input("Category (Kategori - örn: Market): ")
        date = input("Date (Tarih - örn: 2025-01-12): ")
        
        # Tutarı sayı olarak alıyoruz (Hata olmaması için try-except eklenebilir)
        try:
            amount = int(input("Amount (Tutar - Sayı): ")) 
            
            # Listeye sözlük olarak ekle
            monthly_expenses.append({"category": cat, "date": date, "amount": amount})
            
            # VE HEMEN KAYDET (Veri kaybını önlemek için)
            save_expenses(monthly_expenses)
            print(" Saved successfully. (Başarıyla kaydedildi)")
        except ValueError:
            print(" Error: Amount must be a number! (Hata: Tutar sayı olmalı)")

    # --- 2. LİSTELEME VE SİLME (LIST & DELETE) ---
    elif choice == "2":
        print("\n--- EXPENSE LIST ---")
        # enumerate fonksiyonu hem sıra numarasını (i) hem de veriyi verir
        for i, item in enumerate(monthly_expenses):
            print(f"{i}) {item['category']} - {item['amount']} TL ({item['date']})")
            
        sub_choice = input("\nEnter number to delete (Silinecek no girin, Menü için 'm'): ")
        
        if sub_choice != 'm':
            try:
                delete_index = int(sub_choice)
                
                # Girilen numara listenin sınırları içinde mi kontrol et
                if 0 <= delete_index < len(monthly_expenses):
                    removed_item = monthly_expenses.pop(delete_index) # Listeden sil
                    save_expenses(monthly_expenses) # Dosyayı güncelle!
                    print(f" Deleted: {removed_item['category']}")
                else:
                    print(" Invalid number! (Geçersiz numara)")
            except ValueError:
                print(" Please enter a number. (Lütfen sayı girin)")

    # --- 3. ÇIKIŞ (EXIT) ---
    elif choice == "3":
        print("Exiting... Data is safe. (Çıkılıyor, veriler güvende)")
        break # Döngüyü kır ve programı kapat
        
    else:
        print("Invalid choice, please try again. (Geçersiz seçim)")