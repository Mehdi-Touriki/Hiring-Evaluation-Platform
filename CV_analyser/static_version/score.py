from math import sqrt, pow

def cosine_similarity(vector1: list[float], vector2: list[float]) -> float:
    """Returns the cosine of the angle between two vectors."""
    # the cosine similarity between two vectors is the dot product of the two vectors divided by the magnitude of each vector

    dot_product = 0
    magnitude_vector1 = 0
    magnitude_vector2 = 0

    vector1_length = len(vector1)
    vector2_length = len(vector2)

    if vector1_length > vector2_length:
        # fill vector2 with 0s until it is the same length as vector1 (required for dot product)
        vector2 = vector2 + [0] * (vector1_length - vector2_length)
    elif vector2_length > vector1_length:
        # fill vector1 with 0s until it is the same length as vector2 (required for dot product)
        vector1 = vector1 + [0] * (vector2_length - vector1_length)

    # dot product calculation
    for i in range(len(vector1)):
        dot_product += vector1[i] * vector2[i]

    # vector1 magnitude calculation
    for i in range(len(vector1)):
        magnitude_vector1 += pow(vector1[i], 2)

    # vector2 magnitude calculation
    for i in range(len(vector2)):
        magnitude_vector2 += pow(vector2[i], 2)

    # final magnitude calculation
    magnitude = sqrt(magnitude_vector1) * sqrt(magnitude_vector2)

    # return cosine similarity
    return dot_product / magnitude

