# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Code that will impress u ;)
# HEADERS ================================================================
import pyttsx3
import pyttsx3.voice
# note: you might need "sudo apt install libespeak1" to make this work on linux

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def section(section_name:str = "SECTION") -> None:
	section_name = f"\n {section_name} {'-' * (40 - len(section_name))}\n"
	print(section_name)

# ========================================================================
# FUNCTIONS 
# ========================================================================

def check_voices(engine:pyttsx3.engine.Engine):
	section("CHECK VOICES")
	voices:list = engine.getProperty('voices')

	for index, voice in enumerate(voices):
		current_voice:pyttsx3.voice.Voice = voice
		print(f"Voice {index:04}: {current_voice.name} ({current_voice.id})")
	engine.setProperty('voice', voices[1].id)

def text_to_audio(engine:pyttsx3.engine.Engine, text:str = "Template script"):
	section("AUDIO")
	try:
		engine.save_to_file(text, "output.wav")
		engine.runAndWait()
	except Exception as e:
		print(f"Error: {e}")

# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")

	engine = pyttsx3.init()
	print(type(engine))
	
	check_voices(engine = engine)
	text_to_audio(engine=engine)

	section("END")