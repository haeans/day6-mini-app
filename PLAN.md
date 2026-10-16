# app.py 계획

## 읽은 파일
- AGENTS.md (폴더에 다른 파일 없음, app.py도 아직 없음)

## 만들거나 수정할 파일
- 만들기: app.py (단일 파일, 표준 라이브러리만 사용)
- 수정: 없음

## 구현할 함수
- `main()`: 메뉴 루프 (추가 / 목록 / 종료)
- `add_task(tasks, title, priority)`: 할 일 추가
- `sort_tasks(tasks)`: 우선순위 순 정렬 (같으면 입력 순서 유지)
- `show_tasks(tasks)`: 정렬된 목록 출력
- `read_priority()`: 우선순위 입력 검증

## 실행할 확인 명령
- `uv --version`
- `uv run python --version`
- `uv run app.py` (우선순위가 다른 할 일을 여러 개 추가한 뒤 순서대로 나오는지 확인)

## 결정이 필요한 질문
1. 우선순위 표현: 숫자(1=높음) vs 높음/중간/낮음?
2. 저장: 메모리만(종료 시 사라짐) vs JSON 파일 저장?
3. 기능 범위: 추가·목록만 vs 완료 처리·삭제 포함?
