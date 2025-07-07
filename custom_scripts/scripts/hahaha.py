import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math  # For rotation calculations

# --- 1. Schedule Data (remains the same) ---
schedule = {
    "07.07": {  # Monday
        "12:00~14:00": [
            {"person": "UH", "other_object_location": 1, "grape_target_location": 2, "episode_range": (600, 619),
             "other_object_type": "cabbage"},
            {"person": "UH", "other_object_location": 1, "grape_target_location": 3, "episode_range": (620, 639),
             "other_object_type": "cabbage"},
            {"person": "UH", "other_object_location": 1, "grape_target_location": 4, "episode_range": (640, 659),
             "other_object_type": "cabbage"},
            {"person": "UH", "other_object_location": 1, "grape_target_location": 5, "episode_range": (660, 679),
             "other_object_type": "cabbage"},
            {"person": "UH", "other_object_location": 1, "grape_target_location": 6, "episode_range": (680, 699),
             "other_object_type": "cabbage"},
        ],
        "14:00~16:00": [
            {"person": "MJ", "other_object_location": 2, "grape_target_location": 1, "episode_range": (700, 719),
             "other_object_type": "cabbage"},
            {"person": "MJ", "other_object_location": 2, "grape_target_location": 3, "episode_range": (720, 739),
             "other_object_type": "cabbage"},
            {"person": "MJ", "other_object_location": 2, "grape_target_location": 4, "episode_range": (740, 759),
             "other_object_type": "cabbage"},
            {"person": "MJ", "other_object_location": 2, "grape_target_location": 5, "episode_range": (760, 779),
             "other_object_type": "cabbage"},
            {"person": "MJ", "other_object_location": 2, "grape_target_location": 6, "episode_range": (780, 799),
             "other_object_type": "cabbage"},
        ],
        "16:00~18:00": [
            {"person": "DH", "other_object_location": 3, "grape_target_location": 1, "episode_range": (800, 819),
             "other_object_type": "cabbage"},
            {"person": "DH", "other_object_location": 3, "grape_target_location": 2, "episode_range": (820, 839),
             "other_object_type": "cabbage"},
            {"person": "DH", "other_object_location": 3, "grape_target_location": 4, "episode_range": (840, 859),
             "other_object_type": "cabbage"},
            {"person": "DH", "other_object_location": 3, "grape_target_location": 5, "episode_range": (860, 879),
             "other_object_type": "cabbage"},
            {"person": "DH", "other_object_location": 3, "grape_target_location": 6, "episode_range": (880, 899),
             "other_object_type": "cabbage"},
        ],
        "18:00~20:00": [
            {"person": "KH", "other_object_location": 4, "grape_target_location": 1, "episode_range": (900, 919),
             "other_object_type": "cabbage"},
            {"person": "KH", "other_object_location": 4, "grape_target_location": 2, "episode_range": (920, 939),
             "other_object_type": "cabbage"},
            {"person": "KH", "other_object_location": 4, "grape_target_location": 3, "episode_range": (940, 959),
             "other_object_type": "cabbage"},
            {"person": "KH", "other_object_location": 4, "grape_target_location": 5, "episode_range": (960, 979),
             "other_object_type": "cabbage"},
            {"person": "KH", "other_object_location": 4, "grape_target_location": 6, "episode_range": (980, 999),
             "other_object_type": "cabbage"},
        ],
    },
    "07.08": {  # Tuesday
        "12:00~14:00": [
            {"person": "SY", "other_object_location": 5, "grape_target_location": 1, "episode_range": (1000, 1019),
             "other_object_type": "cabbage"},
            {"person": "SY", "other_object_location": 5, "grape_target_location": 2, "episode_range": (1020, 1039),
             "other_object_type": "cabbage"},
            {"person": "SY", "other_object_location": 5, "grape_target_location": 3, "episode_range": (1040, 1059),
             "other_object_type": "cabbage"},
            {"person": "SY", "other_object_location": 5, "grape_target_location": 4, "episode_range": (1060, 1079),
             "other_object_type": "cabbage"},
            {"person": "SY", "other_object_location": 5, "grape_target_location": 6, "episode_range": (1080, 1099),
             "other_object_type": "cabbage"},
        ],
        "14:00~16:00": [
            {"person": "MJ", "other_object_location": 6, "grape_target_location": 1, "episode_range": (1100, 1119),
             "other_object_type": "cabbage"},
            {"person": "MJ", "other_object_location": 6, "grape_target_location": 2, "episode_range": (1120, 1139),
             "other_object_type": "cabbage"},
            {"person": "MJ", "other_object_location": 6, "grape_target_location": 3, "episode_range": (1140, 1159),
             "other_object_type": "cabbage"},
            {"person": "MJ", "other_object_location": 6, "grape_target_location": 4, "episode_range": (1160, 1179),
             "other_object_type": "cabbage"},
            {"person": "MJ", "other_object_location": 6, "grape_target_location": 5, "episode_range": (1180, 1199),
             "other_object_type": "cabbage"},
        ],
        "16:00~18:00": [
            {"person": "KH", "other_object_location": 1, "grape_target_location": 2, "episode_range": (1200, 1219),
             "other_object_type": "corn"},
            {"person": "KH", "other_object_location": 1, "grape_target_location": 3, "episode_range": (1220, 1239),
             "other_object_type": "corn"},
            {"person": "KH", "other_object_location": 1, "grape_target_location": 4, "episode_range": (1240, 1259),
             "other_object_type": "corn"},
            {"person": "KH", "other_object_location": 1, "grape_target_location": 5, "episode_range": (1260, 1279),
             "other_object_type": "corn"},
            {"person": "KH", "other_object_location": 1, "grape_target_location": 6, "episode_range": (1280, 1299),
             "other_object_type": "corn"},
        ],
        "18:00~20:00": [
            {"person": "DH", "other_object_location": 2, "grape_target_location": 1, "episode_range": (1300, 1319),
             "other_object_type": "corn"},
            {"person": "DH", "other_object_location": 2, "grape_target_location": 3, "episode_range": (1320, 1339),
             "other_object_type": "corn"},
            {"person": "DH", "other_object_location": 2, "grape_target_location": 4, "episode_range": (1340, 1359),
             "other_object_type": "corn"},
            {"person": "DH", "other_object_location": 2, "grape_target_location": 5, "episode_range": (1360, 1379),
             "other_object_type": "corn"},
            {"person": "DH", "other_object_location": 2, "grape_target_location": 6, "episode_range": (1380, 1399),
             "other_object_type": "corn"},
        ],
    },
    "07.09": {  # Wednesday
        "12:00~14:00": [
            {"person": "SY", "other_object_location": 3, "grape_target_location": 1, "episode_range": (1400, 1419),
             "other_object_type": "corn"},
            {"person": "SY", "other_object_location": 3, "grape_target_location": 2, "episode_range": (1420, 1439),
             "other_object_type": "corn"},
            {"person": "SY", "other_object_location": 3, "grape_target_location": 4, "episode_range": (1440, 1459),
             "other_object_type": "corn"},
            {"person": "SY", "other_object_location": 3, "grape_target_location": 5, "episode_range": (1460, 1479),
             "other_object_type": "corn"},
            {"person": "SY", "other_object_location": 3, "grape_target_location": 6, "episode_range": (1480, 1499),
             "other_object_type": "corn"},
        ],
        "14:00~16:00": [
            {"person": "UH", "other_object_location": 4, "grape_target_location": 1, "episode_range": (1500, 1519),
             "other_object_type": "corn"},
            {"person": "UH", "other_object_location": 4, "grape_target_location": 2, "episode_range": (1520, 1539),
             "other_object_type": "corn"},
            {"person": "UH", "other_object_location": 4, "grape_target_location": 3, "episode_range": (1540, 1559),
             "other_object_type": "corn"},
            {"person": "UH", "other_object_location": 4, "grape_target_location": 5, "episode_range": (1560, 1579),
             "other_object_type": "corn"},
            {"person": "UH", "other_object_location": 4, "grape_target_location": 6, "episode_range": (1580, 1599),
             "other_object_type": "corn"},
        ],
        "16:00~18:00": [
            {"person": "MJ", "other_object_location": 5, "grape_target_location": 1, "episode_range": (1600, 1619),
             "other_object_type": "corn"},
            {"person": "MJ", "other_object_location": 5, "grape_target_location": 2, "episode_range": (1620, 1639),
             "other_object_type": "corn"},
            {"person": "MJ", "other_object_location": 5, "grape_target_location": 3, "episode_range": (1640, 1659),
             "other_object_type": "corn"},
            {"person": "MJ", "other_object_location": 5, "grape_target_location": 4, "episode_range": (1660, 1679),
             "other_object_type": "corn"},
            {"person": "MJ", "other_object_location": 5, "grape_target_location": 6, "episode_range": (1680, 1699),
             "other_object_type": "corn"},
        ],
        "18:00~20:00": [
            {"person": "DH", "other_object_location": 6, "grape_target_location": 1, "episode_range": (1700, 1719),
             "other_object_type": "corn"},
            {"person": "DH", "other_object_location": 6, "grape_target_location": 2, "episode_range": (1720, 1739),
             "other_object_type": "corn"},
            {"person": "DH", "other_object_location": 6, "grape_target_location": 3, "episode_range": (1740, 1759),
             "other_object_type": "corn"},
            {"person": "DH", "other_object_location": 6, "grape_target_location": 4, "episode_range": (1760, 1779),
             "other_object_type": "corn"},
            {"person": "DH", "other_object_location": 6, "grape_target_location": 5, "episode_range": (1780, 1799),
             "other_object_type": "corn"},
        ],
    },
    "07.10": {  # Thursday - 'X' column indicates no specific object, so we'll use a generic "other_object_type"
        "12:00~14:00": [
            {"person": "SY", "other_object_location": None, "grape_target_location": 1, "episode_range": (1800, 1819),
             "other_object_type": "X"},
            {"person": "SY", "other_object_location": None, "grape_target_location": 2, "episode_range": (1820, 1839),
             "other_object_type": "X"},
            {"person": "SY", "other_object_location": None, "grape_target_location": 3, "episode_range": (1840, 1859),
             "other_object_type": "X"},
            {"person": "SY", "other_object_location": None, "grape_target_location": 4, "episode_range": (1860, 1879),
             "other_object_type": "X"},
            {"person": "SY", "other_object_location": None, "grape_target_location": 5, "episode_range": (1880, 1899),
             "other_object_type": "X"},

        ],
        "14:00~16:00": [
            {"person": "KH", "other_object_location": None, "grape_target_location": 6, "episode_range": (1900, 1919),
            "other_object_type": "X"},
            {"person": "KH", "other_object_location": None, "grape_target_location": 1, "episode_range": (1920, 1939),
             "other_object_type": "X"},
            {"person": "KH", "other_object_location": None, "grape_target_location": 2, "episode_range": (1940, 1959),
             "other_object_type": "X"},
            {"person": "KH", "other_object_location": None, "grape_target_location": 3, "episode_range": (1960, 1979),
             "other_object_type": "X"},
            {"person": "KH", "other_object_location": None, "grape_target_location": 4, "episode_range": (1980, 1999),
             "other_object_type": "X"},

        ],
        "16:00~18:00": [
            {"person": "UH", "other_object_location": None, "grape_target_location": 5, "episode_range": (2000, 2019),
             "other_object_type": "X"},
            {"person": "UH", "other_object_location": None, "grape_target_location": 6, "episode_range": (2020, 2039),
             "other_object_type": "X"},
            {"person": "UH", "other_object_location": None, "grape_target_location": 1, "episode_range": (2040, 2059),
             "other_object_type": "X"},
            {"person": "UH", "other_object_location": None, "grape_target_location": 2, "episode_range": (2060, 2079),
             "other_object_type": "X"},
            {"person": "UH", "other_object_location": None, "grape_target_location": 3, "episode_range": (2080, 2099),
             "other_object_type": "X"},

        ],
        "18:00~20:00": [
            {"person": "MJ", "other_object_location": None, "grape_target_location": 4, "episode_range": (2100, 2119),
             "other_object_type": "X"},
            {"person": "MJ", "other_object_location": None, "grape_target_location": 5, "episode_range": (2120, 2139),
             "other_object_type": "X"},
            {"person": "MJ", "other_object_location": None, "grape_target_location": 6, "episode_range": (2140, 2159),
             "other_object_type": "X"},
        ],  # This slot is empty in the image, so no data for now
    },
    "07.11": {  # Friday - Placeholder, no data yet in the image for X, Grape, and Episode
        "12:00~14:00": [],
        "14:00~16:00": [],
        "16:00~18:00": [],
        "18:00~20:00": [],
    }
}


# --- 2. Visualization Function ---

def get_grid_coords(area_number):
    """
    Returns the (x, y) coordinates of the bottom-left corner of the given area
    and its width and height for a 3x2 grid.
    Grid layout:
    1 2 3
    4 5 6
    """
    # Assuming a grid where each cell is 1 unit wide and 1 unit tall
    # Mapping area numbers to grid positions (col, row)
    mapping = {
        1: (0, 1), 2: (1, 1), 3: (2, 1),  # Top row (y=1)
        4: (0, 0), 5: (1, 0), 6: (2, 0)  # Bottom row (y=0)
    }
    col, row = mapping[area_number]
    return col, row, 1, 1  # x, y, width, height


def draw_grape_pattern(ax, sub_area_coords, pattern_index):
    """
    Draws a specific pattern of grapes within a given sub-area.
    sub_area_coords: (x, y, width, height) of the sub-area.
    pattern_index: 0 to 4 (representing 5 unique patterns from the provided images).
    """
    x_sub, y_sub, w_sub, h_sub = sub_area_coords

    # Calculate center of the sub-area
    center_x_sub = x_sub + w_sub / 2
    center_y_sub = y_sub + h_sub / 2

    # Relative dimensions for the rectangle and triangle within the sub-area
    common_rect_w = w_sub * 0.4
    common_rect_h = h_sub * 0.7

    common_tri_base = common_rect_w * 0.8
    common_tri_height = h_sub * 0.2

    # Helper function to rotate a point (px, py) around an origin (ox, oy) by an angle (degrees)
    def rotate_point(px, py, ox, oy, angle_deg):
        angle_rad = math.radians(angle_deg)
        qx = ox + math.cos(angle_rad) * (px - ox) - math.sin(angle_rad) * (py - oy)
        qy = oy + math.sin(angle_rad) * (px - ox) + math.cos(angle_rad) * (py - oy)
        return qx, qy

    # --- Draw specific pattern based on pattern_index ---
    if pattern_index == 0:  # image_d16de0.png: Vertical rectangle, triangle pointing up
        rect_width = common_rect_w
        rect_height = common_rect_h
        rect_coords = (center_x_sub - rect_width / 2, center_y_sub - rect_height / 2)
        rect_angle = 0

        # Triangle: base centered at top of rectangle, pointing up
        tri_points = [
            (center_x_sub - common_tri_base / 2, rect_coords[1] + rect_height),
            (center_x_sub + common_tri_base / 2, rect_coords[1] + rect_height),
            (center_x_sub, rect_coords[1] + rect_height + common_tri_height)
        ]

        # Draw the rectangle and triangle for pattern 0
        rect_patch = patches.Rectangle(rect_coords, rect_width, rect_height,
                                       angle=rect_angle, rotation_point='center',
                                       color='purple', alpha=0.9, edgecolor='purple', linewidth=1.5)
        ax.add_patch(rect_patch)
        tri_patch = patches.Polygon(tri_points, closed=True, color='green', alpha=0.9, edgecolor='green', linewidth=1.5)
        ax.add_patch(tri_patch)

    elif pattern_index == 1:  # image_d16dbc.png: Vertical rectangle, triangle pointing down
        rect_width = common_rect_w
        rect_height = common_rect_h
        rect_coords = (center_x_sub - rect_width / 2, center_y_sub - rect_height / 2)
        rect_angle = 0

        # Triangle: base centered at bottom of rectangle, pointing down
        tri_points = [
            (center_x_sub - common_tri_base / 2, rect_coords[1]),
            (center_x_sub + common_tri_base / 2, rect_coords[1]),
            (center_x_sub, rect_coords[1] - common_tri_height)
        ]

        # Draw the rectangle and triangle for pattern 1
        rect_patch = patches.Rectangle(rect_coords, rect_width, rect_height,
                                       angle=rect_angle, rotation_point='center',
                                       color='purple', alpha=0.9, edgecolor='purple', linewidth=1.5)
        ax.add_patch(rect_patch)
        tri_patch = patches.Polygon(tri_points, closed=True, color='green', alpha=0.9, edgecolor='green', linewidth=1.5)
        ax.add_patch(tri_patch)

    elif pattern_index == 2:  # image_d16da2.png: Horizontal rectangle, triangle pointing right
        rect_width = common_rect_h  # Swap dimensions for horizontal
        rect_height = common_rect_w
        rect_coords = (center_x_sub - rect_width / 2, center_y_sub - rect_height / 2)
        rect_angle = 0

        # Triangle: base centered at right of rectangle, pointing right
        tri_points = [
            (rect_coords[0] + rect_width, center_y_sub - common_tri_base / 2),
            (rect_coords[0] + rect_width, center_y_sub + common_tri_base / 2),
            (rect_coords[0] + rect_width + common_tri_height, center_y_sub)
        ]

        # Draw the rectangle and triangle for pattern 2
        rect_patch = patches.Rectangle(rect_coords, rect_width, rect_height,
                                       angle=rect_angle, rotation_point='center',
                                       color='purple', alpha=0.9, edgecolor='purple', linewidth=1.5)
        ax.add_patch(rect_patch)
        tri_patch = patches.Polygon(tri_points, closed=True, color='green', alpha=0.9, edgecolor='green', linewidth=1.5)
        ax.add_patch(tri_patch)

    elif pattern_index == 3:  # image_d16d84.png: Diagonal rectangle (-45 deg), triangle pointing top-right
        rect_width = common_rect_w * 1.0
        rect_height = common_rect_h * 1.0
        rect_angle = -45

        bl_dx_unrotated = -rect_width / 2
        bl_dy_unrotated = -rect_height / 2

        rot_bl_dx = bl_dx_unrotated * math.cos(math.radians(rect_angle)) - bl_dy_unrotated * math.sin(
            math.radians(rect_angle))
        rot_bl_dy = bl_dx_unrotated * math.sin(math.radians(rect_angle)) + bl_dy_unrotated * math.cos(
            math.radians(rect_angle))

        rect_coords = (center_x_sub + rot_bl_dx, center_y_sub + rot_bl_dy)

        # Calculate the actual rotated top-right corner of the rectangle
        corner_x_rot = center_x_sub + rect_width / 2 * math.cos(math.radians(rect_angle)) - rect_height / 2 * math.sin(
            math.radians(rect_angle))
        corner_y_rot = center_y_sub + rect_width / 2 * math.sin(math.radians(rect_angle)) + rect_height / 2 * math.cos(
            math.radians(rect_angle))

        tri_rot_angle = rect_angle + 90  # Triangle's base is perpendicular to rectangle's end

        tri_points_relative = [
            (-common_tri_base / 2, 0),
            (common_tri_base / 2, 0),
            (0, common_tri_height)
        ]

        tri_points = []
        for px, py in tri_points_relative:
            rx, ry = rotate_point(px, py, 0, 0, tri_rot_angle)
            tri_points.append((corner_x_rot + rx, corner_y_rot + ry))

        # Draw the rectangle and triangle for pattern 3
        rect_patch = patches.Rectangle(rect_coords, rect_width, rect_height,
                                       angle=rect_angle, rotation_point='center',
                                       color='purple', alpha=0.9, edgecolor='purple', linewidth=1.5)
        ax.add_patch(rect_patch)
        tri_patch = patches.Polygon(tri_points, closed=True, color='green', alpha=0.9, edgecolor='green', linewidth=1.5)
        ax.add_patch(tri_patch)


    elif pattern_index == 4:  # New Pattern: Square with "Rand" text
        square_size = min(w_sub, h_sub) * 0.7  # Make it a clear square within the sub-area
        square_coords = (center_x_sub - square_size / 2, center_y_sub - square_size / 2)

        # Draw the square (can be purple or any other color)
        square_patch = patches.Rectangle(square_coords, square_size, square_size,
                                         color='purple', alpha=0.9, edgecolor='purple', linewidth=1.5)
        ax.add_patch(square_patch)

        # Add "Rand" text in the center of the square
        ax.text(center_x_sub, center_y_sub, "Rand", ha='center', va='center',
                fontsize=min(w_sub, h_sub) * 0.2, color='white', fontweight='bold')


def visualize_placement(episode_number):
    found_entry = None
    # Iterate through the schedule to find the correct entry for the given episode number
    for day, time_slots in schedule.items():
        for time_slot, entries in time_slots.items():
            for entry in entries:
                if entry and entry["episode_range"][0] <= episode_number <= entry["episode_range"][1]:
                    found_entry = entry
                    current_day = day
                    current_time_slot = time_slot
                    break
            if found_entry:
                break
        if found_entry:
            break

    if not found_entry:
        print(f"Episode number {episode_number} not found in the schedule.")
        return

    other_object_location = found_entry["other_object_location"]
    grape_target_location = found_entry["grape_target_location"]
    other_object_type = found_entry["other_object_type"]
    episode_range_start = found_entry["episode_range"][0]
    person = found_entry["person"]  # Get person's name

    # Calculate grape sub-area and pattern index
    # (episode_number - episode_range_start) gives an index from 0 to 19
    relative_episode_index = episode_number - episode_range_start
    sub_area_index = relative_episode_index // 5  # 0, 1, 2, 3 (for TL, TR, BL, BR)
    grape_orientation_index = relative_episode_index % 5  # 0, 1, 2, 3, 4 (for 5 patterns)

    fig, ax = plt.subplots(figsize=(9, 6))  # Adjust figure size for 3x2 grid

    # Draw the main 3x2 grid
    for i in range(1, 7):
        x, y, w, h = get_grid_coords(i)
        rect = patches.Rectangle((x, y), w, h, linewidth=1, edgecolor='black', facecolor='none')
        ax.add_patch(rect)
        ax.text(x + w / 2, y + h / 2, str(i), ha='center', va='center', fontsize=20, color='gray')

    # Place the "other" object
    if other_object_location is not None:
        obj_x, obj_y, obj_w, obj_h = get_grid_coords(other_object_location)
        if other_object_type == "cabbage":
            ax.add_patch(patches.Circle((obj_x + obj_w / 2, obj_y + obj_h / 2), obj_w * 0.3, color='green', alpha=0.7))
            ax.text(obj_x + obj_w / 2, obj_y + obj_h / 2, "Cabbage", ha='center', va='center', color='white',
                    fontsize=10, fontweight='bold')
        elif other_object_type == "corn":
            ax.add_patch(
                patches.Rectangle((obj_x + obj_w * 0.3, obj_y + obj_h * 0.2), obj_w * 0.4, obj_h * 0.6, color='gold',
                                  alpha=0.7))
            ax.text(obj_x + obj_w / 2, obj_y + obj_h / 2, "Corn", ha='center', va='center', color='black', fontsize=10,
                    fontweight='bold')
        else:  # Generic 'X' or unspecified (for Thursday/Friday)
            ax.add_patch(
                patches.Circle((obj_x + obj_w / 2, obj_y + obj_h / 2), obj_w * 0.3, color='lightgray', alpha=0.7))
            ax.text(obj_x + obj_w / 2, obj_y + obj_h / 2, "X", ha='center', va='center', color='black', fontsize=10,
                    fontweight='bold')

    # Place the grapes in the target area
    grape_x, grape_y, grape_w, grape_h = get_grid_coords(grape_target_location)

    # Draw a highlight rectangle for the grape target area
    highlight_rect = patches.Rectangle((grape_x, grape_y), grape_w, grape_h, linewidth=2, edgecolor='red',
                                       facecolor='none', linestyle='--')
    ax.add_patch(highlight_rect)

    # Define sub-area coordinates within the grape target location (TL, TR, BL, BR)
    # These are 0-indexed: 0=TL, 1=TR, 2=BL, 3=BR
    sub_area_coords_list = [
        (grape_x, grape_y + grape_h / 2, grape_w / 2, grape_h / 2),  # Top-Left (Sub-area 1)
        (grape_x + grape_w / 2, grape_y + grape_h / 2, grape_w / 2, grape_h / 2),  # Top-Right (Sub-area 2)
        (grape_x, grape_y, grape_w / 2, grape_h / 2),  # Bottom-Left (Sub-area 3)
        (grape_x + grape_w / 2, grape_y, grape_w / 2, grape_h / 2)  # Bottom-Right (Sub-area 4)
    ]

    # Draw the sub-grid lines for the target grape area
    ax.plot([grape_x + grape_w / 2, grape_x + grape_w / 2], [grape_y, grape_y + grape_h], color='gray', linestyle=':',
            linewidth=0.5)
    ax.plot([grape_x, grape_x + grape_w], [grape_y + grape_h / 2, grape_y + grape_h / 2], color='gray', linestyle=':',
            linewidth=0.5)

    # Draw the specific grape pattern in the determined sub-area
    draw_grape_pattern(ax, sub_area_coords_list[sub_area_index], grape_orientation_index)

    # Add actual sub-area numbers at the corners for clarity as per the example image
    ax.text(grape_x + grape_w / 4, grape_y + grape_h * 3 / 4, "1", ha='center', va='center', fontsize=10,
            color='darkred')
    ax.text(grape_x + grape_w * 3 / 4, grape_y + grape_h * 3 / 4, "2", ha='center', va='center', fontsize=10,
            color='darkred')
    ax.text(grape_x + grape_w / 4, grape_y + grape_h / 4, "3", ha='center', va='center', fontsize=10, color='darkred')
    ax.text(grape_x + grape_w * 3 / 4, grape_y + grape_h / 4, "4", ha='center', va='center', fontsize=10,
            color='darkred')

    ax.set_xlim(-0.5, 3.5)  # 3 columns wide
    ax.set_ylim(-0.5, 2.5)  # 2 rows tall
    ax.set_aspect('equal', adjustable='box')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(
        f"Episode {episode_number} Placement\nDay: {current_day}, Time: {current_time_slot}, Person: {person}\n"
        f"Other Object in Area {other_object_location if other_object_location else 'None'}, Grapes in Area {grape_target_location} (Sub-area {sub_area_index + 1}, Pattern {grape_orientation_index + 1})")
    plt.grid(False)
    plt.show()


# --- 3. Example Usage ---
# Test with episode 600 (first in range)
# relative_episode_index = 0. sub_area_index = 0 (TL), grape_orientation_index = 0.
# Expected: Sub-area 1 (TL), Pattern 1 (vertical up)
for i in range(1000, 1400):
    visualize_placement(i)


