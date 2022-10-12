def indexing_sequence(key, mask=0b111, shift=5):
    # in this case, linear proving uses index=(5*index+perturb+1)
    perturb = hash(key)
    # initial index is hash of key
    index = perturb & mask
    # only looks the last n bits (masking)
    yield index
    while True:
        perturb >>= shift
        index = (index * 5 + perturb + 1) & mask
        yield index
