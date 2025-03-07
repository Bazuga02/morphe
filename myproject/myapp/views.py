from django.http import HttpResponse
import os
import datetime
import pytz
import subprocess

def htop_view(request):
    name = "Abhishek Rai"  
    username = os.getenv("USER", "codespace")  
    ist_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S.%f')
    top_output = subprocess.getoutput('top -b -n 1 | head -20')  

    response = f"""
    <h1>Name: {name}</h1>
    <h2>User: {username}</h2>
    <h2>Server Time (IST): {ist_time}</h2>
    <pre>{top_output}</pre>
    """
    return HttpResponse(response)
