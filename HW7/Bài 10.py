list_10 = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
for item in list_10:
    for i in range(-1, -len(item)-1, -1):
        if item[i] == '.':
            print(item[i+1:])
            break
