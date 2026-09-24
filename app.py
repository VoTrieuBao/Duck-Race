import streamlit as st
import streamlit.components.v1 as components

# Cấu hình trang Streamlit
st.set_page_config(
    page_title="Game Đua Vịt Vui Vẻ",
    page_icon="🦆",
    layout="wide"
)

# Đọc hoặc dán mã HTML/CSS/JS của game tại đây
html_code = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Game Đua Vịt Vui Vẻ</title>
</head>
<body>
    <!-- Mã HTML/JS Game Đua Vịt ở đây -->
</body>
</html>
"""

# Hiển thị giao diện HTML game trong Streamlit
components.html(html_code, height=900, scrolling=True)
