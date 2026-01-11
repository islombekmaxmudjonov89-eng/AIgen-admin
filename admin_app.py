import streamlit as st
import requests
import base64
import json

# --- SOZLAMALAR ---
# Tokenning boshida va oxirida bo'sh joy qolmasin!
GITHUB_TOKEN = "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" 
REPO_NAME = "islombekmaxmudjonov89-eng/AIGen.uz"
FILE_PATH = "config.json"

st.set_page_config(page_title="AIGen Admin", page_icon="🔒")

st.title("👨‍💻 AIGen.uz Boshqaruv Paneli")

# Parol bilan himoya
password = st.sidebar.text_input("Parolni kiriting:", type="password")

if password == "ADMIN1986":
    st.success("Xush kelibsiz, Admin!")
    
    # Statistika (Hozircha qo'lda, keyin Adsterra bilan ulaymiz)
    col1, col2 = st.columns(2)
    col1.metric("Bugungi kliklar", "125", "+12%")
    col2.metric("Taxminiy daromad", "$1.20", "+0.15")

    st.subheader("🔗 Reklama havolasini boshqarish")
    
    # Hozirgi linkni config.json dan o'qib olish
    url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    
    new_link = st.text_input("Yangi Smartlinkni kiriting:", placeholder="Adsterra linkini bu yerga qo'ying")
    
    if st.button("Yangilash"):
        if GITHUB_TOKEN == "BU_YERGA_TOKENNI_QUY":
            st.error("Xatolik: Avval GITHUB_TOKEN o'rniga o'z kalitingizni qo'ying!")
        elif new_link:
            # GitHub API orqali faylni yangilash
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                sha = r.json()['sha']
                content = base64.b64encode(json.dumps({"ad_link": new_link}).encode()).decode()
                
                data = {
                    "message": "Link admin panel orqali yangilandi",
                    "content": content,
                    "sha": sha
                }
                
                put_r = requests.put(url, headers=headers, json=data)
                if put_r.status_code == 200:
                    st.balloons()
                    st.success("Link muvaffaqiyatli yangilandi! Endi AIGen.uz da yangi reklama chiqadi.")
                else:
                    st.error(f"Xatolik: GitHub saqlay olmadi. Status: {put_r.status_code}")
            else:
                st.error("Xatolik: GitHub faylni topa olmadi yoki Token noto'g'ri.")
        else:
            st.warning("Iltimos, yangi linkni kiriting.")
else:
    st.info("Boshqaruv paneliga kirish uchun parolni kiriting.")
