import win32com.client as w

speaker = w.Dispatch("SAPI.SpVoice")

l = ["Anjalica", "Licaa", "Shiro"]

for name in l:
    speaker.Speak(f"Hello {name}")



