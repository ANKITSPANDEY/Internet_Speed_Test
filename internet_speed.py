import speedtest   #pip install speedtest-cli

test=speedtest.Speedtest()

def bytes_to_mb(bytes):
    KB = 1024 # One Kilobyte is 1024 bytes
    MB = KB * 1024 # One MB is 1024 KB
    return int(bytes/MB)

down =bytes_to_mb(test.download())
upload=bytes_to_mb(test.upload())
print(f"Internet Download speed is :- {down} MB")
print(f"Internet Upload speed is :- {upload} MB")


