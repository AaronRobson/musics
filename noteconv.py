base_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def to_note(base_note, octave=5):
    '''http://www.electronics.dit.ie/staff/tscarff/Music_technology/midi/midi_note_numbers_for_octaves.htm
    '''
    if not (0 <= octave <= 10):
        raise ValueError('octave {} is out of range'.format(octave))

    base_note = base_note.upper()
    if base_note not in base_notes:
        raise ValueError('base_note {} is not an accepted {}.'.format(repr(base_note), repr(base_notes)))
    
    output = base_notes.index(base_note) + (octave * len(base_notes))
    assert 0 <= output <= 127, output
    return output