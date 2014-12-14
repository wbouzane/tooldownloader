set log="tooldownloader.log"
python tooldownloader.py > %log%
robocopy  C:\Downloads i:\Downloads /r:0 /e /np /xo /xd .cache >> %log%
bmail -s zm.boomit.ca -p 25 -t william@boomit.ca -f tooldownloader@boomit.ca -h -a "Tooldownloaderlog" -m %log%