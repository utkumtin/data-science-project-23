import pytest
import pandas as pd
import numpy as np
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tasks.task_manager import *

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "monster_name": ["Griffin", "Leshen", "Drowner"],
        "region": ["Velen", "Novigrad", "Novigrad"],
        "kills": [5, 2, 10],
        "difficulty": ["Hard", "Medium", "Easy"],
        "reward": [300, 150, 80]
    })

def test_calculate_avg_reward(sample_df):
    assert calculate_avg_reward(sample_df) == pytest.approx((300 + 150 + 80)/3)

def test_kills_by_region(sample_df):
    result = kills_by_region(sample_df)
    assert result["Novigrad"] == 12
    assert result["Velen"] == 5

def test_encode_difficulty(sample_df):
    df = encode_difficulty(sample_df.copy())
    assert df["difficulty"].tolist() == [3, 2, 1]

def test_add_reward_per_kill(sample_df):
    df = add_reward_per_kill(sample_df.copy())
    assert "reward_per_kill" in df.columns
    assert df["reward_per_kill"].iloc[0] == 300/5

def test_filter_rare_monsters(sample_df):
    df = filter_rare_monsters(sample_df.copy(), threshold=3)
    assert set(df["monster_name"]) == {"Leshen"}

def test_get_most_dangerous_monster(sample_df):
    assert get_most_dangerous_monster(sample_df) == "Drowner"

def test_avg_reward_by_region(sample_df):
    result = avg_reward_by_region(sample_df)
    assert result["Novigrad"] == pytest.approx((150 + 80)/2)

def send_post_request(url: str, data: dict, headers: dict = None):
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # hata varsa exception fırlatır
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
    except Exception as err:
        print(f"Other error occurred: {err}")

class ResultCollector:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            if report.passed:
                self.passed += 1
            elif report.failed:
                self.failed += 1

def run_tests():
    collector = ResultCollector()
    pytest.main(["tests"], plugins=[collector])
    print(f"\nToplam Başarılı: {collector.passed}")
    print(f"Toplam Başarısız: {collector.failed}")
    
    user_score = (collector.passed / (collector.passed + collector.failed)) * 100
    print(round(user_score, 2))
    
    url = "https://edugen-backend-487d2168bc6c.herokuapp.com/projectLog/"
    payload = {
        "user_id": 34,
        "project_id": 266,
        "user_score": round(user_score, 2),
        "is_auto": False
    }
    headers = {
        "Content-Type": "application/json"
    }
    send_post_request(url, payload, headers)

if __name__ == "__main__":
    run_tests()