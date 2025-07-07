import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from datetime import \
    datetime  # Though not directly used for date/time calculations for plot, it's good practice for date handling.

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
    Draws a specific pattern of 5 grapes within a given sub-area.
    sub_area_coords: (x, y, width, height) of the sub-area.
    pattern_index: 0 to 4 (representing 5 unique patterns of 5 grapes).
    """
    x, y, w, h = sub_area_coords
    grape_radius = min(w, h) * 0.15  # Size of individual grape dots

    # Define grape positions for each pattern relative to the sub-area's bottom-left corner (x, y)
    # Each list contains (dx, dy) offsets for 5 grapes
    grape_patterns = [
        # Pattern 0: Central cluster (like the image provided for episode 605)
        [(0.5, 0.5), (0.5 - 0.2, 0.5), (0.5 + 0.2, 0.5), (0.5, 0.5 - 0.2), (0.5, 0.5 + 0.2)],
        # Pattern 1: Diagonal line
        [(0.2, 0.2), (0.35, 0.35), (0.5, 0.5), (0.65, 0.65), (0.8, 0.8)],
        # Pattern 2: Vertical line
        [(0.5, 0.2), (0.5, 0.35), (0.5, 0.5), (0.5, 0.65), (0.5, 0.8)],
        # Pattern 3: Horizontal line
        [(0.2, 0.5), (0.35, 0.5), (0.5, 0.5), (0.65, 0.5), (0.8, 0.5)],
        # Pattern 4: Random scatter
        [(np.random.rand(), np.random.rand()) for _ in range(5)]  # Generate random for this pattern
    ]

    # Ensure "random" pattern is consistent for the same input
    if pattern_index == 4:
        np.random.seed(int(x * 1000 + y * 1000 + w * 1000 + h * 1000))  # Seed based on sub-area coords
        grape_positions = [(x + dx * w, y + dy * h) for dx, dy in grape_patterns[pattern_index]]
    else:
        grape_positions = [(x + dx * w, y + dy * h) for dx, dy in grape_patterns[pattern_index]]

    for gx, gy in grape_positions:
        ax.add_patch(patches.Circle((gx, gy), grape_radius, color='purple', alpha=0.9))

    # Add a stem for the grape cluster for better visual resemblance to grapes
    if pattern_index == 0:  # Only for the central cluster pattern
        ax.plot([x + w * 0.5, x + w * 0.5 + 0.1], [y + h * 0.5 + 0.2, y + h * 0.5 + 0.3], color='green', linewidth=2)


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

    # Add labels for sub-areas (optional, for debugging/clarity)
    for i, (sx, sy, sw, sh) in enumerate(sub_area_coords_list):
        ax.text(sx + sw / 2, sy + sh / 2, f'', ha='center', va='center', fontsize=8, color='blue',
                alpha=0.0)  # Hide by default

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
# Test with episode 605, which you provided an image for.
# Expected: Other Object in Area 1 (Cabbage), Grapes in Area 2 (Sub-area 2, Pattern 1)
visualize_placement(605)

