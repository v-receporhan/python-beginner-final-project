import random

def play_hangman():
    words1 = ["Python", "Java", "C", "C++", "JavaScript", "Go", "Ruby", "Swift", "Kotlin", "Rust"]
    words2 = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Kiwi", "Lemon"]
    words3 = ["Airplane", "Bus", "Train", "Car", "Motorcycle", "Boat", "Tram", "Helicopter", "Ferry", "Bicycle"]
    
    all_words = words1 + words2 + words3
    words = random.choice(all_words).lower() 

    choice_right = 6
    guessed_letters = set() # Set kullanıyoruz, doğru.

    # Bu mesajları döngüden dışarı aldım, yoksa her turda tekrar yazar.
    print("Welcome to hangman game. A random word will be given from one of the three categories")
    print("(programming language, fruit, transportation vehicle).")
    print("_ " * len(words))

    while choice_right > 0:
        # Durumu gösterelim
        display_word = " ".join([letter if letter in guessed_letters else "_" for letter in words])
        print(f"\nWord: {display_word}")
        print(f"Remaining tries: {choice_right}")

        # Giriş alma (Sadece 1 kere istiyoruz)
        person_choice = input("Please enter your guess: ").lower()

        # Hata Kontrolü
        if len(person_choice) != 1 or not person_choice.isalpha():
            print("Invalid choice, please enter a single letter.")
            continue
        
        # Tekrar Kontrolü
        if person_choice in guessed_letters:
            print(f"You already guessed '{person_choice.upper()}'. Try again.")
            continue 

        # Harfi kaydet (Set olduğu için .append değil .add kullanılır)
        guessed_letters.add(person_choice) 
        
        # Doğru mu Yanlış mı?
        if person_choice in words:
            print(f"Correct! {person_choice} is in the word.")
        else:
            choice_right -= 1
            print(f"Wrong guess! Remaining tries: {choice_right}")
        
        # Kazanma Kontrolü
        if all(l in guessed_letters for l in words):
            print(f"\nCONGRATULATIONS! You won! The word was: {words.upper()}")
            break
            
    # Kaybetme Kontrolü (While bittiğinde)
    if choice_right == 0:
        print(f"\nGame over! The word was: {words}")

# Oyunu Başlat
play_hangman()