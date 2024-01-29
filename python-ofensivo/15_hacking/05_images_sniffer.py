#/usr/bin/env python3
"""
Images sniffer
"""

from mitmproxy import http
from mitmproxy import ctx

def response(flow):
    """
    Sniff images
    """

    content_type = flow.response.headers.get("Content-Type", "No Content-Type")

    try:

        if "image" in content_type:

            url = flow.request.url

            ext = content_type.split("/")[-1]

            if ext == "jpeg":
                ext = "jpg"

            file_name = f"img/{url.replace('/', '_')}.{ext}"

            image_data = flow.response.content

            with open(file_name, "wb") as f:

                f.write(image_data)

                print(f"\n[+]Imagen guardada: {file_name}\n")

    except:
        pass