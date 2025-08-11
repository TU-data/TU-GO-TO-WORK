import sys
import webbrowser
import tkinter as tk
from tkinter import messagebox

# --- 설정 ---
LOGIN_URL = "https://tugether.daouoffice.com/login"
# ---

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
    메인 로직: 출근 확인창을 바로 표시합니다.
    """
    show_alert()

if __name__ == "__main__":
    main()
