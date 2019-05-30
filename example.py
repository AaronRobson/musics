from mido import Message, MidiFile, MidiTrack


def _main() -> None:
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    track.append(Message('program_change', program=12, time=0))
    track.append(Message('note_on', note=64, velocity=64, time=32))
    track.append(Message('note_off', note=64, velocity=127, time=32))

    mid.save('new_song.mid')


if __name__ == '__main__':
    _main()
