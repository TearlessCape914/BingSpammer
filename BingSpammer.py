import webbrowser
import random
import time

original_url = 'https://www.bing.com/search?pc=U523&q=<search_item>&form=U523DF'
characters = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for a in range(int(150/5)):
    search = ''
    for b in range(random.randint(5,10)):
        search += characters[random.randint(0,len(characters)-1)]
    webbrowser.open_new_tab(original_url.replace('<search_item>',search))
    time.sleep((random.randint(5,8)/10))