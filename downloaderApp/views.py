from django.contrib import messages
from django.http import FileResponse
from django.shortcuts import render, redirect
from mediaDownloaders.platformDetector import detectPlatform
import os


def downloadMediaView(request):
    mediaUrl = request.POST.get('mediaUrl', '')
    downloader = detectPlatform(mediaUrl)
    file_path = downloader(mediaUrl)
    if file_path and os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
    else:
        messages.error(request, "Error, download failed.")
        return redirect('home')


def home(request):
    return render(request, 'index.html')
