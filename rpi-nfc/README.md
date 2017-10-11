NFC
===

[Exploren-nfc handleiding (Element14)](https://www.element14.com/community/servlet/JiveServlet/previewBody/65446-102-3-310028/AN11480.pdf)

1/. sudo dpkg -i libneardal<version>_armhf.deb wiringpi<version>.deb neardexplorenfc_<version>_armhf.deb

Installation
------------

```
sudo dpkg -i libneardal0_0.14-1_armhf.deb libwiringpi2-2.25-1_armhf.deb neard-explorenfc_0.4-1_armhf.deb
```

### nxppy

nxppy is a **very** simple Python wrapper for interfacing with the excellent <a href="https://www.newark.com/nxp/explore-nfc-ww/nfc-add-on-board-raspberry-pi/dp/45X6356">NXP EXPLORE-NFC shield</a> for the <a href="http://www.raspberrypi.org/">Raspberry Pi</a>.  It takes NXP's NFC Reader Library and provides a thin layer for detecting a Mifare NFC tag, reading its UID (unique identifier), and reading/writing data from/to the user area.</p>

- [Source nxppy](https://github.com/svvitale/nxppy)

```
sudo apt-get update
sudo apt-get install build-essential cmake python3-dev unzip wget
sudo pip3 install nxppy
```

Version `nxppy-1.5.1` on 10-11-2017.
