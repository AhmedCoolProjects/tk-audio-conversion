import librosa
import soundfile as sf
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

root = tk.Tk()
root.geometry("550x600")

def pitch_shift():
    # Load audio file
    y, sr = librosa.load(original_file)

    # Change pitch by n_steps semitones
    y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=n_steps.get())

    # Save the modified audio
    sf.write("modified_audio.wav", y_shifted, sr)
    play_button.config(state='normal')
    
def upload_audio():
    global original_file
    original_file = filedialog.askopenfilename()
    if original_file:
        shift_button.config(state='normal')

def play_audio():
    y, sr = librosa.load("modified_audio.wav")
    librosa.display.waveplot(y, sr=sr)
    plt.show()

def change_n_steps():
    global n_steps
    n_steps = tk.Entry(root)
    n_steps.pack()

upload_button = tk.Button(root, text="Upload audio", command=upload_audio)
upload_button.pack()

shift_button = tk.Button(root, text="Shift Pitch", command=pitch_shift, state='disable')
shift_button.pack()

play_button = tk.Button(root, text="Play audio", command=play_audio, state='disable')
play_button.pack()

change_button = tk.Button(root, text="Change n_steps", command=change_n_steps)
change_button.pack()

root.mainloop()
