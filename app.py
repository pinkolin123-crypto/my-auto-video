import google.generativeai as genai
import streamlit as st

st.markdown("### 🎬 AI Movie Recap (Myanmar)")
st.write(
    "ရုပ်ရှင်ဇာတ်လမ်း အနှစ်ချုပ် (Movie Recap) များကို မြန်မာလို အလိုအလျောက်"
    " ဖန်တီးပေးမည့် AI စနစ်"
)

api_key = st.text_input("Gemini API Key ထည့်ပါ", type="password")

movie_title = st.text_input(
    "ရုပ်ရှင်အမည် သို့မဟုတ် ဇာတ်လမ်းအကြောင်း အတိုချုပ် ထည့်ပါ"
)

if st.button("🚀 မြန်မာလို Movie Recap စတင်ဖန်တီးမည်"):
  if not api_key:
    st.warning("ကျေးဇူးပြု၍ Gemini API Key ထည့်ပါ။")
  elif not movie_title:
    st.warning("ကျေးဇူးပြု၍ ရုပ်ရှင်အမည် သို့မဟုတ် ဇာတ်လမ်းအကြောင်း ထည့်ပါ။")
  else:
    try:
      genai.configure(api_key=api_key)
      model = genai.GenerativeModel("gemini-1.5-flash-8b")


      prompt = f"ရုပ်ရှင်အမည် '{movie_title}' အတွက် စိတ်ဝင်စားစရာကောင်းသော, လူကြိုက်များသော ဇာတ်လမ်းအနှစ်ချုပ် (Movie Recap) တစ်ခုကို မြန်မာဘာသာဖြင့် အသေးစိတ် ရေးသားပေးပါ။"

      with st.spinner("AI ဖြင့် ဇာတ်လမ်းအနှစ်ချုပ် ဖန်တီးနေပါပြီ... ခဏစောင့်ပါ"):
        response = model.generate_content(prompt)
        st.success("အောင်မြင်စွာ ဖန်တီးပြီးပါပြီ!")
        st.markdown("### 📝 ထွက်လာသော မြန်မာဇာတ်လမ်းအနှစ်ချုပ် -")
        st.write(response.text)

    except Exception as e:
      st.error(f"Error ဖြစ်ပေါ်နေပါသည်: {e}")
