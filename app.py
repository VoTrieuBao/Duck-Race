import streamlit as st
import time
import random

st.set_page_config(page_title="GAME ĐUA VỊT MAY MẮN", page_icon="🦆", layout="wide")

st.markdown("""
    <style>
    .main-title { text-align: center; color: #ff8c00; font-size: 2.2rem; font-weight: bold; margin-bottom: 20px; }
    .track-box { background: linear-gradient(180deg, #38bdf8 0%, #0284c7 100%); border-radius: 12px; padding: 15px; border: 4px solid #0284c7; }
    .lane { position: relative; height: 45px; border-bottom: 1px dashed rgba(255,255,255,0.4); display: flex; align-items: center; }
    .duck-tag { background: white; color: #1e293b; font-weight: bold; font-size: 0.8rem; padding: 2px 8px; border-radius: 10px; border: 1px solid #0284c7; margin-right: 5px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🦆 TRƯỜNG ĐUA VỊT MAY MẮN 🦆</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📋 Danh sách đua")
    names_input = st.text_area("Nhập tên (Mỗi dòng 1 tên):", value="Khải\nTùng\nLan\nCường\nMinh\nAnh", height=150)
    names = [n.strip() for n in names_input.split('\n') if n.strip()]
    
    race_time = st.number_input("⏱ Thời gian đua (giây):", min_value=3, max_value=30, value=10)
    start_btn = st.button("🚀 BẮT ĐẦU CUỘC ĐUA", type="primary", use_container_width=True)

with col2:
    st.subheader("🏁 Đường Đua")
    
    track_placeholder = st.empty()
    
    def render_track(positions):
        html = "<div class='track-box'>"
        for name, pos in positions.items():
            indent = int(pos * 85 / 100)
            html += f"""
            <div class='lane'>
                <div style='margin-left: {indent}%; transition: all 0.1s linear;'>
                    <span class='duck-tag'>{name}</span> 🦆
                </div>
            </div>
            """
        html += "</div>"
        track_placeholder.markdown(html, unsafe_allow_html=True)

    # Khởi tạo vị trí ban đầu
    positions = {name: 0 for name in names}
    render_track(positions)

    if start_btn and names:
        steps = race_time * 10
        for step in range(1, steps + 1):
            time.sleep(0.1)
            for name in names:
                if positions[name] < 100:
                    positions[name] += random.uniform(0.5, 3.5)
                    if positions[name] > 100:
                        positions[name] = 100
            render_track(positions)
        
        # Xếp hạng
        sorted_results = sorted(positions.items(), key=lambda x: x[1], reverse=True)
        st.success(f"🏆 NGHƯỜI CẦN THẮNG: **{sorted_results[0][0]}** 🎉")
        st.balloons()
