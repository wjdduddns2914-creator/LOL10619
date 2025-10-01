import streamlit as st

st.set_page_config(page_title="리그 오브 레전드 퀴즈", page_icon="🎮", layout="centered")

# --- 퀴즈 데이터 (10문제 전부) ---
quiz_data = [
    {
        "question": "다음 중 **녹서스** 소속 챔피언이 아닌 것은 무엇인가요?",
        "options": ["다리우스", "카타리나", "스웨인", "가렌"],
        "answer": "가렌",
        "hint": "가렌은 녹서스의 숙적, 데마시아의 용감한 선봉대 소속입니다.",
        "rationale": "정답은 **가렌**입니다. 나머지는 모두 녹서스 소속이에요."
    },
    {
        "question": "챔피언 **'야스오'**의 상징적인 타이틀은 무엇인가요?",
        "options": ["추방된 검", "용서받지 못한 자", "그림자의 계승자", "시간의 수호자"],
        "answer": "용서받지 못한 자",
        "hint": "그의 스킬 이름에도 이 단어가 포함되어 있어요.",
        "rationale": "정답은 **용서받지 못한 자**입니다. 야스오는 룬테라에서 자신의 결백을 증명하기 위해 싸우고 있죠."
    },
    {
        "question": "궁극기 **'완벽한 진실'**을 사용하는 챔피언은 누구인가요?",
        "options": ["제드", "아칼리", "케인", "킨드레드"],
        "answer": "제드",
        "hint": "그는 그림자의 힘을 사용하며, 라이벌은 쉔입니다.",
        "rationale": "정답은 **제드**입니다. 제드의 궁극기는 순간이동 후 큰 피해를 입히죠."
    },
    {
        "question": "다음 중 기본 공격 대신 **'독성 트레일'**을 남기며 이동하는 챔피언은 누구인가요?",
        "options": ["신지드", "트린다미어", "문도 박사", "블라디미르"],
        "answer": "신지드",
        "hint": "그는 화학 기술을 이용한 혼돈의 전문가입니다.",
        "rationale": "정답은 **신지드**입니다. 그의 대표적인 스킬은 독성 트레일이죠."
    },
    {
        "question": "다음 챔피언 중 **바스타야(Vastaya)** 종족에 속하지 않는 챔피언은 누구인가요?",
        "options": ["아리", "라칸", "자야", "나서스"],
        "answer": "나서스",
        "hint": "나서스는 슈리마의 고대 초월체입니다.",
        "rationale": "정답은 **나서스**입니다. 아리, 라칸, 자야는 바스타야에 속합니다."
    },
    {
        "question": "챔피언 **'징크스'**가 사용하는 무기 중, 주변 광역 피해를 입히는 로켓 발사기의 이름은 무엇인가요?",
        "options": ["빠직!", "와작와작 지뢰", "생선대가리", "수류탄"],
        "answer": "생선대가리",
        "hint": "영어 이름은 Fishbones입니다.",
        "rationale": "정답은 **생선대가리**입니다. 징크스의 상징적인 무기죠."
    },
    {
        "question": "이 챔피언은 **'타곤 산의 태양'**으로 불리며, 방패와 검을 사용하는 탱커 서포터입니다.",
        "options": ["레오나", "타릭", "판테온", "다이애나"],
        "answer": "레오나",
        "hint": "패시브는 아군이 추가 피해를 입히게 합니다.",
        "rationale": "정답은 **레오나**입니다. 타곤 산의 대표 서포터 챔피언이죠."
    },
    {
        "question": "아군 챔피언에게 보호막을 씌우고 전장 어디든 순간이동할 수 있는 글로벌 궁극기를 가진 챔피언은 누구인가요?",
        "options": ["트위스티드 페이트", "갈리오", "쉔", "이즈리얼"],
        "answer": "쉔",
        "hint": "그는 이오니아 출신이며, 궁극기는 Stand United입니다.",
        "rationale": "정답은 **쉔**입니다. 그의 궁극기는 아군을 보호하고 합류할 수 있어요."
    },
    {
        "question": "리그 오브 레전드 초창기(시즌 1 이전)에 출시된 챔피언 중 하나는?",
        "options": ["벨베스", "아트록스", "아무무", "세라핀"],
        "answer": "아무무",
        "hint": "그는 미라 소년입니다. '날 안아줄 건가요?'",
        "rationale": "정답은 **아무무**입니다. 2009년 출시된 초기 챔피언이에요."
    },
    {
        "question": "챔피언 **'티모'**의 주력 무기는 무엇인가요?",
        "options": ["장검", "석궁", "독 다트", "활"],
        "answer": "독 다트",
        "hint": "그는 밴들 시티의 정찰대원입니다.",
        "rationale": "정답은 **독 다트**입니다. 티모의 상징이죠."
    },
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

    st.title("🎮 리그 오브 레전드 챔피언 퀴즈")
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
            st.experimental_rerun()

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
        st.experimental_rerun()
