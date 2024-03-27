import os

def find_images(directory):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in image_extensions):
                return True
    return False

def update_readme_with_images():
    directories_with_images = [d for d in os.listdir('.') if os.path.isdir(d) and find_images(d)]
    print(f'Found {len(directories_with_images)} directories with images')

    with open('README.md', 'w') as readme:
        readme.write('# Wallpapers\n')
        readme.write('A personal wallpaper dump\n\n')
        readme.write('---\n\n')
        readme.write('<h1 align="center">\n')
        readme.write('  These wallpapers are NOT MINE<br>\n')
        readme.write('  Credits go to their respective owners!\n')
        readme.write('</h1>\n\n')
        
        for directory in directories_with_images:
            readme.write(f'<a href={directory}>{directory}</a>')
            readme.write(f'<details><summary></summary>')
            image_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
            for image_file in image_files:
                if any(image_file.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif']):
                    readme.write(f'<img src={directory}/{image_file}><br>')
            readme.write('</details>')

        readme.write('<br>')
        readme.write('Inspired by [zDyanTB/aesthic-wallpapers](https://github.com/zDyanTB/aesthic-wallpapers) and [flick0/kabegami](https://github.com/flick0/kabegami)')

if __name__ == "__main__":
    if os.path.exists('README.md'):
        os.remove('README.md')
        print('Removed existing README.md')
    
    update_readme_with_images()
