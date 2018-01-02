from mido import Message, MidiFile, MidiTrack

from noteconv import to_note

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=12, time=0))

beat_length = 200

def do_note(note, beats):
    time = int(beats*beat_length)
    if note is None:
        #rest
        track.append(Message('note_off', note=0, velocity=127, time=time))
    else:
        track.append(Message('note_on', note=note, velocity=127, time=0))
        track.append(Message('note_off', note=note, velocity=127, time=time))

notes = [
    #1st line

    (to_note('e'), 1),
    (to_note('e'), 1),
    (to_note('f'), 1),
    (to_note('g'), 1),

    (to_note('g'), 1),
    (to_note('f'), 1),
    (to_note('e'), 1),
    (to_note('d'), 1),

    (to_note('c'), 1),
    (to_note('c'), 1),
    (to_note('d'), 1),
    (to_note('e'), 1),

    (to_note('e'), 1.5),
    (to_note('d'), 0.5),
    (to_note('d'), 2),

    #2nd line

    (to_note('e'), 1),
    (to_note('e'), 1),
    (to_note('f'), 1),
    (to_note('g'), 1),

    (to_note('g'), 1),
    (to_note('f'), 1),
    (to_note('e'), 1),
    (to_note('d'), 1),

    (to_note('c'), 1),
    (to_note('c'), 1),
    (to_note('d'), 1),
    (to_note('e'), 1),

    (to_note('d'), 1.5),
    (to_note('c'), 0.5),
    (to_note('c'), 2),

    #3rd line

    (to_note('d'), 1),
    (to_note('d'), 1),
    (to_note('e'), 1),
    (to_note('c'), 1),

    (to_note('d'), 1),
    (to_note('e'), 0.5),
    (to_note('f'), 0.5),
    (to_note('e'), 1),
    (to_note('c'), 1),

    (to_note('d'), 1),
    (to_note('e'), 0.5),
    (to_note('f'), 0.5),
    (to_note('e'), 1),
    (to_note('d'), 1),

    (to_note('c'), 1),
    (to_note('d'), 1),
    (to_note('g', 4), 1), #(None, 2),

    #4th line

    (to_note('e'), 1),
    (to_note('e'), 1),
    (to_note('f'), 1),
    (to_note('g'), 1),

    (to_note('g'), 1),
    (to_note('f'), 1),
    (to_note('e'), 1),
    (to_note('d'), 1),

    (to_note('c'), 1),
    (to_note('c'), 1),
    (to_note('d'), 1),
    (to_note('e'), 1),

    (to_note('d'), 1.5),
    (to_note('c'), 0.5),
    (to_note('c'), 2),
]
for note, beats in notes:
    do_note(note, beats)

mid.save('odetojoy.midi')
