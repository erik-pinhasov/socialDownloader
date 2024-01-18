from django.contrib import messages
from django.http import FileResponse
from django.shortcuts import render, redirect
from socialDownloaderApp.mediaDownloaders.util.platformDetector import detectPlatform
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
    media_url = request.POST.get('mediaUrl', '')
    downloader = detectPlatform(media_url)
    file_path = downloader(media_url)

    if file_path and os.path.exists(file_path):
        response = CleanUpFileResponse(open(file_path, 'rb'), as_attachment=True,
                                       filename=os.path.basename(file_path), file_path=file_path)
        return response
    else:
        messages.error(request, "Error, download failed.")
        return redirect('home')


def home(request):
    return render(request, 'index.html')
