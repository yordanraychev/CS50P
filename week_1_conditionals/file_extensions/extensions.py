user_prompt = input("File name: ")
prompt = user_prompt.lower()

if ".jpg" in prompt:
    print("image/jpeg")
elif ".gif" in prompt:
    print("image/gif")
elif ".jpeg" in prompt:
    print("image/jpeg")
elif ".png" in prompt:
    print("image/png")
elif ".pdf" in prompt:
    print("application/pdf")
elif ".txt" in prompt:
    print("text/plain")
elif ".zip" in prompt:
    print("application/zip")
else:
    print("application/octet-stream")
    