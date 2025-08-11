# TU Go To Work

윈도우 시작 시 자동으로 출근 확인 알럿을 표시하는 프로그램입니다.

## 주요 기능

- 🚀 **자동 시작 프로그램 등록**: 윈도우 시작 시 자동 실행
- 🔔 **최상위 레이어 알럿**: 사용자 로그인 시 가장 상위에 알럿 표시
- 🌐 **그룹웨어 연동**: "예" 클릭 시 그룹웨어 로그인 페이지로 이동
- 💻 **윈도우 전용**: 윈도우 환경에 최적화

## 사용법

### 1. 프로그램 실행
- `TUGoToWork.exe`를 실행하면 자동으로 윈도우 시작 프로그램에 등록됩니다
- 이후 윈도우 로그인 시마다 자동으로 실행됩니다

### 2. 출근 확인
- 윈도우 로그인 후 자동으로 알럿이 표시됩니다
- "그룹웨어로 이동하여 출근을 처리하시겠습니까?" 메시지가 나타납니다

### 3. 선택 옵션
- **예**: 그룹웨어 로그인 페이지(`https://tugether.daouoffice.com/login`)로 이동
- **아니오**: 프로그램 종료

## 빌드 방법

### Windows에서 빌드
1. `build_windows.bat` 파일을 더블클릭하여 실행
2. 또는 명령 프롬프트에서 다음 명령 실행:
   ```bash
   pip install pyinstaller
   pyinstaller --onefile --windowed --name TUGoToWork auto_attendance.py
   ```

### 빌드 결과
- `dist/TUGoToWork.exe` 파일이 생성됩니다
- 이 파일을 윈도우 사용자에게 배포하면 됩니다

## 시스템 요구사항

- Windows 10/11
- Python 3.10 이상 (빌드 시에만 필요)
- PyInstaller (빌드 시에만 필요)

## 파일 구조

```
TU-go-to-work/
├── auto_attendance.py      # 메인 프로그램
├── register_account.py     # 계정 등록 (사용하지 않음)
├── build_windows.bat      # 윈도우 빌드 스크립트
├── pyproject.toml         # 프로젝트 설정
└── README.md              # 이 파일
```

## 주의사항

- 프로그램은 윈도우 시작 시 자동으로 실행됩니다
- 시작 프로그램 등록을 원하지 않는 경우 Windows 설정에서 "TUGoToWork" 항목을 제거할 수 있습니다
- 프로그램은 사용자 권한으로 실행되며 관리자 권한이 필요하지 않습니다

## 라이선스

이 프로젝트는 개인 사용 목적으로 제작되었습니다.
