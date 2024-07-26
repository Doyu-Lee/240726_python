import streamlit as st

st.title('테스트')

name = st.text_input('닉네임을 입력해주세요 : ', '예) 도유')
manu = st.selectbox('좋아하는 음식을 선택해주세요 :', ['망고빙수', '아몬드봉봉', '돈까스'])

if st.button('인사말 생성') :
  st.write(name + '님! 당신이 좋아하는 음식은 ' + menu + '이군요? 저도 좋아해요!')
