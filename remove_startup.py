import os
import winshell

# --- 설정 ---
APP_NAME = "TUGoToWork"
# ---

def remove_from_startup():
    """
    시작프로그램 폴더에서 바로가기를 삭제합니다.
    """
    try:
        startup_folder = winshell.startup()
        shortcut_path = os.path.join(startup_folder, f"{APP_NAME}.lnk")

        if os.path.exists(shortcut_path):
            os.remove(shortcut_path)
            print(f"성공: 시작프로그램에서 '{APP_NAME}.lnk'를 삭제했습니다.")
        else:
            print(f"정보: 시작프로그램에 '{APP_NAME}'이(가) 등록되어 있지 않습니다.")

    except Exception as e:
        print(f"오류: 시작프로그램에서 삭제하는 중 문제가 발생했습니다.")
        print(e)

if __name__ == "__main__":
    print(f"'{APP_NAME}'을(를) 시작프로그램에서 삭제합니다...")
    remove_from_startup()
    # 사용자가 결과를 확인할 수 있도록 잠시 대기
    input("\n작업을 완료했습니다. Enter 키를 눌러 창을 닫으세요...")