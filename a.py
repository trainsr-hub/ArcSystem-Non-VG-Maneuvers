import streamlit as st

def convert_channel_id_to_playlist(channel_id):
    # Kiểm tra nếu input hợp lệ và có ký tự 'C' ở vị trí thứ 2 (index 1)
    if len(channel_id) > 1 and channel_id[1] == 'C':
        # Thay thế ký tự 'C' tại index 1 bằng 'U'
        # [Sửa đổi]: Sử dụng slicing để thay đổi chính xác ký tự thứ 2
        playlist_id = channel_id[0] + 'U' + channel_id[2:]
        return f"https://www.youtube.com/playlist?app=desktop&list={playlist_id}"
    return None

st.title("YouTube Channel ID to Playlist Converter")

# Input text từ người dùng
user_input = st.text_input("Nhập Channel ID (VD: UC_zAM9xR1ck0jV8bMdPfhnA):")

if user_input:
    result_link = convert_channel_id_to_playlist(user_input.strip())
    
    if result_link:
        st.success("Chuyển đổi thành công!")
        # Hiển thị clickable link
        st.markdown(f"**Kết quả:** [{result_link}]({result_link})")
    else:
        st.error("Định dạng ID không hợp lệ (Cần bắt đầu bằng 'UC...')")

# --- Tóm tắt các thay đổi ---
# 1. Thêm logic xử lý chuỗi: Cắt chuỗi tại vị trí index 1 để thay 'C' thành 'U'.
# 2. Tích hợp Streamlit: Sử dụng st.text_input để nhận dữ liệu và st.markdown để hiển thị link có thể click.
# 3. Validation: Kiểm tra điều kiện ký tự thứ 2 trước khi xử lý để tránh lỗi input sai định dạng.