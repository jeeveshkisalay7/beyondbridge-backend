from PIL import Image, ImageDraw

def remove_bg(img_path):
    print(f"Processing {img_path}")
    img = Image.open(img_path).convert("RGBA")
    
    # Create a mask by floodfilling from the top-left corner
    # (assuming the background is solid and touches the corners)
    # We will floodfill with a unique color that is not present in the image
    
    # We can use ImageDraw.floodfill on a copy
    # But wait, PIL's floodfill doesn't return a mask easily.
    # Let's do a simple BFS from corners for pixels close to the corner pixel color.
    
    width, height = img.size
    pixels = img.load()
    
    # Let's assume top-left pixel is the background color
    bg_color = pixels[0, 0]
    
    # If the background is already transparent, skip
    if bg_color[3] == 0:
        print("Already transparent")
        return
    
    # We want to remove pixels close to bg_color
    def color_dist(c1, c2):
        return sum(abs(a - b) for a, b in zip(c1[:3], c2[:3]))
        
    visited = set()
    queue = [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1)]
    
    for start in queue:
        if start not in visited and color_dist(pixels[start], bg_color) < 30:
            visited.add(start)
    
    q = list(visited)
    idx = 0
    while idx < len(q):
        x, y = q[idx]
        idx += 1
        
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if (nx, ny) not in visited:
                    if color_dist(pixels[nx, ny], bg_color) < 40: # tolerance
                        visited.add((nx, ny))
                        q.append((nx, ny))
                        
    # Now set all visited pixels to transparent
    for x, y in visited:
        # keep the original color but set alpha to 0
        r, g, b, a = pixels[x, y]
        pixels[x, y] = (r, g, b, 0)
        
    img.save(img_path, "PNG")
    print(f"Saved {img_path}")

import glob
for path in glob.glob("assets/*.png"):
    remove_bg(path)
