# OFFLINE_SCP_WIKI
Just a little project to make an offline scp wiki, from the start the backend has been optimized to reduce storage usage and works on mobile too!

When you scrape it only grabs the page-content div and compresses that in a bz2 file, this is incredibly efficent and I can store the main ~6000 scps taking less than 30mb up.

By default this does download images too, which as you can imagine takes up more space (1gb for ~6000scps) but if you want you can simply comment out a certain line in my scraper program.

To make it as intuitive as possible, this runs a local webserver on your computer and when you connect to it (localhost:5000) it loads the default index.html from scpwiki.com with my custom modifications.

Also as youd expect this is very fast and is a good thing to have if you have slow internet.

# Instructions:

OK so this is just a first upload so you guys can have a taste of this. Basically git clone this repo, install flask on python3 then do python3 scp.py and load up localhost:5000 in your Web browser. Currently scp series one works but I haven't converted the links and other stuff for the other series yet. Also before you get surprised this'll be about a 1gb download when you clone this as it comes with the main ~6000 scps downloaded with images. I would let you guys scrape the data yourself but this is a lot quicker and reduces stress on the scp wiki.

Also one last thing if you notice any bugs or things that can be improved, please let me know in issues. And I'd appreciate even more if you provide code to fix said bug or implement a feature. 
