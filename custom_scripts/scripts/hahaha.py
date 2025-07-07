import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math  # For rotation calculations

# --- 1. Schedule Data (remains the same) ---
schedule = {
    "07.07": {  # Monday
        "12:00~14:00": [
            {"person": "웅희", "other_object_location": 1, "grape_target_location": 2, "episode_range": (600, 619),
             "other_object_type": "cabbage"},
            {"person": "웅희", "other_object_location": 1, "grape_target_location": 3, "episode_range": (620, 639),
             "other_object_type": "cabbage"},
            {"person": "웅희", "other_object_location": 1, "grape_target_location": 4, "episode_range": (640, 659),
             "other_object_type": "cabbage"},
            {"person": "웅희", "other_object_location": 1, "grape_target_location": 5, "episode_range": (660, 679),
             "other_object_type": "cabbage"},
            {"person": "웅희", "other_object_location": 1, "grape_target_location": 6, "episode_range": (680, 699),
             "other_object_type": "cabbage"},
        ],
        "14:00~16:00": [
            {"person": "민지", "other_object_location": 2, "grape_target_location": 1, "episode_range": (700, 719),
             "other_object_type": "cabbage"},
            {"person": "민지", "other_object_location": 2, "grape_target_location": 3, "episode_range": (720, 739),
             "other_object_type": "cabbage"},
            {"person": "민지", "other_object_location": 2, "grape_target_location": 4, "episode_range": (740, 759),
             "other_object_type": "cabbage"},
            {"person": "민지", "other_object_location": 2, "grape_target_location": 5, "episode_range": (760, 779),
             "other_object_type": "cabbage"},
            {"person": "민지", "other_object_location": 2, "grape_target_location": 6, "episode_range": (780, 799),
             "other_object_type": "cabbage"},
        ],
        "16:00~18:00": [
            {"person": "동훈", "other_object_location": 3, "grape_target_location": 1, "episode_range": (800, 819),
             "other_object_type": "cabbage"},
            {"person": "동훈", "other_object_location": 3, "grape_target_location": 2, "episode_range": (820, 839),
             "other_object_type": "cabbage"},
            {"person": "동훈", "other_object_location": 3, "grape_target_location": 4, "episode_range": (840, 859),
             "other_object_type": "cabbage"},
            {"person": "동훈", "other_object_location": 3, "grape_target_location": 5, "episode_range": (860, 879),
             "other_object_type": "cabbage"},
            {"person": "동훈", "other_object_location": 3, "grape_target_location": 6, "episode_range": (880, 899),
             "other_object_type": "cabbage"},
        ],
        "18:00~20:00": [
            {"person": "경훈", "other_object_location": 4, "grape_target_location": 1, "episode_range": (900, 919),
             "other_object_type": "cabbage"},
            {"person": "경훈", "other_object_location": 4, "grape_target_location": 2, "episode_range": (920, 939),
             "other_object_type": "cabbage"},
            {"person": "경훈", "other_object_location": 4, "grape_target_location": 3, "episode_range": (940, 959),
             "other_object_type": "cabbage"},
            {"person": "경훈", "other_object_location": 4, "grape_target_location": 5, "episode_range": (960, 979),
             "other_object_type": "cabbage"},
            {"person": "경훈", "other_object_location": 4, "grape_target_location": 6, "episode_range": (980, 999),
             "other_object_type": "cabbage"},
        ],
    },
    "07.08": {  # Tuesday
        "12:00~14:00": [
            {"person": "수윤", "other_object_location": 5, "grape_target_location": 1, "episode_range": (1000, 1019),
             "other_object_type": "cabbage"},
            {"person": "수윤", "other_object_location": 5, "grape_target_location": 2, "episode_range": (1020, 1039),
             "other_object_type": "cabbage"},
            {"person": "수윤", "other_object_location": 5, "grape_target_location": 3, "episode_range": (1040, 1059),
             "other_object_type": "cabbage"},
            {"person": "수윤", "other_object_location": 5, "grape_target_location": 4, "episode_range": (1060, 1079),
             "other_object_type": "cabbage"},
            {"person": "수윤", "other_object_location": 5, "grape_target_location": 6, "episode_range": (1080, 1099),
             "other_object_type": "cabbage"},
        ],
        "14:00~16:00": [
            {"person": "민지", "other_object_location": 6, "grape_target_location": 1, "episode_range": (1100, 1119),
             "other_object_type": "cabbage"},
            {"person": "민지", "other_object_location": 6, "grape_target_location": 2, "episode_range": (1120, 1139),
             "other_object_type": "cabbage"},
            {"person": "민지", "other_object_location": 6, "grape_target_location": 3, "episode_range": (1140, 1159),
             "other_object_type": "cabbage"},
            {"person": "민지", "other_object_location": 6, "grape_target_location": 4, "episode_range": (1160, 1179),
             "other_object_type": "cabbage"},
            {"person": "민지", "other_object_location": 6, "grape_target_location": 5, "episode_range": (1180, 1199),
             "other_object_type": "cabbage"},
        ],
        "16:00~18:00": [
            {"person": "경훈", "other_object_location": 1, "grape_target_location": 2, "episode_range": (1200, 1219),
             "other_object_type": "corn"},  # "1 (Corn)"
            {"person": "경훈", "other_object_location": 1, "grape_target_location": 3, "episode_range": (1220, 1239),
             "other_object_type": "corn"},
            {"person": "경훈", "other_object_location": 1, "grape_target_location": 4, "episode_range": (1240, 1259),
             "other_object_type": "corn"},
            {"person": "경훈", "other_object_location": 1, "grape_target_location": 5, "episode_range": (1260, 1279),
             "other_object_type": "corn"},
            {"person": "경훈", "other_object_location": 1, "grape_target_location": 6, "episode_range": (1280, 1299),
             "other_object_type": "corn"},
        ],
        "18:00~20:00": [
            {"person": "동훈", "other_object_location": 2, "grape_target_location": 1, "episode_range": (1300, 1319),
             "other_object_type": "cabbage"},
            {"person": "동훈", "other_object_location": 2, "grape_target_location": 3, "episode_range": (1320, 1339),
             "other_object_type": "cabbage"},
            {"person": "동훈", "other_object_location": 2, "grape_target_location": 4, "episode_range": (1340, 1359),
             "other_object_type": "cabbage"},
            {"person": "동훈", "other_object_location": 2, "grape_target_location": 5, "episode_range": (1360, 1379),
             "other_object_type": "cabbage"},
            {"person": "동훈", "other_object_location": 2, "grape_target_location": 6, "episode_range": (1380, 1399),
             "other_object_type": "cabbage"},
        ],
    },
    "07.09": {  # Wednesday
        "12:00~14:00": [
            {"person": "수윤", "other_object_location": 3, "grape_target_location": 1, "episode_range": (1400, 1419),
             "other_object_type": "corn"},
            {"person": "수윤", "other_object_location": 3, "grape_target_location": 2, "episode_range": (1420, 1439),
             "other_object_type": "corn"},
            {"person": "수윤", "other_object_location": 3, "grape_target_location": 4, "episode_range": (1440, 1459),
             "other_object_type": "corn"},
            {"person": "수윤", "other_object_location": 3, "grape_target_location": 5, "episode_range": (1460, 1479),
             "other_object_type": "corn"},
            {"person": "수윤", "other_object_location": 3, "grape_target_location": 6, "episode_range": (1480, 1499),
             "other_object_type": "corn"},
        ],
        "14:00~16:00": [
            {"person": "웅희", "other_object_location": 4, "grape_target_location": 1, "episode_range": (1500, 1519),
             "other_object_type": "corn"},
            {"person": "웅희", "other_object_location": 4, "grape_target_location": 2, "episode_range": (1520, 1539),
             "other_object_type": "corn"},
            {"person": "웅희", "other_object_location": 4, "grape_target_location": 3, "episode_range": (1540, 1559),
             "other_object_type": "corn"},
            {"person": "웅희", "other_object_location": 4, "grape_target_location": 5, "episode_range": (1560, 1579),
             "other_object_type": "corn"},
            {"person": "웅희", "other_object_location": 4, "grape_target_location": 6, "episode_range": (1580, 1599),
             "other_object_type": "corn"},
        ],
        "16:00~18:00": [
            {"person": "민지", "other_object_location": 5, "grape_target_location": 1, "episode_range": (1600, 1619),
             "other_object_type": "corn"},
            {"person": "민지", "other_object_location": 5, "grape_target_location": 2, "episode_range": (1620, 1639),
             "other_object_type": "corn"},
            {"person": "민지", "other_object_location": 5, "grape_target_location": 3, "episode_range": (1640, 1659),
             "other_object_type": "corn"},
            {"person": "민지", "other_object_location": 5, "grape_target_location": 4, "episode_range": (1660, 1679),
             "other_object_type": "corn"},
            {"person": "민지", "other_object_location": 5, "grape_target_location": 6, "episode_range": (1680, 1699),
             "other_object_type": "corn"},
        ],
        "18:00~20:00": [
            {"person": "동훈", "other_object_location": 6, "grape_target_location": 1, "episode_range": (1700, 1719),
             "other_object_type": "corn"},
            {"person": "동훈", "other_object_location": 6, "grape_target_location": 2, "episode_range": (1720, 1739),
             "other_object_type": "corn"},
            {"person": "동훈", "other_object_location": 6, "grape_target_location": 3, "episode_range": (1740, 1759),
             "other_object_type": "corn"},
            {"person": "동훈", "other_object_location": 6, "grape_target_location": 4, "episode_range": (1760, 1779),
             "other_object_type": "corn"},
            {"person": "동훈", "other_object_location": 6, "grape_target_location": 5, "episode_range": (1780, 1799),
             "other_object_type": "corn"},
        ],
    },
    "07.10": {  # Thursday - 'X' column indicates no specific object, so we'll use a generic "other_object_type"
        "12:00~14:00": [
            {"person": "수윤", "other_object_location": None, "grape_target_location": 1, "episode_range": (1800, 1819),
             "other_object_type": "X"},
            {"person": "수윤", "other_object_location": None, "grape_target_location": 2, "episode_range": (1820, 1839),
             "other_object_type": "X"},
            {"person": "수윤", "other_object_location": None, "grape_target_location": 3, "episode_range": (1840, 1859),
             "other_object_type": "X"},
            {"person": "수윤", "other_object_location": None, "grape_target_location": 4, "episode_range": (1860, 1879),
             "other_object_type": "X"},
            {"person": "수윤", "other_object_location": None, "grape_target_location": 5, "episode_range": (1880, 1899),
             "other_object_type": "X"},
            {"person": "수윤", "other_object_location": None, "grape_target_location": 6, "episode_range": (1900, 1919),
             "other_object_type": "X"},
        ],
        "14:00~16:00": [
            {"person": "경훈", "other_object_location": None, "grape_target_location": 1, "episode_range": (1920, 1939),
             "other_object_type": "X"},
            {"person": "경훈", "other_object_location": None, "grape_target_location": 2, "episode_range": (1940, 1959),
             "other_object_type": "X"},
            {"person": "경훈", "other_object_location": None, "grape_target_location": 3, "episode_range": (1960, 1979),
             "other_object_type": "X"},
            {"person": "경훈", "other_object_location": None, "grape_target_location": 4, "episode_range": (1980, 1999),
             "other_object_type": "X"},
            {"person": "경훈", "other_object_location": None, "grape_target_location": 5, "episode_range": (2000, 2019),
             "other_object_type": "X"},
            {"person": "경훈", "other_object_location": None, "grape_target_location": 6, "episode_range": (2020, 2039),
             "other_object_type": "X"},
        ],
        "16:00~18:00": [
            {"person": "웅희", "other_object_location": None, "grape_target_location": 1, "episode_range": (2040, 2059),
             "other_object_type": "X"},
            {"person": "웅희", "other_object_location": None, "grape_target_location": 2, "episode_range": (2060, 2079),
             "other_object_type": "X"},
            {"person": "웅희", "other_object_location": None, "grape_target_location": 3, "episode_range": (2080, 2099),
             "other_object_type": "X"},
            {"person": "웅희", "other_object_location": None, "grape_target_location": 4, "episode_range": (2100, 2119),
             "other_object_type": "X"},
            {"person": "웅희", "other_object_location": None, "grape_target_location": 5, "episode_range": (2120, 2139),
             "other_object_type": "X"},
            {"person": "웅희", "other_object_location": None, "grape_target_location": 6, "episode_range": (2140, 2159),
             "other_object_type": "X"},
        ],
        "18:00~20:00": [],  # This slot is empty in the image, so no data for now
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
    Draws a specific pattern of grapes (rectangle + triangle) within a given sub-area.
    sub_area_coords: (x, y, width, height) of the sub-area.
    pattern_index: 0 to 4 (representing 5 unique patterns from the provided image).
    """
    x_sub, y_sub, w_sub, h_sub = sub_area_coords

    # Calculate center of the sub-area
    center_x_sub = x_sub + w_sub / 2
    center_y_sub = y_sub + h_sub / 2

    # Relative dimensions for the rectangle and triangle within the sub-area
    rect_width = w_sub * 0.4
    rect_height = h_sub * 0.7
    tri_base = rect_width * 0.8
    tri_height = h_sub * 0.2

    # Define grape patterns as (rectangle_center_offset_x, rectangle_center_offset_y, rotation_angle_deg, triangle_offset_x, triangle_offset_y, triangle_direction)
    # The triangle direction dictates where its apex points relative to its base.
    # Pattern descriptions:
    # 0: Vertical rectangle, triangle pointing up
    # 1: 5 Circles in a cluster (as per your previous example, but now pattern 2 in the image) - will approximate with 5 circles
    # 2: Horizontal rectangle, triangle pointing right
    # 3: Diagonal rectangle, triangle pointing up-left (rotated -45 deg)
    # 4: Horizontal rectangle, triangle pointing left, with 'theta' symbol

    # Let's map these to the 0-4 index
    # Pattern 0 in image -> Pattern Index 0 (Vertical)
    # Pattern 1 in image (5 circles) -> Pattern Index 1
    # Pattern 2 in image (Horizontal right) -> Pattern Index 2
    # Pattern 3 in image (Diagonal) -> Pattern Index 3
    # Pattern 4 in image (Horizontal left with theta) -> Pattern Index 4

    # Each entry: (rect_center_dx, rect_center_dy, rect_angle, tri_center_dx, tri_center_dy, tri_angle, custom_text)
    # tri_angle is for the triangle's overall orientation, 0 for pointing up, 90 for right, 180 for down, 270 for left

    # For Pattern 1 (5 circles), we will draw 5 circles.
    # For others, draw rect + triangle.

    if pattern_index == 1:  # Pattern 1 in image (5 circles, labeled 'Y' with subscript 'i', 't', 's')
        # This one is a cluster of 5 circles, as in your `image_d1d622.jpg`
        grape_radius = min(w_sub, h_sub) * 0.1  # Smaller radius for individual grapes
        ax.add_patch(patches.Circle((center_x_sub, center_y_sub), grape_radius * 1.5, color='purple',
                                    alpha=0.9))  # Center grape slightly larger

        # Surrounding grapes
        offset_dist = grape_radius * 2
        ax.add_patch(
            patches.Circle((center_x_sub - offset_dist, center_y_sub), grape_radius, color='purple', alpha=0.9))
        ax.add_patch(
            patches.Circle((center_x_sub + offset_dist, center_y_sub), grape_radius, color='purple', alpha=0.9))
        ax.add_patch(
            patches.Circle((center_x_sub, center_y_sub - offset_dist), grape_radius, color='purple', alpha=0.9))
        ax.add_patch(
            patches.Circle((center_x_sub, center_y_sub + offset_dist), grape_radius, color='purple', alpha=0.9))

        # Add a small stem-like triangle at the top, slightly offset
        stem_points = [
            (center_x_sub, center_y_sub + offset_dist + grape_radius),
            (center_x_sub - grape_radius * 0.5, center_y_sub + offset_dist + grape_radius + tri_height),
            (center_x_sub + grape_radius * 0.5, center_y_sub + offset_dist + grape_radius + tri_height)
        ]
        ax.add_patch(patches.Polygon(stem_points, closed=True, color='green', alpha=0.9))

        # Add text 'Yits' (approximated for plot, cannot render subscripts easily)
        ax.text(center_x_sub, center_y_sub + h_sub * 0.45, "Yits", ha='center', va='bottom', fontsize=8, color='black')

    else:  # Patterns using rectangle and triangle
        if pattern_index == 0:  # Vertical rectangle, triangle up (from image)
            rect_coords = (center_x_sub - rect_width / 2, center_y_sub - rect_height / 2)
            rect_angle = 0
            # Triangle points upwards from top center of rectangle
            tri_points = [
                (center_x_sub - tri_base / 2, rect_coords[1] + rect_height),
                (center_x_sub + tri_base / 2, rect_coords[1] + rect_height),
                (center_x_sub, rect_coords[1] + rect_height + tri_height)
            ]
        elif pattern_index == 2:  # Horizontal rectangle, triangle right (from image)
            rect_width_temp = rect_height  # Swap dimensions
            rect_height_temp = rect_width
            rect_coords = (center_x_sub - rect_width_temp / 2, center_y_sub - rect_height_temp / 2)
            rect_angle = 0  # No explicit rotation needed if coords are adjusted
            # Triangle points right from right center of rectangle
            tri_points = [
                (rect_coords[0] + rect_width_temp, center_y_sub - tri_base / 2),
                (rect_coords[0] + rect_width_temp, center_y_sub + tri_base / 2),
                (rect_coords[0] + rect_width_temp + tri_height, center_y_sub)
            ]
            rect_width, rect_height = rect_width_temp, rect_height_temp  # Update for drawing
        elif pattern_index == 3:  # Diagonal rectangle, triangle up-left (from image)
            rect_coords = (center_x_sub - rect_width / 2, center_y_sub - rect_height / 2)  # Start from center
            rect_angle = -45  # Rotate by -45 degrees
            # Triangle points up-left relative to the rotated rectangle
            # This is more complex. Let's make it visually similar by rotating the standard triangle
            # around the end of the rectangle.

            # First, place rectangle. Then calculate triangle points relative to rotated rectangle end.
            # Base of triangle is at the top-left-ish corner of the rotated rectangle.
            # Rotate rect_coords around center to get the actual bottom-left

            # Simple approach: draw rectangle, then draw triangle independently based on visual.
            # This pattern is rotated, so the `Rectangle` patch needs `angle`.

            # Calculate rotated rectangle's origin (bottom-left)
            half_diag = math.sqrt((rect_width / 2) ** 2 + (rect_height / 2) ** 2)
            angle_offset = math.atan2(rect_height / 2, rect_width / 2)

            # Rotate bottom-left corner of unrotated rectangle relative to its center
            bl_x_unrotated = -rect_width / 2
            bl_y_unrotated = -rect_height / 2

            bl_x_rotated = bl_x_unrotated * math.cos(math.radians(rect_angle)) - bl_y_unrotated * math.sin(
                math.radians(rect_angle))
            bl_y_rotated = bl_x_unrotated * math.sin(math.radians(rect_angle)) + bl_y_unrotated * math.cos(
                math.radians(rect_angle))

            rect_coords = (center_x_sub + bl_x_rotated, center_y_sub + bl_y_rotated)

            # Triangle's position will be relative to the rotated top-left of the rectangle
            # Approximate the triangle's position relative to the overall pattern center
            tri_center_x = center_x_sub - rect_width * 0.3 * math.cos(
                math.radians(rect_angle)) - rect_height * 0.3 * math.sin(math.radians(rect_angle))
            tri_center_y = center_y_sub - rect_width * 0.3 * math.sin(
                math.radians(rect_angle)) + rect_height * 0.3 * math.cos(math.radians(rect_angle))

            # Triangle points: relative to its own center, then rotated
            tri_base_pts_unrotated = [
                (-tri_base / 2, 0), (tri_base / 2, 0), (0, tri_height)
            ]
            tri_points = []
            for dx_tri, dy_tri in tri_base_pts_unrotated:
                # Rotate triangle points around triangle's center by rect_angle + 90 (to point up-left)
                rot_angle_tri = rect_angle + 90
                px = dx_tri * math.cos(math.radians(rot_angle_tri)) - dy_tri * math.sin(math.radians(rot_angle_tri))
                py = dx_tri * math.sin(math.radians(rot_angle_tri)) + dy_tri * math.cos(math.radians(rot_angle_tri))
                tri_points.append((tri_center_x + px, tri_center_y + py))

            # Add 'alpha' symbol for pattern 3
            ax.text(center_x_sub, center_y_sub, r'$\alpha$', ha='center', va='center', fontsize=12, color='white',
                    rotation=rect_angle)

        elif pattern_index == 4:  # Horizontal rectangle, triangle left, with 'theta' symbol (from image)
            rect_width_temp = rect_height  # Swap dimensions
            rect_height_temp = rect_width
            rect_coords = (center_x_sub - rect_width_temp / 2, center_y_sub - rect_height_temp / 2)
            rect_angle = 0
            # Triangle points left from left center of rectangle
            tri_points = [
                (rect_coords[0], center_y_sub - tri_base / 2),
                (rect_coords[0], center_y_sub + tri_base / 2),
                (rect_coords[0] - tri_height, center_y_sub)
            ]
            rect_width, rect_height = rect_width_temp, rect_height_temp  # Update for drawing

            # Add 'theta' symbol for pattern 4
            ax.text(center_x_sub, center_y_sub, r'$\theta$', ha='center', va='center', fontsize=12, color='white')

        # Draw the rectangle
        rect_patch = patches.Rectangle(rect_coords, rect_width, rect_height,
                                       angle=rect_angle, rotation_point='center',
                                       color='purple', alpha=0.9)
        ax.add_patch(rect_patch)

        # Draw the triangle
        tri_patch = patches.Polygon(tri_points, closed=True, color='green', alpha=0.9)
        ax.add_patch(tri_patch)


def visualize_placement(episode_number):
    found_entry = None
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
# Test with episode 605, which you provided an image for (now pattern 1 in the new image mapping)
# For episode 605: relative_episode_index = 5. sub_area_index = 1 (TR), grape_orientation_index = 0.
# So, sub-area 2, Pattern 1 (vertical rectangle).
visualize_placement(605)

# Example 1: Episode 600 (first in range)
# relative_episode_index = 0. sub_area_index = 0 (TL), grape_orientation_index = 0.
# Expected: Sub-area 1 (TL), Pattern 1 (vertical)
visualize_placement(600)

# Example 2: Episode 601 (second in range)
# relative_episode_index = 1. sub_area_index = 0 (TL), grape_orientation_index = 1.
# Expected: Sub-area 1 (TL), Pattern 2 (5 circles)
visualize_placement(601)

# Example 3: Episode 602 (third in range)
# relative_episode_index = 2. sub_area_index = 0 (TL), grape_orientation_index = 2.
# Expected: Sub-area 1 (TL), Pattern 3 (horizontal, right triangle)
visualize_placement(602)

# Example 4: Episode 603 (fourth in range)
# relative_episode_index = 3. sub_area_index = 0 (TL), grape_orientation_index = 3.
# Expected: Sub-area 1 (TL), Pattern 4 (diagonal)
visualize_placement(603)

# Example 5: Episode 604 (fifth in range, "random")
# relative_episode_index = 4. sub_area_index = 0 (TL), grape_orientation_index = 4.
# Expected: Sub-area 1 (TL), Pattern 5 (horizontal, left triangle with theta)
visualize_placement(604)

# Example from Thursday (where 'X' is the other object)
# Episode 1888: 1880-1899. Other object None, Grapes in Area 5.
# 1888 - 1880 = 8.
# sub_area_index = 8 // 5 = 1 (Sub-area 2, TR)
# grape_orientation_index = 8 % 5 = 3 (Pattern 4, diagonal)
visualize_placement(605)
visualize_placement(606)

