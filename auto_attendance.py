import sys
import webbrowser
import pymsgbox

# --- 설정 ---
LOGIN_URL = "https://tugether.daouoffice.com/login"
# ---

def show_attendance_alert():
    """
    출근 확인 알럿을 표시하고, 링크 클릭 시 웹사이트를 열고 알럿을 닫습니다.
    """
    response = pymsgbox.confirm(
        text="그룹웨어로 이동하여 출근을 처리하시겠습니까?",
        title="출근 확인",
        buttons=["예", "아니오"]
    )

    if response == "예":
        # 웹사이트 열기
        webbrowser.open(LOGIN_URL)
        # 알럿 닫기 (자동으로 닫힘)

def main():
    """
    메인 로직: 출근 확인창을 바로 표시합니다.
    """
    show_attendance_alert()

if __name__ == "__main__":
    main()