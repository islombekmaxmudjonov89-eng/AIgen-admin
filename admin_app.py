import streamlit as st
import requests
import base64
import json

# --- SOZLAMALAR (HASAN MIGAL USULI) ---
# Tokenning boshida yoki oxirida bitta ham bo'sh joy qolmasin!
GITHUB_TOKEN = "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" 
REPO_NAME = "islombekmaxmudjonov89-eng/AIGen.uz"
FILE_PATH = "config.json"

st.set_page_config(page_title="AIGen Admin", page_icon="🔒")
st.title("👨‍💻 AIGen.uz Boshqaruv Paneli")

password = st.sidebar.text_input("Parolni kiriting:", type="password")

if password == "ADMIN1986":
    st.success("Xush kelibsiz, Admin!")
    new_link = st.text_input("Yangi Smartlinkni kiriting:", placeholder="Linkni shu yerga tashla")
    
    if st.button("Yangilash"):
        url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FILE_PATH}"
        # Tokenni to'g'ri yuborish uchun header
        headers = {
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        r = requests.get(url, headers=headers)
        
        if r.status_code == 200:
            sha = r.json()['sha']
            content_base64 = base64.b64encode(json.dumps({"ad_link": new_link}).encode()).decode()
            
            data = {"message": "Link yangilandi", "content": content_base64, "sha": sha}
            put_r = requests.put(url, headers=headers, json=data)
            
            if put_r.status_code == 200:
                st.balloons()
                st.success("Bo'ldi uka, soqqa tayyor! Saytni tekshir.")
            else:
                st.error(f"GitHub ruxsat bermadi: {put_r.status_code}")
        elif r.status_code == 401:
            st.error("Token xato! GitHub'dan yangi token olib, kodga qo'y.")
        else:
            st.error(f"Xatolik kodi: {r.status_code}")
else:
    st.info("Kirish uchun parolni kiriting.")
