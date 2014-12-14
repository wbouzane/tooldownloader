from bs4 import BeautifulSoup
import httplib2
import zipfile
from zipfile import ZipFile
import errno
import os
import re
import glob

# Make sure directory exists
def createDir(path):
  try:
    os.makedirs(path)
  except OSError as exception:
    if exception.errno != errno.EEXIST:
      raise

# Extract zip files
def extract(zipFilename, dm_extraction_dir) :
  zipTest = ZipFile(zipFilename)
  zipTest.extractall(dm_extraction_dir)

# Download Auslogics Disk Defragmenter portable
def getAusDefrag():
  print("Downloading Auslogics Defrag Portable...")

  response, content = h.request('http://www.auslogics.com/en/downloads/disk-defrag/ausdiskdefragportable.exe')

  print(response.reason)

  with open('ausdiskdefragportable.exe', 'wb') as f:
    f.write(content)

# Download Avast
def getAvast():
  print("Downloading Avast...")

  response, content = h.request('http://files.avast.com/iavs5x/avast_free_antivirus_setup.exe')

  print(response.reason)

  with open('avast_free_antivirus_setup.exe', 'wb') as f:
    f.write(content)

# Download AVG
def getAVG():
  print("Downloading AVG (Offline installer x86, x64, online installer)...")

  response, content = h.request("http://free.avg.com/us-en/download.prd-afh")
  soup = BeautifulSoup(content)

  for link in soup.findAll('a', href=re.compile(".exe")):
    avg = link.get('href')
    response, content = h.request(avg)
    print(response.reason)
    with open(avg.split('/')[-1], 'wb') as f:
      f.write(content)

# Download AVG Remover
def getAVGRemover():
  print("Downloading AVG Remover (2012 x86, 2012 x64, 2013 x86, 2013 x64)...")

  response, content = h.request("http://www.avg.com/ca-en/utilities")
  soup = BeautifulSoup(content)

  for link in soup.findAll('a', href=re.compile("remover")):
    avgr = link.get('href')
    response, content = h.request(avgr)
    print(response.reason)
    with open(avgr.split('/')[-1], 'wb') as f:
      f.write(content)

# Download CCleaner portable
def getCCleaner():
  print("Downloading CCleaner...")

  response, content = h.request('http://www.piriform.com/ccleaner/download/portable/downloadfile')

  print(response.reason)

  with open('CCleaner.zip', 'wb') as f:
    f.write(content)
      
  createDir("CCleaner")
  extract("CCleaner.zip", "CCleaner")
  os.remove('CCleaner.zip')

# Download ComboFix
def getComboFix():
  print("Downloading ComboFix...")

  response, content = h.request('http://www.infospyware.net/sUBs/ComboFix.exe')

  print(response.reason)

  with open('ComboFix.exe', 'wb') as f:
    f.write(content)

# Download Flashplayer
def getFlashPlayer():
  print("Downloading Flashplayer for IE...")

  response, content = h.request('http://download.macromedia.com/pub/flashplayer/current/support/install_flash_player_ax.exe')

  print(response.reason)

  with open('install_flash_player_ax.exe', 'wb') as f:
    f.write(content)
  
  print("Downloading Flashplayer...")

  response, content = h.request('http://download.macromedia.com/pub/flashplayer/current/support/install_flash_player.exe')

  print(response.reason)

  with open('install_flash_player.exe', 'wb') as f:
    f.write(content)

# Download HijackThis
def getHiJackThis():
  print("Downloading HiJackThis...")

  response, content = h.request('http://downloads.sourceforge.net/project/hjt/2.0.4/HijackThis.exe')

  print(response.reason)

  with open('HijackThis.exe', 'wb') as f:
    f.write(content)

# Download Kaspersky AVPTool
def getKaspersky():
  print("Downloading Kaspersky...")

  response, content = h.request("http://devbuilds.kaspersky-labs.com/devbuilds/AVPTool/avptool11/")
  soup = BeautifulSoup(content)
  for link in soup.findAll('a'):
    avp = link.get('href')

  response, content = h.request("http://devbuilds.kaspersky-labs.com/devbuilds/AVPTool/avptool11/" + avp)

  print(response.reason)

  if response.status == 200:
    for name in glob.glob('setup_11*'):
      os.remove(name)

  with open(avp, 'wb') as f:
    f.write(content)

# Download Malwarebytes
def getMalwarebytes():
  print("Downloading Malwarebytes...")

  response, content = h.request('http://www.malwarebytes.org/mbam/program/mbam-setup.exe')

  print(response.reason)

  with open('mbam-setup.exe', 'wb') as f:
    f.write(content)

# Download McAfee Removal Tool MCPR
def getMcAfeeRemovalTool():
  print("Downloading McAfee Removal Tool...")

  response, content = h.request('http://download.mcafee.com/products/licensed/cust_support_patches/MCPR.exe')

  print(response.reason)

  with open('MCPR.exe', 'wb') as f:
    f.write(content)

# Download and extract Revo Portable
def getRevoUninstaller():
  print("Downloading Revo Uninistaller...")

  response, content = h.request('http://www.revouninstaller.com/download/revouninstaller.zip')

  print(response.reason)

  with open('revouninstaller.zip', 'wb') as f:
    f.write(content)
      
  extract("revouninstaller.zip", ".")
  os.remove('revouninstaller.zip')

# Download SpyBot
def getSpyBot():
  print("Downloading SpyBot...")

  response, content = h.request('http://www.spybotupdates.biz/files/spybotsd162.exe')

  print(response.reason)

  with open('spybotsd162.exe', 'wb') as f:
    f.write(content)

# Download SpyBot 2
def getSpyBot2():
  print("Downloading SpyBot 2...")

  response, content = h.request('http://files.spybot.info/SpybotSD2.exe')

  print(response.reason)

  with open('SpybotSD2.exe', 'wb') as f:
    f.write(content)

# Download TDSSKiller
def getTDSSKiller():
  print("Downloading TDSSKiller...")

  response, content = h.request('http://support.kaspersky.com/downloads/utils/tdsskiller.zip')

  print(response.reason)

  with open('tdsskiller.zip', 'wb') as f:
    f.write(content)
      
  createDir("TDSSKiller")
  extract("tdsskiller.zip", "TDSSKiller")
  os.remove('tdsskiller.zip')

createDir("Downloads")
os.chdir("Downloads")
h = httplib2.Http('.cache')

getAusDefrag()
getAvast()
getAVG()
getAVGRemover()
getCCleaner()
getComboFix()
getFlashPlayer()
getHiJackThis()
getKaspersky()
getMalwarebytes()
getMcAfeeRemovalTool()
getRevoUninstaller()
getSpyBot()
getSpyBot2()
getTDSSKiller()