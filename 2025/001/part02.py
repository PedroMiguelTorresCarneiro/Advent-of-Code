def compute_password_click_method(rotations):
    """
    Computes the number of times a single click (unit movement of the dial)
    causes the dial to point at 0.

    The dial:
      - has values from 0 to 99 (mod 100),
      - starts at position 50,
      - 'Rk' = rotate k steps towards higher numbers,
      - 'Lk' = rotate k steps towards lower numbers.

    Each unit step (click) is counted; if the dial lands on 0 after that step,
    the counter is incremented.
    """
    position = 50
    zero_clicks = 0

    for r in rotations:
        r = r.strip()
        if not r:
            continue

        direction = r[0]
        distance = int(r[1:])

        # Step is +1 for R, -1 for L
        step = 1 if direction == "R" else -1

        for _ in range(distance):
            position = (position + step) % 100
            if position == 0:
                zero_clicks += 1

    return zero_clicks


if __name__ == "__main__":
    # Read the puzzle input (one rotation per line)
    with open("input.txt") as f:
        rotations = f.readlines()

    password = compute_password_click_method(rotations)
    print(password)
