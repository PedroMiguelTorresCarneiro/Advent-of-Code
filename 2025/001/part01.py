def compute_password(rotations):
    """
    Computes the number of times the dial points at 0 after applying
    each rotation in the sequence. The dial has values 0–99 and starts at 50.
    """
    position = 50
    zero_count = 0

    for r in rotations:
        direction = r[0]
        value = int(r[1:])

        if direction == "R":
            position = (position + value) % 100
        else:  # direction == "L"
            position = (position - value) % 100

        if position == 0:
            zero_count += 1

    return zero_count


# --- Leitura de input do ficheiro ---
if __name__ == "__main__":
    with open("input.txt") as f:
        rotations = [line.strip() for line in f if line.strip()]

    print(compute_password(rotations))
