import requests
import os
from datetime import datetime


def generate_image(prompt):
    try:
        print("🖼️ Generating image...")

        # Clean prompt for URL
        clean_prompt = prompt.replace(" ", "%20")

        url = f"https://image.pollinations.ai/prompt/{clean_prompt}"

        response = requests.get(url)

        if response.status_code != 200:
            print("❌ Failed to generate image")
            return None

        # Create folder if not exists
        if not os.path.exists("images"):
            os.makedirs("images")

        # Unique filename
        filename = f"images/image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"

        with open(filename, "wb") as f:
            f.write(response.content)

        print(f"✅ Image saved: {filename}")
        return filename

    except Exception as e:
        print(f"❌ Image error: {e}")
        return None