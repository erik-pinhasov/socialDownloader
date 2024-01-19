from django.contrib import messages
from django.http import FileResponse
from django.shortcuts import render, redirect
from socialDownloaderApp.mediaDownloaders.util.platformDetector import detectPlatform, PLATFORM_INFO
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
        response = CleanUpFileResponse(open(filePath, 'rb'), as_attachment=True,
                                       filename=os.path.basename(filePath), file_path=filePath)
        messages.success(request, "ההורדה בוצעה.")
        return response
    except Exception as e:
        print(f"Error : {e}")
        messages.error(request, "שגיאה, ההורדה נכשלה.")
        return redirect('home')


def home(request):
    return render(request, 'index.html', {'PLATFORM_INFO': PLATFORM_INFO})
