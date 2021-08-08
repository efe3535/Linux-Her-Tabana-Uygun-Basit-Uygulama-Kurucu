import os

print('Uygulama Kurucuya Hoş Geldiniz.')
soru = input('Hangi Uygulama Kurulsun (Desteklenenler:neofetch,google,opera,discord,7zip) ')
neofetch = ('sudo apt install neofetch')
opera1 = ('wget -qO- https://deb.opera.com/archive.key | sudo apt-key add -')
opera2 = ('wget https://download3.operacdn.com/pub/opera/desktop/69.0.3686.77/linux/opera-stable_69.0.3686.77_amd64.deb')
opera3 = ('sudo dpkg -i opera-stable_69.0.3686.77_amd64.deb')
opera4 = ('sudo apt install -f')
yedizip = ('sudo apt-get install p7zip-full')
discord1 = ('sudo snap install discord')
google = ('sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
google2 = ('sudo dpkg -i google-chrome-stable_current_amd64.deb')
snap = ('sudo install snapd')

if soru == 'discord':
    print('Discord Kuruluyor !')
    os.system(snap)
    os.system(discord1)
if soru == 'neofetch':
    print('Neofecth Kuruluyor !')
    os.system(neofetch)

if soru == 'opera':
    print('Opera Kuruluyor !')
    os.system(opera1)
    os.system(opera2)
    os.system(opera3)
    os.system(opera4)

if soru == 'google':
    print('Google Kuruluyor !')
    os.system(google)
    os.system(google2)

if soru == '7zip':
    print('7zip Kuruluyor !')
    os.system(yedizip)