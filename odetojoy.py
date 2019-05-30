from typing import List, Tuple

from mido import Message, MidiFile, MidiTrack

from noteconv import to_note

beat_length: int = 200


def do_note(track, note: int, beats: float) -> None:
    time = int(beats*beat_length)
    if note is None:
        # a rest between notes
        track.append(Message('note_off', note=0, velocity=127, time=time))
    else:
        track.append(Message('note_on', note=note, velocity=127, time=0))
        track.append(Message('note_off', note=note, velocity=127, time=time))


def _main() -> None:
    mid = MidiFile(type=1)
    main_track = MidiTrack()
    chord_track = MidiTrack()
    mid.tracks.append(main_track)
    mid.tracks.append(chord_track)

    main_track.append(Message('program_change', program=12, time=0))
    chord_track.append(Message('program_change', program=12, time=0))

    main_notes: List[Tuple[int, float]] = [
        # 1st line

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

        # 2nd line

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

        # 3rd line

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
        (to_note('g', 4), 1),

        # 4th line

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
    for note, beats in main_notes:
        do_note(main_track, note, beats)

    chord_notes: List[Tuple[int, float]] = [
        # 1st line
        (to_note('c', 4), 4),
        (to_note('g', 3), 4),
        (to_note('c', 4), 4),
        (to_note('g', 3), 4),

        # 2nd line
        (to_note('c', 4), 4),
        (to_note('g', 3), 4),
        (to_note('c', 4), 4),
        (to_note('g', 3), 2),
        (to_note('c', 4), 2),

        # 3rd line
        (to_note('g', 3), 4),
        (to_note('g', 3), 4),
        (to_note('g', 3), 4),
        (to_note('g', 3), 4),

        # 4th line
        (to_note('c', 4), 4),
        (to_note('g', 3), 4),
        (to_note('c', 4), 4),
        (to_note('g', 3), 2),
        (to_note('c', 4), 2),
    ]
    for note, beats in chord_notes:
        do_note(chord_track, note, beats)

    mid.save('odetojoy.midi')


if __name__ == '__main__':
    _main()
