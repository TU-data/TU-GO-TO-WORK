import json
import os
import sys
import time
import webbrowser
import winreg
import ctypes
from ctypes import wintypes
import tkinter as tk
from tkinter import messagebox
import threading

# 윈도우 최상위 레이어 설정을 위한 상수
HWND_TOPMOST = -1
SWP_SHOWWINDOW = 0x0040
SWP_NOMOVE = 0x0002
SWP_NOSIZE = 0x0001

# ✅ 실행 위치가 아니라, 스크립트/실행파일 위치를 기준으로 경로 설정
def get_base_dir():
    if getattr(sys, 'frozen', False):
        # PyInstaller로 빌드된 실행 파일의 경로
        return os.path.dirname(sys.executable)
    else:
        # Python으로 직접 실행하는 경우
        return os.path.dirname(__file__)

CONFIG_PATH = os.path.join(get_base_dir(), "config.json")
LOGIN_URL = "https://tugether.daouoffice.com/login"

def is_admin():
    """관리자 권한 확인"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def add_to_startup():
    """윈도우 시작 프로그램에 등록"""
    try:
        # 현재 실행 파일 경로
        if getattr(sys, 'frozen', False):
            exe_path = sys.executable
        else:
            exe_path = os.path.abspath(__file__)
        
        # 레지스트리 키 열기
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        
        # 프로그램 등록
        winreg.SetValueEx(
            key,
            "TUGoToWork",
            0,
            winreg.REG_SZ,
            exe_path
        )
        
        winreg.CloseKey(key)
        return True
    except Exception as e:
        print(f"시작 프로그램 등록 실패: {e}")
        return False

def remove_from_startup():
    """윈도우 시작 프로그램에서 제거"""
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        
        winreg.DeleteValue(key, "TUGoToWork")
        winreg.CloseKey(key)
        return True
    except Exception as e:
        print(f"시작 프로그램 제거 실패: {e}")
        return False

def set_window_topmost(window):
    """윈도우를 최상위 레이어로 설정"""
    try:
        ctypes.windll.user32.SetWindowPos(
            window.winfo_id(),
            HWND_TOPMOST,
            0, 0, 0, 0,
            SWP_NOMOVE | SWP_NOSIZE | SWP_SHOWWINDOW
        )
    except:
        pass

def show_attendance_alert():
    """출근 확인 알럿 표시"""
    # 메인 윈도우 생성
    root = tk.Tk()
    root.title("출근 확인")
    root.geometry("400x200")
    root.resizable(False, False)
    
    # 윈도우를 최상위로 설정
    set_window_topmost(root)
    
    # 윈도우를 화면 중앙에 배치
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    # 메시지 라벨
    message_label = tk.Label(
        root, 
        text="그룹웨어로 이동하여 출근을 처리하시겠습니까?",
        font=("맑은 고딕", 12),
        wraplength=350,
        justify="center"
    )
    message_label.pack(pady=20)
    
    # 버튼 프레임
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)
    
    def on_yes():
        """예 버튼 클릭 시 그룹웨어 링크로 이동"""
        webbrowser.open(LOGIN_URL)
        root.destroy()
    
    def on_no():
        """아니오 버튼 클릭 시 프로그램 종료"""
        root.destroy()
        os._exit(0)
    
    # 버튼들
    yes_button = tk.Button(
        button_frame, 
        text="예", 
        command=on_yes,
        width=10,
        height=2,
        font=("맑은 고딕", 10)
    )
    yes_button.pack(side=tk.LEFT, padx=10)
    
    no_button = tk.Button(
        button_frame, 
        text="아니오", 
        command=on_no,
        width=10,
        height=2,
        font=("맑은 고딕", 10)
    )
    no_button.pack(side=tk.LEFT, padx=10)
    
    # 포커스를 예 버튼에 설정
    yes_button.focus_set()
    
    # Enter 키로 예 버튼 실행
    root.bind('<Return>', lambda e: on_yes())
    # Escape 키로 아니오 버튼 실행
    root.bind('<Escape>', lambda e: on_no())
    
    # 윈도우를 항상 최상위로 유지
    root.attributes('-topmost', True)
    
    # 메인 루프 실행
    root.mainloop()

def main():
    """메인 함수"""
    # 시작 프로그램에 등록 (최초 실행 시)
    if not os.path.exists(os.path.join(get_base_dir(), "startup_registered.txt")):
        if add_to_startup():
            # 등록 완료 표시
            with open(os.path.join(get_base_dir(), "startup_registered.txt"), "w") as f:
                f.write("registered")
            print("윈도우 시작 프로그램에 등록되었습니다.")
        else:
            print("윈도우 시작 프로그램 등록에 실패했습니다.")
    
    # 출근 확인 알럿 표시
    show_attendance_alert()

if __name__ == "__main__":
    main()
