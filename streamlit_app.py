import streamlit as st

st.title("배가 아프나요?")
st.write(
    "반갑습니다. 저는 똥입니다. 지금부터 나오겠습니다."
)

if st.button("똥싸기 버튼"):
    st.write("뿌지직!")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgLYELrfWxO0c3gzrzbSg4qGAYJedosxKSfg&s")

onedaypoopnum = st.number_input("하루에 똥싸는 횟수를 입력해주세요.", step=1)
st.write("하루 똥 수:", onedaypoopnum)

if onedaypoopnum >2:
    st.write("you are 똥쨍이")
else:
    st.write("you are 정상인")

level = st.slider("똥 마려운 정도", 1, 10, 5)
st.write("선택한 똥 마려운 정도:", level)

if level > 6:
    st.write("very 급함ㅠㅠ")
else:
    st.write("참아라 닝겐")


st.success("똥")
st.info("싸")
st.warning("라")
st.video("https://www.youtube.com/watch?v=twqHKKC41bg")


#주석 주석 주석 주석 주석 주석 주석 주석 주석










