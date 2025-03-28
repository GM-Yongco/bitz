# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Code that will impress u ;)
# HEADERS ================================================================
from gtts import gTTS
from pydub import AudioSegment
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

def text_to_audio(text:str = "Template script", file_name:str = "template.mp4"):
	tts_au = gTTS(text, lang="en", tld="co.uk")
	tts_au.save(file_name)

def speed(file_name:str = "template.mp4"):
	audio:AudioSegment = AudioSegment.from_file("au.mp3")
	faster_audio = audio.speedup(playback_speed=1.5)

	# Save the faster audio
	faster_audio.export("faster.mp3", format="mp3")

	# Slow down (0.75x speed)
	slower_audio = audio.speedup(playback_speed=0.75)
	slower_audio.export("slower.mp3", format="mp3")


# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")

	new_text = "In machine learning, a common problem is the high dimensionality of the data; the datasets which we use contain huge data and sometimes we cannot view that data even in 3D, which is also called the curse of dimensionality [12]. So, when we perform operations on this data, we require a huge amount of memory, and sometimes the data can also grow exponentially and overfitting can happen. *e weighting features can be used, so the redundancy in the dataset can be decreased which in turn also helps in decreasing the pro- cessing time of the execution [13–17]. For decreasing the dimensionality of the dataset, there are various feature engineering and feature selection techniques which can be used to remove that data not having that much importance in the dataset"
	text_to_audio(text=new_text)


	section("END")