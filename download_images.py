import os
import requests
import time
from urllib.parse import urljoin

def create_directory():
    if not os.path.exists('images'):
        os.makedirs('images')
        print("Created images directory")

def download_image(url, filename):
    try:
        # Add headers to mimic a browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Download the image
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Save the image
        filepath = os.path.join('images', filename)
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        print(f"Successfully downloaded {filename}")
        time.sleep(1)  # Add a small delay between downloads
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {filename}: {str(e)}")
    except Exception as e:
        print(f"Unexpected error downloading {filename}: {str(e)}")

def main():
    # Create images directory
    create_directory()
    
    # List of image URLs with working Unsplash images
    image_urls = {
        # Home section images
        'home-shoe-1.png': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff',
        'home-shoe-2.png': 'https://images.unsplash.com/photo-1605348532760-6753d2c43329',
        'home-shoe-3.png': 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa',
        'home-text-1.png': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff',
        'home-text-2.png': 'https://images.unsplash.com/photo-1605348532760-6753d2c43329',
        'home-text-3.png': 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa',
        
        # Product section images
        'product-1.png': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff',
        'product-2.png': 'https://images.unsplash.com/photo-1605348532760-6753d2c43329',
        'product-3.png': 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa',
        'product-4.png': 'https://images.unsplash.com/photo-1600185365487-76e8baf719d6',
        'product-5.png': 'https://images.unsplash.com/photo-1608231383042-177eecc1ac60',
        'product-6.png': 'https://images.unsplash.com/photo-1605348532760-6753d2c43329',
        
        # Featured section images
        'f-img-1.1.png': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff',
        'f-img-1.2.png': 'https://images.unsplash.com/photo-1605348532760-6753d2c43329',
        'f-img-1.3.png': 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa',
        'f-img-1.4.png': 'https://images.unsplash.com/photo-1600185365487-76e8baf719d6',
        'f-img-2.1.png': 'https://images.unsplash.com/photo-1608231383042-177eecc1ac60',
        'f-img-2.2.png': 'https://images.unsplash.com/photo-1605348532760-6753d2c43329',
        'f-img-2.3.png': 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa',
        'f-img-2.4.png': 'https://images.unsplash.com/photo-1600185365487-76e8baf719d6',
        'f-img-3.1.png': 'https://images.unsplash.com/photo-1608231383042-177eecc1ac60',
        'f-img-3.2.png': 'https://images.unsplash.com/photo-1605348532760-6753d2c43329',
        'f-img-3.3.png': 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa',
        'f-img-3.4.png': 'https://images.unsplash.com/photo-1600185365487-76e8baf719d6',
        
        # Review section images
        'pic1.png': 'https://images.unsplash.com/photo-1494790108377-be9c29b29330',
        'pic2.png': 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80',
        'pic3.png': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e'
    }
    
    print("Starting image downloads...")
    
    # Download all images
    for filename, url in image_urls.items():
        print(f"Downloading {filename}...")
        download_image(url, filename)
    
    print("Download process completed!")

if __name__ == "__main__":
    main() 