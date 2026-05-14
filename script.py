SCRIPT_DARG_AND_DROP = (
'''
    const source = arguments[0];
    const target = arguments[1];

    const dataTransfer = new DataTransfer();

    source.dispatchEvent(new DragEvent('dragstart', {
        bubbles: true,
        cancelable: true,
        dataTransfer: dataTransfer
    }));

    target.dispatchEvent(new DragEvent('dragenter', {
        bubbles: true,
        cancelable: true,
        dataTransfer: dataTransfer
    }));

    target.dispatchEvent(new DragEvent('dragover', {
        bubbles: true,
        cancelable: true,
        dataTransfer: dataTransfer
    }));

    target.dispatchEvent(new DragEvent('drop', {
        bubbles: true,
        cancelable: true,
        dataTransfer: dataTransfer
    }));

    source.dispatchEvent(new DragEvent('dragend', {
        bubbles: true,
        cancelable: true,
        dataTransfer: dataTransfer
    }));
'''
)