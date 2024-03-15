import win32com.client as w


speaker = w.Dispatch("SAPI.SpVoice")

l = ["Angela", "Rabi", "Sen"]

for names in l:

    speaker.Speak(f" Hello, Shout out to {names}")


