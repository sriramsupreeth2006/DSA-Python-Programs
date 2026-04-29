import sys

def get_orientation(p, q, r):
    # Returns 0 for collinear, 1 for clockwise, 2 for counter-clockwise
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0: return 0
    return 1 if val > 0 else 2

def merge(points):
    # Uses Monotone Chain logic to merge sub-hulls into one
    points.sort()
    
    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and get_orientation(lower[-2], lower[-1], p) != 2:
            lower.pop()
        lower.append(p)
    
    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and get_orientation(upper[-2], upper[-1], p) != 2:
            upper.pop()
        upper.append(p)
        
    return lower[:-1] + upper[:-1]

def convex_hull(points):
    n = len(points)
    if n <= 3:
        return sorted(points)

    # Divide: Sort by X and split
    points.sort()
    mid = n // 2
    left_hull = convex_hull(points[:mid])
    right_hull = convex_hull(points[mid:])

    # Conquer: Merge the two hulls
    return merge(left_hull + right_hull)

def get_min_square_area(points):
    """Greedy method to find minimal square area enclosing all points"""
    if not points: return 0
    
    # Find the range of X and Y coordinates
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    
    # The span in both directions
    width = max_x - min_x
    height = max_y - min_y
    
    # To enclose all points in a SQUARE, the side must be the larger of the two spans
    side = max(width, height)
    return side * side

# --- Execution Logic based on the Image Task ---
def main():
    # Example handling for T test cases as per the image
    # For a real lab submission, you might use input() or sys.stdin.read()
    
    # Sample Input based on image:
    # 2 (Test Cases)
    # 4 (Points) -> (-1,-1), (1,1), (1,-1), (-1,1)
    # 3 (Points) -> (0,0), (1,1), (2,2)
    
    test_cases = [
        [(-1, -1), (1, 1), (1, -1), (-1, 1)],
        [(0, 0), (1, 1), (2, 2)]
    ]
    
    for pts in test_cases:
        # Step 1: Find Convex Hull (Divide and Conquer)
        hull = convex_hull(pts)
        
        # Step 2: Calculate Square Area (Greedy)
        # Note: You can calculate area from the original points OR the hull points.
        # The result will be the same since the hull contains the extreme points.
        area = get_min_square_area(hull)
        
        print(area)

if __name__ == "__main__":
    main()