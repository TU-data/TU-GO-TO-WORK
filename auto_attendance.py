import sys
import webbrowser
import pymsgbox

# --- 설정 ---
LOGIN_URL = "https://tugether.daouoffice.com/login"
# ---

def show_alert():
    """
    메시지 박스를 화면에 표시합니다.
    """
    response = pymsgbox.confirm(
        text="그룹웨어로 이동하여 출근을 처리하시겠습니까?",
        title="출근 확인",
        buttons=["예", "아니오"]
    )

    if response == "예":
        webbrowser.open(LOGIN_URL)
    # If response is "아니오" or None (user closed dialog), program exits naturally

def main():
    """
    메인 로직: 출근 확인창을 바로 표시합니다.
    """
    show_alert()

if __name__ == "__main__":
    main()