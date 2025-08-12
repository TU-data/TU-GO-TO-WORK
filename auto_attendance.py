import sys
import webbrowser
import pymsgbox
from pathlib import Path

# --- 설정 ---
LOGIN_URL = "https://tugether.daouoffice.com/login"
# ---

def show_attendance_question():
    """출근 확인 다이얼로그"""
    response = pymsgbox.confirm(
        text="그룹웨어로 이동하여 출근을 처리하시겠습니까?",
        title="출근 확인",
        buttons=["예", "아니오"]
    )

    if response == "예":
        try:
            webbrowser.open(LOGIN_URL)
            pymsgbox.alert(
                text="그룹웨어가 열렸습니다.\n출근 처리를 완료해주세요.",
                title="그룹웨어 열기 완료",
                button="확인"
            )
        except Exception as e:
            pymsgbox.alert(
                text=f"브라우저를 열 수 없습니다: {e}",
                title="오류",
                button="확인"
            )

def show_startup_guide():
    """시작프로그램 설정 안내"""
    guide_text = """윈도우 시작 시 자동으로 실행되도록 설정하는 방법:

1️⃣ 바로가기 만들기
   • TUGoToWork.exe 파일을 우클릭
   • "바로 가기 만들기" 선택

2️⃣ 시작프로그램 폴더 열기
   • Windows 키 + R 누르기
   • 'shell:startup' 입력 후 확인

3️⃣ 바로가기 이동
   • 만든 바로가기를 시작프로그램 폴더로 이동
   • 끌어다 놓기 또는 복사/붙여넣기

이제 윈도우를 재시작하면 자동으로 실행됩니다!"""
    
    pymsgbox.alert(
        text=guide_text,
        title="시작프로그램 설정 방법",
        button="확인"
    )

def show_main_menu():
    """메인 메뉴 표시"""
    options = [
        "출근 확인하기",
        "시작프로그램 설정 안내",
        "종료"
    ]
    
    while True:
        choice = pymsgbox.confirm(
            text="TU Go To Work 프로그램\n\n원하는 작업을 선택하세요:",
            title="메인 메뉴",
            buttons=options
        )
        
        if choice == "출근 확인하기":
            show_attendance_question()
        elif choice == "시작프로그램 설정 안내":
            show_startup_guide()
        elif choice == "종료" or choice is None:
            break

def main():
    """메인 로직"""
    # 메인 메뉴 표시
    show_main_menu()

if __name__ == "__main__":
    main()