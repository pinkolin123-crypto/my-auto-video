import streamlit as st

st.markdown("### ✨ One-Click Auto Pilot")
st.write("ဗီဒီယိုဖိုင် သို့မဟုတ် လင့်ခ်ကို ထည့်ပြီး အောက်ပါခလုတ်ကို နှိပ်ပါ။")

tab1, tab2 = st.tabs(["📁 File Upload", "🔗 Video Link"])

with tab1:
  uploaded_file = st.file_uploader("ဗီဒီယိုဖိုင် ရွေးချယ်ပါ", type=["mp4", "mp3"])
  if uploaded_file is not None:
    st.success("ဖိုင်တင်ပြီးပါပြီ!")

with tab2:
  video_link = st.text_input("YouTube လင့်ခ် ထည့်ပါ")

if st.button("🚀 စတင်ဖန်တီးမည်"):
  st.info("AI လုပ်ဆောင်နေပါပြီ... ခဏစောင့်ပေးပါ။")
