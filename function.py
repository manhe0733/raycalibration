from pytube import YouTube
import time

def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def download_youtube_video(url, output_path=None):
    try:
        # YouTube 객체 생성
        yt = YouTube(url)
        
        # 영상 정보 출력
        print(f"제목: {yt.title}")
        print(f"길이: {yt.length} 초")
        print(f"조회수: {yt.views}")
        
        # 최고 해상도의 mp4 스트림 선택
        video = yt.streams.get_highest_resolution()
        
        # 다운로드 실행
        if output_path:
            video.download(output_path)
        else:
            video.download()
            
        print("다운로드가 완료되었습니다!")
        return True
        
    except Exception as e:
        print(f"에러 발생: {str(e)}")
        return False

def download_multiple_videos(urls, output_path=None, delay=1):
    """
    여러 개의 유튜브 동영상을 순차적으로 다운로드합니다.
    
    Args:
        urls (list): 다운로드할 유튜브 URL 리스트
        output_path (str, optional): 저장 경로
        delay (int, optional): 다운로드 사이의 대기 시간(초)
    """
    success_count = 0
    fail_count = 0
    
    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{len(urls)}] 다운로드 시작...")
        if download_youtube_video(url, output_path):
            success_count += 1
        else:
            fail_count += 1
            
        if i < len(urls):  # 마지막 다운로드가 아니면 대기
            print(f"{delay}초 대기 중...")
            time.sleep(delay)
    
    print(f"\n다운로드 완료!")
    print(f"성공: {success_count}개")
    print(f"실패: {fail_count}개")
