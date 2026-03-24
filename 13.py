# Write a function that takes (01, 02, Li, La) and outputs (x, y) of the end effector.

import math
def forward_kinematics_2dof(q1, q2, l1, l2):
    """
    Calculates the end-effector (x, y) coordinates for a 2-DOF planar robot arm.
    Args:
    q1 (float): Angle of the first joint in radians.
    q2 (float): Angle of the second joint in radians (relative to the first link).
    l1 (float): Length of the first link.
    l2 (float): Length of the second link.
    Returns:
    tuple: A tuple containing the (x, y) coordinates of the end-effector.
    """
    x = l1 * math.cos(q1) + l2 * math.cos(q1 + q2)
    y = l1 * math.sin(q1) + l2 * math.sin(q1 + q2)
    return x, y
if __name__ == '__main__':
    # Example usage:
    q1_rad = math.pi / 4 # 45 degrees
    q2_rad = math.pi / 2 # 90 degrees
    link1_length = 1.0
    link2_length = 0.8
    end_effector_x, end_effector_y = forward_kinematics_2dof(q1_rad, q2_rad, link1_length, link2_length)
    print(f"End-effector X coordinate: {end_effector_x:.2f}")
    print(f"End-effector Y coordinate: {end_effector_y:.2f}")
    # Another example
    q1_rad_2 = 0
    q2_rad_2 = 0
    link1_length_2 = 1.0
    link2_length_2 = 1.0
    end_effector_x_2, end_effector_y_2 = forward_kinematics_2dof(q1_rad_2, q2_rad_2, link1_length_2, link2_length_2)
    print(f"\nEnd-effector X coordinate (second example): {end_effector_x_2:.2f}")
    print(f"End-effector Y coordinate (second example): {end_effector_y_2:.2f}")