# streamlit官方网址：https://streamlit.io
# 安装streamlit : pip install streamlit
# 运行streamlit : streamlit run xxx.py
import streamlit as st

# 标题
st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")

# 插入图片
st.image(r"D:\PycharmProjects\PythonProject\py_project01\streamlit素材\dog.jpg")

# 插入文字
st.write("阳光洒满青草地，一只柯基仰躺在草坪上，肚皮舒展，四肢轻轻抬起。它嘴巴张开，吐着粉嫩舌头，黑亮的眼睛亮晶晶的，满是惬意欢喜。背景里帐篷与绿树朦胧柔和，暖融融的氛围，像把无忧无虑的快乐，都揉进了这明媚的户外时光里。")

# 插入音频
st.audio(r"D:\PycharmProjects\PythonProject\py_project01\streamlit素材\龙呼呼.mp3")

# 插入视频
st.video(r"D:\PycharmProjects\PythonProject\py_project01\streamlit素材\视频.mp4",loop=True,autoplay=True,alt="年轻女性与柯基在草地嬉戏玩耍")

# 插入logo
st.logo(r"D:\PycharmProjects\PythonProject\py_project01\streamlit素材\logo.png")

# 输入用户名和密码
name = st.text_input("请输入您的用户名")
password = st.text_input("请输入密码",type="password")
st.write(f"您的用户名：{name}\n您的密码：{password}")

# 插入代码
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")

# 雪
st.snow()

# 单选按钮
gender = st.radio("请选择您的性别",["男","女","不愿透露"],index=2)



