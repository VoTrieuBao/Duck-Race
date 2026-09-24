import streamlit as st
import time
import random

st.set_page_config(
    page_title="TRƯỜNG ĐUA VỊT MAY MẮN",
    page_icon="🦆",
    layout="wide"
)

# Tối ưu giao diện & CSS trang trí
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #ff8c00;
        font-size: 2.3rem;
        font-weight: 800;
        margin-bottom: 20px;
        text-shadow: 2px 2px 0px #333, -1px -1px 0 #fff;
    }
    
    /* Khung đường đua nước sinh động */
    .track-box {
        position: relative;
        background: linear-gradient(180deg, #38bdf8 0%, #0284c7 50%, #0369a1 100%);
        border-radius: 16px;
        padding: 15px 75px 15px 15px;
        border: 5px solid #0284c7;
        box-shadow: inset 0 0 20px rgba(0,0,0,0.2), 0 8px 20px rgba(0,0,0,0.1);
        overflow: hidden;
    }
    
    /* Vạch đích Finish chuẩn */
    .finish-banner {
        position: absolute;
        right: 15px;
        top: 8px;
        background: #dc2626;
        color: white;
        font-weight: bold;
        font-size: 0.75rem;
        padding: 2px 8px;
        border-radius: 4px;
        z-index: 10;
        letter-spacing: 1px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .finish-line {
        position: absolute;
        right: 35px;
        top: 0;
        bottom: 0;
        width: 22px;
        background: repeating-linear-gradient(0deg, #000, #000 10px, #fff 10px, #fff 20px);
        border-left: 2px solid #fff;
        border-right: 2px solid #fff;
        z-index: 5;
    }
    
    /* Làn đua */
    .lane {
        position: relative;
        height: 52px;
        border-bottom: 2px dashed rgba(255,255,255,0.4);
        display: flex;
        align-items: center;
    }
    .lane:last-child {
        border-bottom: none;
    }
    
    /* Thiết kế Vịt ghép tên liền khối */
    .duck-wrapper {
        display: inline-flex;
        flex-direction: column;
        align-items: center;
        transition: margin-left 0.1s linear;
        z-index: 6;
    }
    
    .duck-nametag {
        background: rgba(255, 255, 255, 0.95);
        color: #0f172a;
        font-weight: bold;
        font-size: 0.75rem;
        padding: 1px 8px;
        border-radius: 12px;
        white-space: nowrap;
        box-shadow: 0 2px 5px rgba(0,0,0,0.25);
        border: 1.5px solid #0284c7;
        margin-bottom: -4px;
    }
    
    .duck-avatar {
        font-size: 1.8rem;
        filter: drop-shadow(0 3px 3px rgba(0,0,0,0.3));
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🦆 TRƯỜNG ĐUA VỊT MAY MẮN 🦆</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📋 Danh sách đua")
    names_input = st.text_area(
        "Nhập tên đua (Mỗi dòng 1 tên):",
        value="Khải\nTùng\nLan\nCường\nMinh\nAnh",
        height=160
    )
    names = [n.strip() for n in names_input.split('\n') if n.strip()]
    
    race_time = st.number_input("⏱ Thời gian đua (giây):", min_value=3, max_value=30, value=10)
    start_btn = st.button("🚀 BẮT ĐẦU CUỘC ĐUA", type="primary", use_container_width=True)

with col2:
    st.subheader("🏁 Đường Đua")
    
    track_placeholder = st.empty()
    
    def render_track(positions):
        # Biểu tượng các chú vịt màu sắc khác nhau
        duck_icons = ["🦆", "🐤", "🐥"]
        
        html_content = """
        <div class='track-box'>
            <div class='finish-banner'>FINISH</div>
            <div class='finish-line'></div>
        """
        
        for idx, (name, pos) in enumerate(positions.items()):
            # Tính toán khoảng cách di chuyển từ 0% đến 85% đường đua
            indent = int(pos * 85 / 100)
            icon = duck_icons[idx % len(duck_icons)]
            
            html_content += f"""
            <div class='lane'>
                <div class='duck-wrapper' style='margin-left: {indent}%;'>
                    <div class='duck-nametag'>{name}</div>
                    <div class='duck-avatar'>{icon}</div>
                </div>
            </div>
            """
            
        html_content += "</div>"
        track_placeholder.markdown(html_content, unsafe_allow_html=True)

    # Khởi tạo vị trí ban đầu
    positions = {name: 0 for name in names}
    render_track(positions)

    # Xử lý cuộc đua khi bấm nút
    if start_btn and names:
        steps = int(race_time * 10)
        finished_order = []
        
        for step in range(1, steps + 1):
            time.sleep(0.1)
            for name in names:
                if positions[name] < 100:
                    # Tạo độ tăng ngẫu nhiên cho từng chú vịt
                    positions[name] += random.uniform(0.8, 3.8)
                    if positions[name] >= 100:
                        positions[name] = 100
                        if name not in finished_order:
                            finished_order.append(name)
            render_track(positions)
        
        # Bổ sung các vịt chưa về đích vào bảng xếp hạng
        for name, _ in sorted(positions.items(), key=lambda x: x[1], reverse=True):
            if name not in finished_order:
                finished_order.append(name)
        
        st.success(f"🏆 NGƯỜI CHIẾN THẮNG: **{finished_order[0]}** 🎉")
        st.balloons()
