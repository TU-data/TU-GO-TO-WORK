@echo off
echo TU Go To Work - Windows 빌드 시작...
echo.

REM 가상환경 활성화 (있는 경우)
if exist ".venv\Scripts\activate.bat" (
    echo 가상환경 활성화 중...
    call .venv\Scripts\activate.bat
)

REM 필요한 패키지 설치
echo 필요한 패키지 설치 중...
pip install pyinstaller

REM PyInstaller로 빌드
echo.
echo PyInstaller로 빌드 중...
pyinstaller --onefile --windowed --name TUGoToWork auto_attendance.py

echo.
echo 빌드 완료!
echo 실행 파일 위치: dist\TUGoToWork.exe
echo.
pause
