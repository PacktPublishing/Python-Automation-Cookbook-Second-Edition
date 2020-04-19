PI = 3.14159


def rectangle(sideA, sideB):
    return sideA * sideB


def circle(radius):
    return 2 * PI * radius


def calculate_area(shape, sizeA, sizeB=0):
    if sizeA <= 0:
        raise ValueError('sizeA needs to be positive')

    if sizeB < 0:
        raise ValueError('sizeB needs to be positive')

    if shape == 'SQUARE':
        return rectangle(sizeA, sizeA)

    if shape == 'RECTANGLE':
        return rectangle(sizeA, sizeB)

    if shape == 'CIRCLE':
        return circle(sizeA)

    raise Exception(f'Shape {shape} not defined')
