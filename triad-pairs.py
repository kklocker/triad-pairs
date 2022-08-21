import random

note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
note_idx = range(12)


triads: list = random.sample(note_idx, 6)

for note in triads:
    print(f"Note: {note_names[note]}")
