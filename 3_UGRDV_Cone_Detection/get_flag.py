#!/usr/bin/env python3

def ugrdv_challenge_3(left_frame, right_frame):
    """Calculate mean of two arrays of x and y coordinates (as floats)

    Args:
        left_frame (array of tuples): x and y coordinates (as floats) from left frame
        right_frame (array of tuples): x and y coordinates (as floats) from right frame

    Returns:
        array of tuples: mean x and y coordinates of both frames
    """
    mean_coords = []
    n_coords = len(right_frame)

    for i in range(0, len(right_frame)):
        mean_x = (right_frame[i][0] + left_frame[i][0]) / 2
        mean_y = (right_frame[i][1] + left_frame[i][1]) / 2
        mean_coords.append((mean_x, mean_y))
    
    return mean_coords


# driver code
if __name__ == "__main__":
    # using challenge example
    right_frame = [(3.0, 9.0), (12.0, 16.0)]
    left_frame = [(4.0, 10.0), (13.0, 17.0)]
    print(ugrdv_challenge_3(right_frame, left_frame))  # [(3.5, 9.5), (12.5, 16.5)]