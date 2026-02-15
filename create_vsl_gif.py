import os
from PIL import Image, ImageDraw

def create_vsl_gif(image_folder, output_path, duration=800):
    images = []
    # Get all png files from assets
    files = sorted([f for f in os.listdir(image_folder) if f.endswith('.png')])
    
    if not files:
        print("No images found!")
        return

    # Load and process images
    processed_images = []
    target_size = (800, 450) # 16:9 Ratio

    for file in files:
        img = Image.open(os.path.join(image_folder, file))
        # Resize and crop to target size
        img = img.resize(target_size, Image.Resampling.LANCZOS)
        processed_images.append(img)

    # Add a frame with a play button overlay to each image to make it look like a video
    frames = []
    for img in processed_images:
        # Create a copy to draw on
        frame = img.copy()
        draw = ImageDraw.Draw(frame, "RGBA")
        
        # Draw a glossy play button in the center
        center_x, center_y = target_size[0] // 2, target_size[1] // 2
        radius = 50
        
        # Circle background (semi-transparent white)
        draw.ellipse([center_x - radius, center_y - radius, center_x + radius, center_y + radius], fill=(255, 255, 255, 180))
        
        # Glossy effect (inner circle)
        draw.ellipse([center_x - radius + 5, center_y - radius + 5, center_x + radius - 5, center_y + radius - 5], outline=(255, 255, 255, 255), width=2)
        
        # Triangle (Play symbol) - centered
        tri_size = 20
        points = [
            (center_x - tri_size + 5, center_y - tri_size),
            (center_x - tri_size + 5, center_y + tri_size),
            (center_x + tri_size, center_y)
        ]
        draw.polygon(points, fill=(0, 0, 0, 200))
        
        frames.append(frame)

    # Save as GIF
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0
    )
    print(f"GIF created at {output_path}")

if __name__ == "__main__":
    asset_dir = r"c:\Users\MOAZZAM\coding\ai-automation-agentic-ide\agency_websites\demgrow_vsl\assets"
    output = os.path.join(asset_dir, "preview.gif")
    create_vsl_gif(asset_dir, output)
