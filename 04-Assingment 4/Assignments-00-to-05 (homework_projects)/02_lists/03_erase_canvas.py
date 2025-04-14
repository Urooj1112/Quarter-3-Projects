from graphics import GraphWin, Rectangle, Point
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def rectangles_overlap(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    """Return True if rectangle A (ax1, ay1, ax2, ay2) overlaps rectangle B (bx1, by1, bx2, by2)."""
    return not (ax2 < bx1 or ax1 > bx2 or ay2 < by1 or ay1 > by2)

def erase_objects(eraser_coords, cells):
    """
    For each cell, if its rectangle overlaps with the eraser,
    change its fill color to white.
    
    eraser_coords: (left, top, right, bottom)
    cells: list of tuples (cell_rectangle, (left, top, right, bottom))
    """
    for cell, (cx1, cy1, cx2, cy2) in cells:
        if rectangles_overlap(eraser_coords[0], eraser_coords[1], eraser_coords[2], eraser_coords[3],
                              cx1, cy1, cx2, cy2):
            cell.setFill("white")

def main():
    # Create the window.
    win = GraphWin("Eraser Canvas", CANVAS_WIDTH, CANVAS_HEIGHT)
    win.setBackground("white")
    
    # Create grid of blue cells and store each cell with its coordinates.
    cells = []
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            p1 = Point(col, row)
            p2 = Point(col + CELL_SIZE, row + CELL_SIZE)
            cell = Rectangle(p1, p2)
            cell.setFill("blue")
            cell.draw(win)
            cells.append((cell, (col, row, col + CELL_SIZE, row + CELL_SIZE)))
    
    # Wait for an initial click to create the eraser.
    initial_click = win.getMouse()
    eraser = Rectangle(Point(initial_click.getX(), initial_click.getY()),
                       Point(initial_click.getX() + ERASER_SIZE, initial_click.getY() + ERASER_SIZE))
    eraser.setFill("pink")
    eraser.draw(win)
    
    # Main loop to simulate click-and-drag.
    # Use win.checkMouse() to get new mouse events without blocking.
    # (True dragging isn’t supported in Zelle’s graphics, but rapid clicks while moving
    #  the mouse can simulate dragging.)
    while True:
        # Allow user to press "q" to quit.
        key = win.checkKey()
        if key.lower() == "q":
            break
        
        # Check for a new mouse event.
        new_point = win.checkMouse()
        if new_point is not None:
            # Calculate the difference between the new click and the eraser's current top-left.
            current_top_left = eraser.getP1()
            dx = new_point.getX() - current_top_left.getX()
            dy = new_point.getY() - current_top_left.getY()
            eraser.move(dx, dy)
        
        # Get current coordinates of the eraser.
        p1 = eraser.getP1()
        p2 = eraser.getP2()
        eraser_coords = (p1.getX(), p1.getY(), p2.getX(), p2.getY())
        
        # Erase any cell overlapping with the eraser.
        erase_objects(eraser_coords, cells)
        
        time.sleep(0.01)  # A short pause for smoother updating.
    
    win.close()

if __name__ == '__main__':
    main()