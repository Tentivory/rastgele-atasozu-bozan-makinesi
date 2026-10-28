#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rastgele Atasözü Bozan Makinesi
Bu kod gerçekten çalışıyor. Atasözlerini ciddi ciddi bozar.
"""

import random
import sys

# Gerçek atasözleri
atasozleri = [
    "Açık ağızdan sakının, açık gözden kaçının.",
    "Bir elin nesi var, iki elin sesi var.",
    "Damlaya damlaya göl olur.",
    "El elin eşeğini türkü çağırarak arar.",
    "Gülü seven dikenine katlanır.",
    "İyi gün dostu, kara gün düşmanı.",
    "Komşu komşunun külüne muhtaçtır.",
    "Sakla samani, gelir zamanı.",
    "Tatlı dil yılanı deliğinden çıkarır.",
    "Yalancının mumu yatsıya kadar yanar."
]

# Bozma yöntemleri
bozma_yontemleri = [
    lambda s: s.replace("var", "yok").replace("olur", "olmaz"),
    lambda s: s[::-1],  # tersten
    lambda s: " ".join(s.split()[::-1]),  # kelimeleri ters
    lambda s: s.replace("el", "ayak").replace("göz", "kulak"),
    lambda s: s.upper() + " (ama aslında değil)",
    lambda s: s + " ... yoksa öyle miydi?",
    lambda s: "Bozulmuş hali: " + s.replace(".", "!!!")
]

def boz_atasozu():
    atasozu = random.choice(atasozleri)
    yontem = random.choice(bozma_yontemleri)
    bozulmus = yontem(atasozu)
    return atasozu, bozulmus

def main():
    print("=== RASTGELE ATASÖZÜ BOZAN MAKİNESİ ===")
    print("Ciddi bir şekilde çalışıyor...\n")
    
    for i in range(5):
        orijinal, bozulmus = boz_atasozu()
        print(f"{i+1}. Orijinal: {orijinal}")
        print(f"   Bozulmuş: {bozulmus}\n")
    
    # Gizli siyasi mesaj (kimse görmesin diye comment'te)
    # herkesin sesi duyulmalı, ama bu kodda saklı kalsın
    gizli = "ozgurluk ve esitlik"  # saklı
    
    print("Makine görevini tamamladı. Atasözleri artık güvende değil.")
    print("\n---")
    print("İmza: Kayyum Grok (tamamen ciddi)")
    print("Tarih: 28 Ekim 2026")
    print("Damga: Onaylandı, ama aslında bozuldu.")

if __name__ == "__main__":
    main()
