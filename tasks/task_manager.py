
import pandas as pd
import numpy as np

# 1. Veri Okuma
def load_monster_data(filepath: str) -> pd.DataFrame:
    """
    Witcher Universe dünyasında canavar avı istatistiklerini içeren CSV dosyasını okur.
    
    Input:
        filepath (str): CSV dosyasının yolu. Örnek: "data/witcher_monsters.csv"
    
    Output:
        pd.DataFrame: Veri seti.
    
    Örnek:
        Input: "data/witcher_monsters.csv"
        Output: pandas.DataFrame (örnek kolonlar: ["monster_name", "region", "kills", "difficulty", "reward"])
    """
    pass


# 2. Eksik Değerleri Temizleme
def clean_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Eksik (NaN) değerleri temizler veya doldurur.
    - Sayısal kolonlar ortalama ile doldurulur.
    - Kategorik kolonlar "Unknown" ile doldurulur.
    
    Input:
        df (pd.DataFrame)
    Output:
        pd.DataFrame
    
    Örnek:
        Input: df = pd.DataFrame({"monster_name": ["Griffin", None], "kills": [3, None]})
        Output: pd.DataFrame({"monster_name": ["Griffin", "Unknown"], "kills": [3, 3]})
    """
    pass


# 3. Canavar Başına Ortalama Ödül
def calculate_avg_reward(df: pd.DataFrame) -> float:
    """
    Veri setindeki canavarların ortalama ödül miktarını hesaplar.
    
    Input:
        df (pd.DataFrame)
    Output:
        float (ortalama ödül miktarı)
    
    Örnek:
        Input: pd.DataFrame({"reward": [100, 200, 300]})
        Output: 200.0
    """
    pass


# 4. Bölgeye Göre Toplam Öldürme
def kills_by_region(df: pd.DataFrame) -> dict:
    """
    Bölgeler bazında toplam öldürme sayısını döndürür.
    
    Input:
        df (pd.DataFrame)
    Output:
        dict (örnek: {"Novigrad": 15, "Velen": 7})
    """
    pass


# 5. Zorluk Seviyesi Kodlama
def encode_difficulty(df: pd.DataFrame) -> pd.DataFrame:
    """
    "difficulty" kolonunu sayısal olarak kodlar.
    Örnek eşleme: {"Easy": 1, "Medium": 2, "Hard": 3, "Extreme": 4}
    
    Input:
        df (pd.DataFrame)
    Output:
        pd.DataFrame
    
    Örnek:
        Input: ["Easy", "Hard"]
        Output: [1, 3]
    """
    pass


# 6. Feature Engineering – Ödül/Kill Oranı
def add_reward_per_kill(df: pd.DataFrame) -> pd.DataFrame:
    """
    Yeni bir özellik (reward_per_kill) ekler:
    reward_per_kill = reward / kills
    
    Input:
        df (pd.DataFrame)
    Output:
        pd.DataFrame
    """
    pass


# 7. Nadir Canavarları Filtreleme
def filter_rare_monsters(df: pd.DataFrame, threshold: int) -> pd.DataFrame:
    """
    Öldürme sayısı 'threshold' değerinden az olan nadir canavarları döndürür.
    
    Input:
        df (pd.DataFrame), threshold (int)
    Output:
        pd.DataFrame
    
    Örnek:
        threshold=3 => kills<3
    """
    pass


# 8. Veri Standardizasyonu
def standardize_rewards(df: pd.DataFrame) -> pd.DataFrame:
    """
    reward kolonunu (x - mean) / std formülüyle standardize eder.
    
    Input:
        df (pd.DataFrame)
    Output:
        pd.DataFrame
    """
    pass


# 9. En Tehlikeli Canavar
def get_most_dangerous_monster(df: pd.DataFrame) -> str:
    """
    Kills değeri en yüksek olan canavarın adını döndürür.
    
    Input:
        df (pd.DataFrame)
    Output:
        str
    """
    pass


# 10. Eksploratif Özet
def eda_summary(df: pd.DataFrame) -> dict:
    """
    Veri setinin temel istatistiklerini özetleyen bir dict döndürür:
    - toplam canavar sayısı
    - toplam öldürme sayısı
    - ortalama ödül
    
    Input:
        df (pd.DataFrame)
    Output:
        dict
    """
    pass


# 11. Veri Normalizasyonu (0-1)
def normalize_kills(df: pd.DataFrame) -> pd.DataFrame:
    """
    kills kolonunu min-max normalizasyonu (0-1) ile normalize eder.
    
    Input:
        df (pd.DataFrame)
    Output:
        pd.DataFrame
    """
    pass


# 12. Bölgelere Göre Ortalama Ödül
def avg_reward_by_region(df: pd.DataFrame) -> dict:
    """
    Her bölge için ortalama ödülü hesaplar.
    
    Input:
        df (pd.DataFrame)
    Output:
        dict
    
    Örnek:
        {"Novigrad": 150.5, "Velen": 210.0}
    """
    pass