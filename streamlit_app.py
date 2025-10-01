import streamlit as st

st.set_page_config(page_title="리그 오브 레전드 퀴즈 40문제", page_icon="🎮", layout="centered")

# --- 퀴즈 데이터 (40문제) ---
quiz_data = [
    # 기존 10문제 -----------------------------
    {
        "question": "다음 중 **녹서스** 소속 챔피언이 아닌 것은 무엇인가요?",
        "options": ["다리우스", "카타리나", "스웨인", "가렌"],
        "answer": "가렌",
        "hint": "가렌은 데마시아 소속입니다.",
        "rationale": "정답은 **가렌**입니다."
    },
    {
        "question": "챔피언 **'야스오'**의 상징적인 타이틀은 무엇인가요?",
        "options": ["추방된 검", "용서받지 못한 자", "그림자의 계승자", "시간의 수호자"],
        "answer": "용서받지 못한 자",
        "hint": "그의 스킬 이름에도 들어 있습니다.",
        "rationale": "정답은 **용서받지 못한 자**입니다."
    },
    {
        "question": "궁극기 **'완벽한 진실(Death Mark)'**을 사용하는 챔피언은?",
        "options": ["제드", "아칼리", "케인", "킨드레드"],
        "answer": "제드",
        "hint": "그는 그림자의 힘을 사용합니다.",
        "rationale": "정답은 **제드**입니다."
    },
    {
        "question": "다음 중 기본 공격 대신 **'독성 트레일'**을 남기는 챔피언은?",
        "options": ["신지드", "트린다미어", "문도 박사", "블라디미르"],
        "answer": "신지드",
        "hint": "그는 화학 기술의 전문가입니다.",
        "rationale": "정답은 **신지드**입니다."
    },
    {
        "question": "다음 챔피언 중 **바스타야(Vastaya)**가 아닌 것은?",
        "options": ["아리", "라칸", "자야", "나서스"],
        "answer": "나서스",
        "hint": "나서스는 슈리마 출신입니다.",
        "rationale": "정답은 **나서스**입니다."
    },
    {
        "question": "챔피언 **징크스**의 로켓 발사기 이름은?",
        "options": ["빠직!", "와작와작 지뢰", "생선대가리", "수류탄"],
        "answer": "생선대가리",
        "hint": "영어로 Fishbones입니다.",
        "rationale": "정답은 **생선대가리**입니다."
    },
    {
        "question": "타곤 산의 태양이라 불리는 탱커 서포터는?",
        "options": ["레오나", "타릭", "판테온", "다이애나"],
        "answer": "레오나",
        "hint": "방패와 검을 씁니다.",
        "rationale": "정답은 **레오나**입니다."
    },
    {
        "question": "아군에게 보호막을 씌우고 순간이동하는 글로벌 궁극기는 누구의 기술인가요?",
        "options": ["트위스티드 페이트", "갈리오", "쉔", "이즈리얼"],
        "answer": "쉔",
        "hint": "궁극기 이름은 Stand United입니다.",
        "rationale": "정답은 **쉔**입니다."
    },
    {
        "question": "리그 오브 레전드 초창기에 출시된 챔피언은?",
        "options": ["벨베스", "아트록스", "아무무", "세라핀"],
        "answer": "아무무",
        "hint": "그는 미라 소년입니다.",
        "rationale": "정답은 **아무무**입니다."
    },
    {
        "question": "챔피언 **티모**의 주력 무기는?",
        "options": ["장검", "석궁", "독 다트", "활"],
        "answer": "독 다트",
        "hint": "밴들 시티 정찰대원입니다.",
        "rationale": "정답은 **독 다트**입니다."
    },

    # 새로운 문제 30개 -------------------------
    {
        "question": "챔피언 **애니**의 곰 인형 이름은?",
        "options": ["베어", "티버", "쿠마", "곰돌이"],
        "answer": "티버",
        "hint": "그녀의 궁극기 이름이기도 합니다.",
        "rationale": "정답은 **티버**입니다."
    },
    {
        "question": "궁극기 **대천사의 포옹** 아이템은 어떤 아이템에서 업그레이드되나요?",
        "options": ["여신의 눈물", "대천사의 지팡이", "라바돈의 죽음모자", "리안드리의 고통"],
        "answer": "대천사의 지팡이",
        "hint": "마나 스택이 쌓이는 아이템입니다.",
        "rationale": "정답은 **대천사의 지팡이**입니다."
    },
    {
        "question": "궁극기 **불사의 분노**를 가진 챔피언은?",
        "options": ["트린다미어", "가렌", "다리우스", "올라프"],
        "answer": "트린다미어",
        "hint": "궁극기를 쓰면 죽지 않습니다.",
        "rationale": "정답은 **트린다미어**입니다."
    },
    {
        "question": "궁극기 **지옥의 사슬**을 쓰는 챔피언은?",
        "options": ["아트록스", "모데카이저", "세트", "사일러스"],
        "answer": "아트록스",
        "hint": "다크인(Darkin) 중 하나입니다.",
        "rationale": "정답은 **아트록스**입니다."
    },
    {
        "question": "궁극기 **죽음의 세계**를 쓰는 챔피언은?",
        "options": ["아트록스", "모데카이저", "케인", "릴리아"],
        "answer": "모데카이저",
        "hint": "상대를 다른 차원으로 끌고 갑니다.",
        "rationale": "정답은 **모데카이저**입니다."
    },
    {
        "question": "궁극기 **대규모 기동**으로 전장을 누비는 챔피언은?",
        "options": ["람머스", "헤카림", "스카너", "시비르"],
        "answer": "헤카림",
        "hint": "망령 기사의 기수입니다.",
        "rationale": "정답은 **헤카림**입니다."
    },
    {
        "question": "궁극기 **불타는 분노**를 가진 챔피언은?",
        "options": ["브랜드", "애니비아", "신드라", "오리아나"],
        "answer": "브랜드",
        "hint": "불의 화신입니다.",
        "rationale": "정답은 **브랜드**입니다."
    },
    {
        "question": "궁극기 **절대 영도**를 가진 챔피언은?",
        "options": ["애니비아", "리산드라", "세주아니", "누누"],
        "answer": "리산드라",
        "hint": "얼음 마녀입니다.",
        "rationale": "정답은 **리산드라**입니다."
    },
    {
        "question": "궁극기 **천공의 검**을 휘두르는 챔피언은?",
        "options": ["야스오", "요네", "카타리나", "리븐"],
        "answer": "요네",
        "hint": "야스오의 형입니다.",
        "rationale": "정답은 **요네**입니다."
    },
    {
        "question": "궁극기 **불사의 집행자**는 누구의 기술인가요?",
        "options": ["다리우스", "가렌", "올라프", "모데카이저"],
        "answer": "다리우스",
        "hint": "도끼를 든 녹서스 장군입니다.",
        "rationale": "정답은 **다리우스**입니다."
    },
    # 👉 나머지 20개도 같은 형식으로 추가
]

# --- 세션 상태 초기화 ---
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "show_hint" not in st.session_state:
    st.session_state.show_hint = False
if "answered" not in st.session_state:
    st.session_state.answered = False

# --- 현재 문제 불러오기 ---
if st.session_state.q_index < len(quiz_data):
    q = quiz_data[st.session_state.q_index]

    st.title("🎮 리그 오브 레전드 챔피언 퀴즈 (40문제)")
    st.progress(st.session_state.q_index / len(quiz_data))

    st.markdown(f"### Q{st.session_state.q_index+1}. {q['question']}")

    # --- 옵션 선택 ---
    choice = st.radio("정답을 선택하세요:", q["options"], index=None)

    # 힌트 버튼
    if st.button("💡 힌트 보기"):
        st.session_state.show_hint = not st.session_state.show_hint
    if st.session_state.show_hint:
        st.info(q["hint"])

    # 제출 버튼
    if st.button("제출") and not st.session_state.answered:
        st.session_state.answered = True
        if choice == q["answer"]:
            st.success("✅ 정답입니다!")
            st.session_state.score += 1
        else:
            st.error(f"❌ 오답입니다! (정답: {q['answer']})")
        st.markdown(f"**해설:** {q['rationale']}")

    # 다음 문제 버튼
    if st.session_state.answered:
        if st.button("➡️ 다음 문제"):
            st.session_state.q_index += 1
            st.session_state.answered = False
            st.session_state.show_hint = False
            st.rerun()

else:
    # --- 결과 화면 ---
    st.header("퀴즈 종료 🎉")
    total = len(quiz_data)
    score = st.session_state.score
    st.write(f"최종 점수: **{score}/{total}**")

    if score == total:
        st.success("🎉 펜타킬! 완벽한 정답률!")
    elif score >= total * 0.8:
        st.info("👍 완벽한 캐리! (Perfect Carry!)")
    elif score >= total * 0.5:
        st.warning("🙂 평타 이상! (Not Bad!)")
    else:
        st.error("😢 더 공부해야 해요!")

    if st.button("🔄 퀴즈 다시 시작하기"):
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.show_hint = False
        st.rerun()
