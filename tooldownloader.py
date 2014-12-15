from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import  URLError
from zipfile import ZipFile
from zipfile import BadZipFile
import pickle
import errno
import glob
import os
import re
import sys

# Create directory
def createDir(path):
  try:
    os.makedirs(path)
  except OSError as e:
    if e.errno != errno.EEXIST:
      print(e)

# Extract zip files
def extract(filename, directory):
  if directory != '.':
    createDir(directory)
  sys.stdout.write('Extracting... ')
  try:
    z = ZipFile(filename)
    z.extractall(directory)
    z.close()
  except BadZipFile as e:
    print('Error: Zip file is corrupt')
    return
  os.remove(filename)
  sys.stdout.write('Done\n')

# Download file from url
def getFile(url, filename):
  req = Request(url)

  try:
    response = urlopen(req)
    try:
      filelastmodified = lastmod[filename]
    except:
      lastmod[filename] = ''
    if lastmod[filename] == response.info().get('last-modified') and os.path.isfile(filename):
      sys.stdout.write(filename + ' already exists and file on server is not newer.\n')
      return
    sys.stdout.write('Downloading ' + filename)
    filesize = int(response.info().get('content-length'))
    lefttodownload = filesize
    subamount = int(filesize / 10)
    downloadedfile = response.read(0)
    while lefttodownload != 0:
      if lefttodownload < subamount:
        downloadedfile += response.read(lefttodownload)
        lefttodownload = 0
      else:
        downloadedfile += response.read(subamount)
        lefttodownload -= subamount
        sys.stdout.write('.')
        sys.stdout.flush()
    try:
      with open(filename, 'wb') as f:
        f.write(downloadedfile)
        sys.stdout.write('Done!\n')
        lastmod[filename] = response.info().get('last-modified')
        writeCache()
    except OSError as e:
      sys.stdout.write('Failed to write file to disk:\n')
      print(e)
  except URLError as e:
    if hasattr(e, 'reason'):
      print('We failed to reach a server.')
      print('Reason:', e.reason)
    elif hasattr(e, 'code'):
      print('The server couldn\'t fulfill the request.')
      print('Error code: ', e.code)
    else:
      print('unexpected error')

def getPage(url):
  req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

  try:
    return urlopen(req).read()
  except URLError as e:
    if hasattr(e, 'reason'):
      print('We failed to reach a server.')
      print('Reason:', e.reason)
    elif hasattr(e, 'code'):
      print('The server could not fulfill the request.')
      print('Error code: ', e.code)
    else:
      print('unexpected error')

def writeCache():
  with open('.cache', 'wb') as f:
    pickle.dump(lastmod, f)

# Download ADWCleaner
def getADWCleaner():
  getFile('http://www.infospyware.com/Software/AdwCleaner.exe', 'AdwCleaner.exe')

# Download Auslogics Disk Defragmenter portable
def getAusDefrag():
  getFile('http://www.auslogics.com/en/downloads/disk-defrag/ausdiskdefragportable.exe', 'ausdiskdefragportable.exe')

# Download Avast
def getAvast():
  getFile('http://files.avast.com/iavs5x/avast_free_antivirus_setup.exe', 'avast_free_antivirus_setup.exe')

# Download AVG
def getAVG():
  page = getPage('http://free.avg.com/download-free-all-product/')
  
  if not page:
    print('No data returned')
    return

  soup = BeautifulSoup(page)

  for link in soup.findAll('a', href=re.compile(".exe")):
    avg = link.get('href')
    getFile(avg, avg.split('/')[-1])

# Download AVG Remover
def getAVGRemover():
  page = getPage("http://www.avg.com/ca-en/utilities/index.html")

  if not page:
    print('No data returned')
    return
  
  soup = BeautifulSoup(page)

  for link in soup.findAll('a', href=re.compile("remover")):
    avgr = link.get('href')
    getFile(avgr, avgr.split('/')[-1])

# Download CCleaner portable
def getCCleaner():
  getFile('http://www.piriform.com/ccleaner/download/portable/downloadfile', 'CCleaner.zip')
  extract("CCleaner.zip", "CCleaner")

# Download ComboFix
def getComboFix():
  getFile('http://www.infospyware.net/sUBs/ComboFix.exe', 'ComboFix.exe')

# Download HijackThis
def getHiJackThis():
  getFile('http://downloads.sourceforge.net/project/hjt/2.0.4/HijackThis.exe', 'HijackThis.exe')

# Download JRT
def getJRT():
  getFile('http://thisisudax.org/downloads/JRT.exe', 'JRT.exe')

# Download Kaspersky AVPTool
def getKaspersky():
  page = getPage('http://devbuilds.kaspersky-labs.com/devbuilds/AVPTool/avptool11/')
  
  if not page:
    print('No data returned')
    return

  soup = BeautifulSoup(page)
  for link in soup.findAll('a'):
    avp = link.get('href')

  getFile('http://devbuilds.kaspersky-labs.com/devbuilds/AVPTool/avptool11/' + avp, avp)

  for name in glob.glob('setup_11*')[:-1]:
    os.remove(name)

# Download Malwarebytes
def getMalwarebytes():
  getFile('http://downloads.malwarebytes.org/file/mbam/mbam-setup-2.0.4.1028.exe', 'mbam-setup.exe')

# Download McAfee Removal Tool MCPR
def getMcAfeeRemovalTool():
  getFile('http://download.mcafee.com/products/licensed/cust_support_patches/MCPR.exe', 'MCPR.exe')

# Download and extract Revo Portable
def getRevoUninstaller():
  getFile('http://www.revouninstaller.com/download/revouninstaller.zip', 'revouninstaller.zip')
  extract("revouninstaller.zip", ".")

# Download SpyBot
def getSpyBot():
  getFile('http://www.spybotupdates.biz/files/spybotsd162.exe', 'spybotsd162.exe')

# Download SpyBot 2
def getSpyBot2():
  getFile('http://files.spybot.info/SpybotSD2.exe', 'SpybotSD2.exe')

# Download TDSSKiller
def getTDSSKiller():
  getFile('http://media.kaspersky.com/utilities/VirusUtilities/EN/tdsskiller.exe', 'tdsskiller.exe')

# Create Download directory and make it the working directory

createDir("Downloads")
os.chdir("Downloads")

# Load cache file

if os.path.isfile('.cache'):
  with open('.cache', 'rb') as f:
    lastmod = pickle.load(f)
else:
  lastmod = {}

# Call download functions

getADWCleaner()
getAusDefrag()
getAvast()
getAVG()
getAVGRemover()
getCCleaner()
getComboFix()
getHiJackThis()
getJRT()
getKaspersky()
getMalwarebytes()
getMcAfeeRemovalTool()
getRevoUninstaller()
getSpyBot()
getSpyBot2()
getTDSSKiller()