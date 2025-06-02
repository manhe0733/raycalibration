from function import download_multiple_videos, add

if __name__ == "__main__":
    # 1 + 2 계산
    result = add(1, 2)
    print(f"1 + 2 = {result}")

    # 기존 코드
    video_urls = [
        "https://www.youtube.com/watch?v=example1",
        "https://www.youtube.com/watch?v=example2",
        "https://www.youtube.com/watch?v=example3"
    ]
    download_multiple_videos(video_urls, "downloads", delay=2)
