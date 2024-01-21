from django.http import FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from socialDownloaderApp.mediaDownloaders.util.mediaHandler import formatVideoName
from socialDownloaderApp.mediaDownloaders.util.platformDetector import detectPlatform, PLATFORM_INFO
from django.http import JsonResponse
import os


class CleanUpFileResponse(FileResponse):
    def __init__(self, *args, file_path, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_path = file_path

    def close(self):
        super().close()
        if self.file_path and os.path.exists(self.file_path):
            os.remove(self.file_path)


def downloadMediaView(request):
    try:
        mediaUrl = request.POST.get('mediaUrl', '')
        downloader = detectPlatform(mediaUrl)
        filePath = downloader(mediaUrl)
        if not filePath.lower().endswith('.mp4'):
            return JsonResponse({'error': 'File is not valid'}, status=400)

        return CleanUpFileResponse(open(filePath, 'rb'), as_attachment=True,
                                   filename=os.path.basename(filePath), file_path=filePath)
    except Exception as e:
        print(f"Error downloadMediaView: {e}")
        return redirect('home')


def home(request):
    return render(request, 'index.html', {'PLATFORM_INFO': PLATFORM_INFO})
