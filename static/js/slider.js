var granimInstance = new Granim({
    element: '#canvas-basic',
    direction: 'left-right',
    isPausedWhenNotInView: true,
    states: {
        "default-state": {
            gradients: [
                ['#fff', '#e9e6f6'],
                ['#e9e6f6', '#d2cced']
            ]
        }
    }
});