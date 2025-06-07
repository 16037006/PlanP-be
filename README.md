# 개요

의미 기반 일정 추천 플래너

# Architecture

```shell
PlanP - BE/
├── main.py
├── routers/
│   ├── schedule.py     # 일정 CRUD
│   ├── emotion.py      # 감정 입력/추천
│   └── location.py     # 화장실/ATM 정보
├── services/
│   ├── gpt.py          # ChatGPT API 연동
│   └── weather.py      # 날씨 API 연동
├── models/
│   ├── user.py
│   └── schedule.py
├── database.py         # DB 연결
├── config.py           # 설정파일(.env 읽기)
└── utils/              # 공통 유틸
```

