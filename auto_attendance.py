import json
import os
import sys
import time
import webbrowser
import pymsgbox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# ✅ 실행 위치가 아니라, 스크립트/실행파일 위치를 기준으로 경로 설정
def get_base_dir():
    if getattr(sys, 'frozen', False):
        # PyInstaller로 빌드된 실행 파일의 경로
        return os.path.dirname(sys.executable)
    else:
        # Python으로 직접 실행하는 경우
        return os.path.dirname(__file__)

CONFIG_PATH = os.path.join(get_base_dir(), "config.json")
LOGIN_URL = "https://tugether.daouoffice.com/app/home"
ATTENDANCE_URL = "https://tugether.daouoffice.com/app/ehr"

def load_credentials():
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError("config.json 파일이 없습니다. 먼저 register_account.exe를 실행하세요.")
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
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

    # 로그인
    driver.find_element(By.ID, "username").send_keys(user_id)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login_submit").click()

    time.sleep(3)

    # 출근 메뉴 이동 및 클릭
    driver.get(ATTENDANCE_URL)
    time.sleep(2)
    driver.find_element(By.ID, "workIn").click()

    time.sleep(2)
    driver.quit()

def main():
    response = pymsgbox.confirm(
        "그룹웨어 출근을 하시겠습니까?",
        title="출근 체크",
        buttons=["예", "아니오"]
    )

    if response == "예":
        try:
            creds = load_credentials()
            run_bot(creds["id"], creds["pw"])

            result = pymsgbox.confirm(
                "그룹웨어 출근을 정상적으로 하였습니다.",
                title="출근 완료",
                buttons=["확인", "바로가기"]
            )
            if result == "바로가기":
                webbrowser.open(LOGIN_URL)
        except Exception as e:
            pymsgbox.alert(f"오류 발생: {e}", title="오류")
    else:
        pymsgbox.alert("출근 체크를 취소하였습니다.", title="취소")

if __name__ == "__main__":
    main()
