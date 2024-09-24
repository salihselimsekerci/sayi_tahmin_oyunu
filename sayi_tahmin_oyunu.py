# -*- coding: utf-8 -*-
import random

class RandomNumberGenerator:
    """Rastgele bir sayı üreten sınıf. Bu sınıf, bağımlılık enjeksiyonu için kullanılabilir."""
    
    def generate(self, start: int, end: int) -> int:
        """start ve end parametreleri arasında rastgele bir sayı üretir."""
        return random.randint(start, end)

class UserInput:
    """Kullanıcıdan veri almayı yöneten sınıf."""
    
    def get_input(self, prompt: str) -> int:
        """Kullanıcıdan bir tahmin alır ve int olarak döner."""
        try:
            return int(input(prompt))
        except ValueError:
            raise ValueError("Geçersiz giriş! Lütfen bir sayı girin.")

class GameEngine:
    """Oyun motoru sınıfı. Oyun mekaniklerini ve işleyişi yönetir."""
    
    def __init__(self, number_generator: RandomNumberGenerator, user_input: UserInput, max_attempts: int = 10):
        self.number_generator = number_generator
        self.user_input = user_input
        self.max_attempts = max_attempts
        self.secret_number = None
        self.attempts_left = max_attempts

    def start(self):
        """Oyunu başlatır ve ana döngüyü yönetir."""
        print("Sayı Tahmin Etme Oyununa Hoşgeldiniz!")
        self.secret_number = self.number_generator.generate(1, 100)
        print("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misiniz?")

        while self.attempts_left > 0:
            try:
                guess = self.user_input.get_input(f"Kalan tahmin hakkınız {self.attempts_left}. Tahmininiz nedir?: ")
                self.check_guess(guess)
            except ValueError as ve:
                print(ve)

    def check_guess(self, guess: int):
        """Tahminin doğru olup olmadığını kontrol eder ve geri bildirim verir."""
        if guess == self.secret_number:
            print("Tebrikler! Doğru tahmin ettiniz!")
            self.attempts_left = 0  # Oyun biter
        elif guess < self.secret_number:
            print("Daha büyük bir sayı girin.")
            self.attempts_left -= 1
        else:
            print("Daha küçük bir sayı girin.")
            self.attempts_left -= 1

        if self.attempts_left == 0 and guess != self.secret_number:
            print(f"Üzgünüm, tahmin hakkınız bitti. Tuttuğum sayı {self.secret_number} idi.")

if __name__ == "__main__":
    # Bağımlılıkları oluşturalım ve oyunu başlatalım
    random_generator = RandomNumberGenerator()
    user_input = UserInput()
    game = GameEngine(random_generator, user_input)
    game.start()
