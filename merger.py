from PIL import Image
import time

# Creating layout of image
layout = [
    ['#', 'Top', '#', '#'],
    ['East', 'North', 'South', 'West'],
    ['#', 'Bottom', '#', '#']
]

# Creating new image (64x48)
result = Image.new('RGBA', (64, 48), (0, 0, 0, 0))

# Size of each texture (16x16)
tile_size = 16

print(f"Result should appear in current directory as combined.png\n")

# Go through each element in layout
for y, row in enumerate(layout):
    for x, cell in enumerate(row):
        if cell != '#':
            try:
                # Opening image and converting it to RGBA
                with Image.open(f'{cell}.png').convert('RGBA') as img:

                    # Checking image size
                    if img.size != (tile_size, tile_size):
                        print(f'Warning: image size is not 16x16')
                    
                    # Calculating position for pasting
                    position = (x * tile_size, y * tile_size)
                    
                    # Pasting image into result
                    result.paste(img, position, img)
                    print(f"{cell} texture succesfuly added")

            except FileNotFoundError:
                print(f"ERROR: {cell}.png not found")
print(f'\n')
# Saving result
result.save('combined.png')
input('Press any button to close...')
