# LinuxServerStudy

## Shell 사용법

### alias (별칭)

**현재 쉘 창에서** 단축 명령어를 생성함  
`alias ll="ls -la"`

영구적인 alias를 생성하려면:  
- `~/.bashrc` 파일 편집
- 마지막 줄에 alias 명령어 추가
- 현재 쉘에 즉시 적용하려면 `source ~/.bashrc` 실행

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

## Python venv 가상환경 설정하기

Python 모듈의 버전 관리를 위해 가상환경을 만들어 사용한다.
```python
# 가상환경 만들기
python -m venv (환경이름)

# 가상환경 적용하기
source (환경이름)/bin/activate
```

## Docker를 통해 Influx DB 설치하기

### Docker 설치하기

1. Docker 설치에 필요한 패키지 설치

```bash
sudo apt install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

2. Docker 공식 GPG 키 추가

```bash
sudo install -m 0755 -d /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

3. Docker 저장소 추가

```
sudo install -m 0755 -d /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

4. Docker Engine 설치

```bash
sudo apt update

sudo apt install -y \
docker-ce \
docker-ce-cli \
containerd.io \
docker-buildx-plugin \
docker-compose-plugin
```

5. Docker 서비스 시작 및 자동 시작 설정

```bash
sudo systemctl start docker

sudo systemctl enable docker
```

### influx DB 설치하기

1. 데이터 저장 디렉터리 생성

```bash
mkdir -p ~/influxdb/data
mkdir -p ~/influxdb/config
cd ~/influxdb
```

2. 데이터 저장 디렉터리 생성

```vim
version: "3.8"

services:
  influxdb:
    image: influxdb:2.7
    container_name: influxdb
    restart: unless-stopped

    ports:
      - "8086:8086"

    volumes:
      - ./data:/var/lib/influxdb2
      - ./config:/etc/influxdb2

    environment:
      DOCKER_INFLUXDB_INIT_MODE: setup
      DOCKER_INFLUXDB_INIT_USERNAME: admin
      DOCKER_INFLUXDB_INIT_PASSWORD: Admin1234!
      DOCKER_INFLUXDB_INIT_ORG: my-org
      DOCKER_INFLUXDB_INIT_BUCKET: my-bucket
      DOCKER_INFLUXDB_INIT_ADMIN_TOKEN: my-super-secret-token
```

3. 컨테이너 실행

```bash
docker compose up -d
```

실행 확인

```bash
docker ps
```

4. 웹 UI 접속

브라우저에서 `http://서버IP(또는 localhost):8086`

5. 로그 확인

```bash
docker logs -f influxdb
```

6. 컨테이너 관리

중지
```bash
docker compose stop
```

시작
```bash
docker compose start
```

재시작
```bash
docker compose restart
```

삭제(데이터 유지)
```bash
docker compose down
```

삭제(데이터 삭제)
```bash
docker compose down -v
```

- 디렉터리 구조
```plaintext
~/influxdb/
├── docker-compose.yml
├── data/
└── config/
```
