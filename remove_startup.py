import winreg
import os
import sys

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
        
        # 등록 완료 표시 파일도 제거
        base_dir = get_base_dir()
        startup_file = os.path.join(base_dir, "startup_registered.txt")
        if os.path.exists(startup_file):
            os.remove(startup_file)
        
        print("윈도우 시작 프로그램에서 제거되었습니다.")
        return True
    except Exception as e:
        print(f"시작 프로그램 제거 실패: {e}")
        return False

def get_base_dir():
    """기본 디렉토리 경로 반환"""
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(__file__)

if __name__ == "__main__":
    print("TU Go To Work - 시작 프로그램 제거")
    print("=" * 40)
    
    response = input("시작 프로그램에서 제거하시겠습니까? (y/n): ")
    if response.lower() in ['y', 'yes', '예']:
        remove_from_startup()
    else:
        print("취소되었습니다.")
    
    input("Enter를 누르면 종료됩니다...")
