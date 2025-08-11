import os
import sys
import webbrowser
import tkinter as tk
from tkinter import messagebox
import winshell
from win32com.client import Dispatch

# --- 설정 ---
APP_NAME = "TUGoToWork"
LOGIN_URL = "https://tugether.daouoffice.com/login"
# ---

def get_executable_path():
    """
    실행 파일의 경로를 반환합니다.
    PyInstaller로 빌드된 .exe 파일이거나, .py 스크립트일 수 있습니다.
    """
    if getattr(sys, 'frozen', False):
        return sys.executable
    else:
        return os.path.abspath(__file__)

def is_in_startup():
    """
    시작프로그램 폴더에 바로가기가 있는지 확인합니다.
    """
    startup_folder = winshell.startup()
    shortcut_path = os.path.join(startup_folder, f"{APP_NAME}.lnk")
    return os.path.exists(shortcut_path)

def add_to_startup():
    """
    시작프로그램 폴더에 현재 실행 파일에 대한 바로가기를 생성합니다.
    """
    if is_in_startup():
        return

    executable_path = get_executable_path()
    startup_folder = winshell.startup()
    shortcut_path = os.path.join(startup_folder, f"{APP_NAME}.lnk")

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = executable_path
    shortcut.WorkingDirectory = os.path.dirname(executable_path)
    shortcut.IconLocation = executable_path
    shortcut.save()

def show_alert():
    """
    메시지 박스를 화면에 표시합니다.
    """
    root = tk.Tk()
    root.withdraw()  # 메인 윈도우 숨기기
    root.attributes("-topmost", True)  # 다른 모든 창 위에 표시

    response = messagebox.askyesno(
        title="출근 처리 확인",
        message="그룹웨어로 이동하여 출근을 처리하시겠습니까?"
    )

    if response:
        webbrowser.open(LOGIN_URL)

    root.destroy()

def main():
    """
    메인 로직
    """
    # 프로그램이 시작프로그램에 등록되어 있지 않다면 등록합니다.
    # 사용자가 수동으로 실행했을 때 등록 절차가 진행됩니다.
    if not is_in_startup():
        try:
            add_to_startup()
            # 첫 등록 시 사용자에게 알림
            root = tk.Tk()
            root.withdraw()
            root.attributes("-topmost", True)
            messagebox.showinfo("등록 완료", "프로그램을 시작프로그램에 등록했습니다.\n이제 윈도우가 시작될 때마다 출근 알림을 받게 됩니다.")
            root.destroy()
            return # 첫 등록 후에는 바로 종료
        except Exception as e:
            # 권한 문제 등으로 실패 시 알림
            root = tk.Tk()
            root.withdraw()
            root.attributes("-topmost", True)
            messagebox.showerror("등록 실패", f"시작프로그램 등록에 실패했습니다.\n\n오류: {e}\n\n관리자 권한으로 다시 실행해 보세요.")
            root.destroy()
            return

    # 시작프로그램을 통해 실행되었을 때 알림창을 띄웁니다.
    show_alert()


if __name__ == "__main__":
    main()