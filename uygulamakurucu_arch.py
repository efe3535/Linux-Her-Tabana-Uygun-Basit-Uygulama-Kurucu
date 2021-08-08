import os

print('Uygulama Kurucuya Hoş Geldiniz !')
bileşen = input('Programın Çalışması İçin Gerekli Bileşenler Kurulsun mu ? Örn:snap ')
soru = ('Hangi Uygulama Kurulsun ? (Desteklenenler:discord,google chrome,opera,neofetch,woeusb) ')
git = ('sudo pacman -S git')
snap1 = ('git clone https://aur.archlinux.org/snapd.git')
snap2 = ('cd snapd')
snap3 = ('makepkg -si')
snap4 = ('sudo systemctl enable --now snapd.socket')
snap5 = ('sudo ln -s /var/lib/snapd/snap /snap')
yay1 = ('git clone https://aur.archlinux.org/yay-git.git')
yay2 = ('cd yay && makepkg -si')
googlechrome = ('yay -S google-chrome')
güncelle = ('sudo pacman -Syu')
discord = ('sudo snap install discord')
opera = ('sudo snap install opera')
neofetch = ('sudo pacman -S neofecth')
woeusb1 = ('git clone https://aur.archlinux.org/woeusb-gui.git')
woeusb2 = ('cd woeusb-gui && makepkg -si')

if bileşen == 'evet':
    print('Gerekli Bileşenler Kuruluyor !')
    os.system(snap1)
    os.system(snap2)
    os.system(snap3)
    os.system(snap4)
    os.system(snap5)
    os.system(yay1)
    os.system(yay2)
    os.system(güncelle)

if soru == 'discord':
    print('Discord Kuruluyor !')
    os.system(discord)
    os.system(güncelle)

if soru == 'google chrome':
    print('Google Chrome Kuruluyor !')
    os.system(googlechrome)
    os.system(güncelle)

if soru == 'opera':
    print('Opera Kuruluyor !')
    os.system(opera)
    os.system(güncelle)
    
if soru == 'neofetch':
    print('Neofetch Kuruluyor !')
    os.system(neofetch)
    os.system(güncelle)

if soru == 'woeusb':
    print('Woeusb Kuruluyor !')
    os.system(woeusb1)
    os.system(woeusb2)
    os.system(güncelle)
