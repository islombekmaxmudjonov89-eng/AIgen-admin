import streamlit as st

st.set_page_config(page_title="AIGen Admin", page_icon="🔒")

st.title("👨‍💻 AIGen.uz Boshqaruv Paneli")

# Parol bilan himoya
password = st.sidebar.text_input("Parolni kiriting:", type="password")

if password == "ADMIN1986": # Paroling shu bo'ladi
    st.success("Xush kelibsiz, Admin!")
    
    # Statistika (Hozircha qo'lda, keyin AdMaven bilan bog'laymiz)
    col1, col2 = st.columns(2)
    col1.metric("Bugungi kliklar", "125", "+12%")
    col2.metric("Taxminiy daromad", "$1.20", "+0.15")

    st.subheader("🔗 Reklama havolasini boshqarish")
    st.info("Hozirgi aktiv link: https://rtouchingthewaterw.com/?cGnR=1236571")
    
    new_link = st.text_input("Yangi Smartlinkni kiriting:")
    if st.button("Yangilash"):
        st.write("Link muvaffaqiyatli yangilandi (Hozircha simulyatsiya)")
else:
    st.warning("Kirish uchun parolni kiriting.")
