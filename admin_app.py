import streamlit as st
import requests
import base64
import json

# --- SOZLAMALAR ---
# Tokenning boshida yoki oxirida bo'sh joy qolmasin!
GITHUB_TOKEN = "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" 
REPO_NAME = "islombekmaxmudjonov89-eng/AIGen.uz"
FILE_PATH = "config.json"

st.set_page_config(page_title="AIGen Admin", page_icon="🔒")
st.title("👨‍💻 AIGen.uz Boshqaruv Paneli")

password = st.sidebar.text_input("Parolni kiriting:", type="password")

# Kodingdagi yangi parol
if password == "ADMIN1986":
    st.success("Xush kelibsiz, Admin!")
    
    st.subheader("🔗 Reklama havolasini boshqarish")
    new_link = st.text_input("Yangi Smartlinkni kiriting:", placeholder="HilltopAds linkini qo'ying")
    
    if st.button("Yangilash"):
        url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FILE_PATH}"
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        # 1. Avval faylni tekshiramiz
        r = requests.get(url, headers=headers)
        
        if r.status_code == 200:
            sha = r.json()['sha']
            # Yangi ma'lumotni tayyorlash
            content_dict = {"ad_link": new_link}
            content_json = json.dumps(content_dict, indent=4)
            content_base64 = base64.b64encode(content_json.encode()).decode()
            
            data = {
                "message": "Link yangilandi",
                "content": content_base64,
                "sha": sha
            }
            
            # 2. Faylni yangilaymiz
            put_r = requests.put(url, headers=headers, json=data)
            
            if put_r.status_code == 200:
                st.balloons()
                st.success("Muvaffaqiyatli! Saytga o'tib tekshiring.")
            else:
                st.error(f"GitHub yangilay olmadi. Kod: {put_r.status_code}")
        elif r.status_code == 401:
            st.error("Xatolik: Token muddati o'tgan yoki noto'g'ri!")
        elif r.status_code == 404:
            st.error(f"Xatolik: {FILE_PATH} fayli topilmadi!")
        else:
            st.error(f"Bog'lanishda xato: {r.status_code}")
else:
    st.info("Kirish uchun parolni kiriting.")
