import streamlit as st
import time
import random

st.set_page_config(
    page_title="NHỮNG CON VỊT KHÔNG MAY MẮN",
    page_icon="🦆",
    layout="wide"
)

# Cấu hình giao diện CSS trang trí chữ 3D & hình ảnh vịt 3D chân thực
st.markdown("""
    <style>
    /* Tiêu đề 3D chữ to, bóng bẩy và màu sắc rực rỡ */
    .super-title-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        margin-top: 10px;
        margin-bottom: 25px;
    }
    
    .super-title {
        display: inline-block;
        font-size: 2.8rem;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 2px;
        background: linear-gradient(180deg, #ffe066 0%, #ff922b 50%, #d9480f 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        -webkit-text-stroke: 1.5px #ffffff;
        filter: drop-shadow(0 4px 0px #b02a00) 
                drop-shadow(0 7px 2px #5c1400) 
                drop-shadow(0 12px 15px rgba(0, 0, 0, 0.4));
        line-height: 1.2;
    }

    /* Hiệu ứng bồng bềnh như nổi trên nước cho 2 chú vịt */
    .duck-3d-left {
        width: 75px;
        height: 75px;
        filter: drop-shadow(0 6px 8px rgba(0,0,0,0.3));
        animation: bobDuck 2.4s ease-in-out infinite alternate;
    }

    .duck-3d-right {
        width: 75px;
        height: 75px;
        filter: drop-shadow(0 6px 8px rgba(0,0,0,0.3));
        transform: scaleX(-1); /* Lật gương để vịt hướng mặt vào tiêu đề */
        animation: bobDuck 2.4s ease-in-out infinite alternate -1.2s;
    }

    @keyframes bobDuck {
        0% { transform: translateY(0px) rotate(0deg); }
        100% { transform: translateY(-7px) rotate(3deg); }
    }

    .duck-3d-right {
        animation-name: bobDuckRight;
    }

    @keyframes bobDuckRight {
        0% { transform: scaleX(-1) translateY(0px) rotate(0deg); }
        100% { transform: scaleX(-1) translateY(-7px) rotate(3deg); }
    }

    /* Khung đường đua nước */
    .track-box {
        position: relative;
        background: linear-gradient(180deg, #38bdf8 0%, #0284c7 50%, #0369a1 100%);
        border-radius: 16px;
        padding: 15px 75px 15px 15px;
        border: 5px solid #0284c7;
        box-shadow: inset 0 0 20px rgba(0,0,0,0.2), 0 8px 20px rgba(0,0,0,0.1);
        overflow: hidden;
    }
    
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
    
    .duck-wrapper {
        display: inline-flex;
        flex-direction: column;
        align-items: center;
        z-index: 6;
    }
    
    .duck-nametag {
        background: rgba(255, 255, 255, 0.95);
        color: #0f172a;
        font-weight: bold;
        font-size: 0.8rem;
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

# SVG chú vịt 3D đổ bóng chân thực
duck_svg_code = """
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <!-- Gradient đổ bóng thân 3D -->
        <radialGradient id="body3D" cx="40%" cy="35%" r="65%">
            <stop offset="0%" stop-color="#fff275"/>
            <stop offset="45%" stop-color="#ffb703"/>
            <stop offset="85%" stop-color="#fb8500"/>
            <stop offset="100%" stop-color="#c95700"/>
        </radialGradient>
        <!-- Gradient đầu vịt 3D -->
        <radialGradient id="head3D" cx="35%" cy="30%" r="60%">
            <stop offset="0%" stop-color="#fff69b"/>
            <stop offset="50%" stop-color="#ffc107"/>
            <stop offset="90%" stop-color="#fb8500"/>
            <stop offset="100%" stop-color="#b04f00"/>
        </radialGradient>
        <!-- Gradient cánh vịt -->
        <linearGradient id="wing3D" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#ffea65"/>
            <stop offset="60%" stop-color="#ffaa00"/>
            <stop offset="100%" stop-color="#d65a00"/>
        </linearGradient>
        <!-- Gradient mỏ vịt -->
        <linearGradient id="beak3D" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#ff9e00"/>
            <stop offset="60%" stop-color="#e85d04"/>
            <stop offset="100%" stop-color="#9d0208"/>
        </linearGradient>
    </defs>
    <!-- Thân vịt 3D -->
    <path d="M 22 55 C 10 55 12 76 28 80 C 45 83 75 83 82 66 C 85 58 78 50 68 50 C 58 50 48 54 36 54 C 28 54 25 55 22 55 Z" fill="url(#body3D)"/>
    <!-- Cánh vịt nổi khối -->
    <path d="M 32 58 C 22 58 20 72 32 75 C 44 77 60 72 58 63 C 57 58 42 58 32 58 Z" fill="url(#wing3D)" opacity="0.95"/>
    <path d="M 35 60 C 26 60 25 68 33 70 C 43 72 52 69 50 64 C 48 60 41 60 35 60 Z" fill="#fff" opacity="0.2"/>
    <!-- Đầu vịt 3D -->
    <circle cx="63" cy="38" r="21" fill="url(#head3D)"/>
    <!-- Vệt bóng sáng bóng bẩy trên trán (Highlight) -->
    <ellipse cx="58" cy="27" rx="7" ry="4" fill="#ffffff" opacity="0.55" transform="rotate(-20 58 27)"/>
    <!-- Mỏ vịt 3D -->
    <path d="M 76 38 C 88 38 95 44 87 49 C 78 52 74 46 72 44 Z" fill="url(#beak3D)"/>
    <!-- Mắt vịt to tròn đen bóng có điểm sáng -->
    <circle cx="68" cy="33" r="4.5" fill="#1e293b"/>
    <circle cx="69.5" cy="31.5" r="1.6" fill="#ffffff"/>
    <circle cx="66.5" cy="34.5" r="0.8" fill="#ffffff"/>
</svg>
"""

# Hiển thị tiêu đề với 2 vịt 3D chất lượng cao
st.markdown(f"""
<div class="super-title-container">
    <div class="duck-3d-left">{duck_svg_code}</div>
    <span class="super-title">NHỮNG CON VỊT KHÔNG MAY MẮN</span>
    <div class="duck-3d-right">{duck_svg_code}</div>
</div>
""", unsafe_allow_html=True)

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
        duck_icons = ["🦆", "🐤", "🐥"]
        lanes_html = ""
        for idx, (name, pos) in enumerate(positions.items()):
            indent = int(pos * 85 / 100)
            icon = duck_icons[idx % len(duck_icons)]
            lanes_html += f"<div class='lane'><div class='duck-wrapper' style='margin-left: {indent}%;'><div class='duck-nametag'>{name}</div><div class='duck-avatar'>{icon}</div></div></div>"
            
        full_html = f"<div class='track-box'><div class='finish-banner'>FINISH</div><div class='finish-line'></div>{lanes_html}</div>"
        track_placeholder.markdown(full_html, unsafe_allow_html=True)

    # Khởi tạo vị trí ban đầu
    positions = {name: 0 for name in names}
    render_track(positions)

    # Xử lý cuộc đua
    if start_btn and names:
        steps = int(race_time * 10)
        finished_order = []
        
        for step in range(1, steps + 1):
            time.sleep(0.1)
            for name in names:
                if positions[name] < 100:
                    positions[name] += random.uniform(0.8, 3.8)
                    if positions[name] >= 100:
                        positions[name] = 100
                        if name not in finished_order:
                            finished_order.append(name)
            render_track(positions)
        
        for name, _ in sorted(positions.items(), key=lambda x: x[1], reverse=True):
            if name not in finished_order:
                finished_order.append(name)
        
        st.success(f"🏆 NGƯỜI CHIẾN THẮNG: **{finished_order[0]}** 🎉")
        st.balloons()
