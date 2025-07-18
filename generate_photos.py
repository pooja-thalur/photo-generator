#!/usr/bin/env python3
import json

def generate_photos(count=5000):
    items = []
    for i in range(1, count + 1):
        album = (i - 1) // 100 + 1
        pic_id = i % 1000  # Picsum has image IDs around 0–1084
        items.append({
            "albumId": album,
            "id": i,
            "title": f"Photo {i}",
            "url": f"https://picsum.photos/id/{pic_id}/600/400",
            "thumbnailUrl": f"https://picsum.photos/id/{pic_id}/150/150"
        })
    return {"photos": items}

def main():
    data = generate_photos()
    with open("db.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("✅ db.json generated with 5000 photos.")

if __name__ == "__main__":
    main()
