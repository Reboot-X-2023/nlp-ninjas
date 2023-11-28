# app_speech_to_text_function.py
import streamlit as st
import openai
import speech_recognition as sr
openai.api_key='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'
def speech_to_text(audio_source):
    model_id='whisper-1'
    response=openai.Audio.transcribe(
    model=model_id,
    file=audio_source,
    response_format='srt'
)
    return response

def auto_summriztion(text):
    response = openai.Completion.create(
    engine="text-ada-001",  # specify engine
    prompt=f"Summarize the following text:\n{text}",
    max_tokens=150,  # maximum number of tokens in the response
    temperature=0.7,  # adjust the temperature parameter
    n=1  # Number of completions to generate
)
    summarized_text = response['choices'][0]['text']
    return summarized_text


def speech_to_text_and_summarize():

    # Streamlit app title
    st.title("Auto call summarizer")
    start_recording = st.button("Start Recording")

    # Record button
    if start_recording:
        with sr.Microphone() as source:
            st.info("Recording... Speak now!")
            recognizer=sr.Recognizer() 
            audio = recognizer.listen(source, timeout=None)

        # Speech to text
        st.subheader("Transcription:")
        try:
            text = speech_to_text(audio)
        except sr.UnknownValueError:
            st.warning("Speech recognition could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results from Google Speech Recognition service; {e}")

        # Auto summarization
        st.subheader("Auto Summarization:")
        try:
            summary = auto_summriztion(text)
        except Exception as e:
            st.error(f"Error in auto summarization: {e}")
    stop_recording = st.button("Stop Recording", disabled=not start_recording)
    if stop_recording:
        st.success("Recording stopped!")

if __name__ == "__main__":
    speech_to_text_and_summarize()
