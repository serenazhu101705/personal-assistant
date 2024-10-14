if ask == "google something" or ask == "google an image":
    look = input("What would you like to look up?\n")
    look = look.replace(" ","+")
    if ask == "google something":
        url = 'https://www.google.com/search?q=' + look + '&oq=' + look + '&aqs=chrome.0.0l3.2802j0j4&sourceid=chrome&ie=UTF-8'
    else:
        url = 'https://www.google.com/search?q=' + look +  '&safe=strict&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj-8K2VjpvqAhWVcc0KHQn1CsUQ_AUoAXoECB4QAw&biw=1038&bih=576'
    webbrowser.open(url)
elif ask == "check mycircle":
	webbrowser.open("mycircle.meetcircle.com")
elif ask == "open a website":
	url = input("What website would you like to visit?\n")
	webbrowser.open(url)
