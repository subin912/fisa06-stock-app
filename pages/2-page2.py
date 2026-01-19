import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

#text_input을 활용해서 검색창을 만듭니다. 
#이 검색창에 ani_list 안의 일부 단어가 일치하면
#img_list의 해당 이미지를 출력하는 로직을 만들어 주세요
# if / for 를 활용하면 될겁니다
data = st.text_input('검색어 입력하세요') #입력받아야하니까 변수몀에 넣어줌.
#확인할때 st.write(data)로 확인하기 f-string 같은 느낌!
if data:
   #st.write_stream()
   for i in range(len(ani_list)):
      # 부분 문자열 포함 여부
      if data.lower() in ani_list[i].lower():
        st.image(img_list[i], caption=ani_list[i])
        found = True
#화면에 뜨는 것부터 1개만 만들고 


##또다른 방법
# if search !='':
# for ani in ani_list:
#    if search in ani:
#     st.image(imag_list[ani_list.index(ani)])


#최종 목표는 주가 데이터 받아와서 