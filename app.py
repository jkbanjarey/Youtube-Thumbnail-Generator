import streamlit as st
from main import generate_thumbnail_prompt, generate_image

st.set_page_config(page_title="YouTube Thumbnail Generator", layout="centered")

st.title("🎬 YouTube Thumbnail Creator with AI")
st.markdown("Paste a YouTube video summary or transcript below to generate a thumbnail image.")

video_summary = st.text_area("Video Summary / Transcript", height=300)

if st.button("Generate Thumbnail"):
    if not video_summary.strip():
        st.warning("Please enter a video summary.")
    else:
        with st.spinner("Generating prompt..."):
            prompt = generate_thumbnail_prompt(video_summary)

        with st.spinner("Generating image..."):
            image_bytes = generate_image(prompt)

        st.image(image_bytes, caption="AI-Generated Thumbnail", use_column_width=True)
        st.success("Thumbnail generated successfully!")

        # 🎯 Add download button
        st.download_button(
            label="📥 Download Thumbnail",
            data=image_bytes,
            file_name="youtube_thumbnail.png",
            mime="image/png"
        )
