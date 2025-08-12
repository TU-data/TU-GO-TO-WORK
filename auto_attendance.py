import sys
import os
import webbrowser
import pymsgbox
import winreg
import ctypes
from pathlib import Path

# --- 설정 ---
LOGIN_URL = "https://tugether.daouoffice.com/login"
APP_NAME = "TUGoToWork"
# ---

def is_admin():
    """관리자 권한으로 실행 중인지 확인"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def add_to_startup():
    """프로그램을 윈도우 시작프로그램에 등록"""
    try:
        # 현재 실행 파일 경로
        exe_path = sys.executable if getattr(sys, 'frozen', False) else sys.argv[0]
        exe_path = os.path.abspath(exe_path)
        
        # 시작프로그램 레지스트리 키
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        
        # 프로그램 등록
        winreg.SetValueEx(key, APP_NAME, 0, winreg.REG_SZ, exe_path)
        winreg.CloseKey(key)
        
        return True
    except Exception as e:
        print(f"시작프로그램 등록 실패: {e}")
        return False

def remove_from_startup():
    """프로그램을 윈도우 시작프로그램에서 제거"""
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        
        winreg.DeleteValue(key, APP_NAME)
        winreg.CloseKey(key)
        return True
    except Exception as e:
        print(f"시작프로그램 제거 실패: {e}")
        return False

def show_startup_question():
    """시작프로그램 등록 여부를 묻는 다이얼로그"""
    response = pymsgbox.confirm(
        text="윈도우 시작 시 자동으로 실행되도록 등록하시겠습니까?\n\n'예'를 선택하면 자동으로 시작프로그램에 등록됩니다.",
        title="자동 시작 등록",
        buttons=["예", "아니오"]
    )
    
    if response == "예":
        if add_to_startup():
            pymsgbox.alert(
                text="성공적으로 시작프로그램에 등록되었습니다!\n\n이제 윈도우를 재시작하면 자동으로 실행됩니다.",
                title="등록 완료",
                button="확인"
            )
        else:
            pymsgbox.alert(
                text="시작프로그램 등록에 실패했습니다.\n\n관리자 권한으로 실행해보세요.",
                title="등록 실패",
                button="확인"
            )

def show_attendance_question():
    """출근 확인 다이얼로그"""
    response = pymsgbox.confirm(
        text="그룹웨어로 이동하여 출근을 처리하시겠습니까?",
        title="출근 확인",
        buttons=["예", "아니오"]
    )

    if response == "예":
        # 웹사이트 열기
        webbrowser.open(LOGIN_URL)
        # 알럿은 자동으로 닫힘

def show_main_menu():
    """메인 메뉴 표시"""
    options = [
        "출근 확인하기",
        "시작프로그램에 등록",
        "시작프로그램에서 제거",
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
        elif choice == "시작프로그램에 등록":
            show_startup_question()
        elif choice == "시작프로그램에서 제거":
            if remove_from_startup():
                pymsgbox.alert(
                    text="시작프로그램에서 제거되었습니다.",
                    title="제거 완료",
                    button="확인"
                )
            else:
                pymsgbox.alert(
                    text="제거에 실패했습니다.",
                    title="제거 실패",
                    button="확인"
                )
        elif choice == "종료" or choice is None:
            break

def main():
    """메인 로직"""
    # 윈도우에서만 실행
    if sys.platform != "win32":
        print("이 프로그램은 Windows에서만 실행됩니다.")
        return
    
    # 첫 실행 시 시작프로그램 등록 여부 확인
    if not is_startup_registered():
        show_startup_question()
    
    # 메인 메뉴 표시
    show_main_menu()

def is_startup_registered():
    """시작프로그램에 등록되어 있는지 확인"""
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_READ
        )
        
        value, _ = winreg.QueryValueEx(key, APP_NAME)
        winreg.CloseKey(key)
        
        return value == sys.executable
    except:
        return False

if __name__ == "__main__":
    main()