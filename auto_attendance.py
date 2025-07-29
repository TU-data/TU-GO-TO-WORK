import json
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")
LOGIN_URL = "https://tugether.daouoffice.com/app/home"
ATTENDANCE_URL = "https://tugether.daouoffice.com/app/ehr"

def load_credentials():
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError("config.json 파일이 없습니다. 먼저 register_account.exe를 실행하세요.")
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def run_bot(user_id, password):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.get(LOGIN_URL)
    time.sleep(2)

    # 실제 로그인 input ID/class에 따라 수정 필요
    driver.find_element(By.ID, "username").send_keys(user_id)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "loginSubmit").click()

    time.sleep(3)

    # 출근 메뉴로 이동
    driver.get(ATTENDANCE_URL)

    # ↓ 출근 버튼 클릭 - 실제 element 구조에 맞게 수정 필요
    # driver.find_element(By.ID, "start_work_button").click()

    time.sleep(2)
    driver.quit()

if __name__ == "__main__":
    try:
        creds = load_credentials()
        run_bot(creds["id"], creds["pw"])
    except Exception as e:
        print("자동화 실행 중 오류 발생:", e)
