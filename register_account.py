import json
import os
from tkinter import Tk, Label, Entry, Button, messagebox

CONFIG_PATH = "config.json"  # 수정된 경로 (현재 폴더에 저장)

def save_credentials(user_id, password):
    try:
        with open(CONFIG_PATH, "w") as f:
            json.dump({"id": user_id, "pw": password}, f)
    except Exception as e:
        messagebox.showerror("저장 실패", f"config.json 저장 중 오류 발생: {e}")

def on_submit():
    uid = entry_id.get()
    pw = entry_pw.get()
    if not uid or not pw:
        messagebox.showwarning("입력 오류", "아이디와 비밀번호를 모두 입력해주세요.")
        return
    save_credentials(uid, pw)
    messagebox.showinfo("저장 완료", "계정 정보가 저장되었습니다.")
    window.destroy()

# GUI
window = Tk()
window.title("계정 등록")
window.geometry("300x150")
window.resizable(False, False)

Label(window, text="아이디").pack()
entry_id = Entry(window)
entry_id.pack()

Label(window, text="비밀번호").pack()
entry_pw = Entry(window, show="*")
entry_pw.pack()

Button(window, text="저장", command=on_submit).pack(pady=10)

window.mainloop()
