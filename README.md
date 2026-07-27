# LinuxServerStudy

## Shell 사용법

### alias (별칭)

**현재 쉘 창에서** 단축 명령어를 생성함  
`alias ll="ls -la"`

영구적인 alias를 생성하려면:  
* `~/.bashrc` 파일 편집
* 마지막 줄에 alias 명령어 추가
* 현재 쉘에 즉시 적용하려면 `source ~/.bashrc` 실행

### 파이프와 리다이렉션

**"|" (파이프)**  
: 왼쪽 명령어의 출력을 오른쪽 명령어의 입력으로 넘겨줌.

**">"/"<" (리다이렉션)**  
: 명령어의 출력을 파일에 저장하거나(">"), 파일 내용을 명령어의 입력으로 넣어줌("<").

```bash
du -h * | sort -hr > script.txt
```

### 쉘 스크립트 파일

쉘 스크립트 명령어를 저장할 수 있는 파일.

```vim
" shelltest.sh

#!/bin/bash    " 사용할 쉘 지정

echo "this is shell test!"

```

**실행 방법**

- `sh shelltest.sh`
- `bash shelltest.sh`

## VIM 사용법

**VIM 설정**

```vim
" ~/.vimrc

syntax on
set tabstop=4
set shiftwidth=4
set smartindent    " 자동 들여쓰기
set cindent
```


**단축키:**

- `w`: 변경 사항 저장
- `q`: 종료
- `i`: 입력 모드 진입
- `!`: 강제 실행 (예: `q!`)
- `yny`: n줄 복사
- `pp`: 붙여넣기
- `dnd`: n줄 삭제 (및 잘라내기)

## 원격 서버 연결 방법

### 1. 포트 포워딩

1. 공유기 설정 페이지 열기 (IP 주소 입력)
2. "포트 포워딩" 메뉴 이동
3. 새 규칙 추가
4. 내부 IP 주소: 기기 IP 입력
5. 외부 포트 -> 내부 포트 설정

### 2. SSH 연결

**SSH(Secure Shell)**  
: 원격 컴퓨터를 안전하게 제어할 수 있는 프로토콜.

- PowerShell 명령어: `ssh -p [포트] [로그인 ID]@[공유기 IP]`
- PuTTY 이용 시: IP 주소, 포트 입력
