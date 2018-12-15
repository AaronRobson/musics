import inputs


def input_event_repr(input_event):
    return repr(
        (
            # input_event.device,
            # input_event.timestamp,
            # input_event.ev_type,
            input_event.code,
            input_event.state,
        )
    )


inputs.InputEvent.__repr__ = input_event_repr

while True:
    events = inputs.get_gamepad()
    for event in events:
        if event.ev_type != 'Sync':
            print('\t'.join([event.code, repr(event.state)]))
