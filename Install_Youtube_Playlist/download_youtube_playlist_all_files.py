from pytube import Playlist

playlist = Playlist('https://www.youtube.com/playlist?list=PL-k_liNMvNQCQSCCZPs6TA2QCVlMw51Ky')
print('Number of videos in playlist: %s' % len(playlist.video_urls))
playlist.download_all()