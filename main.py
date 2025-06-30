import streamlit as st

st.title("Project 1")


# Show text:
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is a text")
st.caption("This is a caption")

st.divider()

# Markdown
st.markdown("# Heading 1")
st.markdown("## [AIVN](http:ss)")
st.markdown("""
1. Machine Learning
2. Deep Learning
            """)
st.markdown("$a_x + b = 0$")
st.latex(r"\sqrt{x} \rightarrow y")

# Code
st.code(
"""
import numpy as np
arr = np.array([1,2,3,4])
for a in arr:
    print(a)
""", language = "python")

st.divider()

st.write("hello")
st.write("## Hello 2")
st.write("$\sqrt{2x}$")

# Media
st.logo("coffee.png")
# st.image("coffee.png", caption="Coffee Image")
# st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4")
# st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

st.divider()
# Input
status = st.checkbox("Check me please")
st.write("Checkbox status:", status)
status_2 = st.radio("Color", ["Yellow", "Blue", "Red"], captions = [
    "This is yellow",
    "This is blue",
    "This is red"
])
st.write("Selected color:", status_2)
st.selectbox("Select one", ["Option 1", "Option 2"])

st.select_slider("Select a number", options = [1, 2, 3, 4, 5])
st.slider("Values", 0.0, 100.0, (25.0, 75.0), step = 5.0)
st.multiselect("Select multiple", ["Option 1", "Option 2", "Option 3"])
st.text_input("Enter your name", placeholder = "Type here")
st.number_input("Enter a number", min_value = 0, max_value = 100, value = 50, step = 1)

st.divider()

# Button
st.button("Click me")

if st.button("Click me 2"):
    st.write("Button clicked!")
else:
    st.write("Button not clicked!")

st.link_button("Go to AIVN", "https://aivn.org")

# Chatbot
st.chat_input("Ask me anything", key = "chat_input")
# st.chat_message("user", "Hello, how are you?")
# st.chat_message("assistant", "I'm fine, thank you!")

upload_files = st.file_uploader("Upload a file", type = ["csv", "txt", "pdf"], accept_multiple_files = True)

for upload_file in upload_files:
    # upload_file.read()
    st.write("File name:", upload_file.name)
    st.write("File type:", upload_file.type)

st.divider()

import numpy as np
# import pandas as pd
a = np.random.rand(10, 10)
print(a)

import pandas as pd
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.bar_chart(chart_data)

# st.write(st.session_state.key)

