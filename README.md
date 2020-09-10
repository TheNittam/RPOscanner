# RPOscanner By [@TheNittam](https://twitter.com/TheNittam)

Relative Path Overwrite Vulnerability Scanner - Version 1

Follow : [@CryptoGenNepal](https://twitter.com/cryptogennepal)

[![python](https://img.shields.io/badge/python-3.7-blue.svg?logo=python&labelColor=yellow)](https://www.python.org/downloads/) [![GitHub license](https://img.shields.io/github/license/TheNittam/RPOscanner)](https://github.com/TheNittam/RPOscanner/blob/master/LICENSE) [![platform](https://img.shields.io/badge/platform-osx%2Flinux%2Fwindows-green.svg)](https://github.com/TheNittam/RPOscanner/)

![RPO Scanner](RPO.png)

## Ever heard about **RPO Attack**?

If not here is the [video](https://www.youtube.com/watch?v=VrHkG5choM4) about **Relative Path Overwrite (RPO) Attack**. It's a lesser-known web-based vulnerability yet a very cool vulnerability. File descriptor was rewarded with 6000$ for his sweet exploit on this from Google. I have explained about this attack along with the mitigation techniques in our own language (**NEPALI** ![Love](https://cloud.githubusercontent.com/assets/4301109/16754758/82e3a63c-4813-11e6-9430-6015d98aeaab.png)).  It might be fruitful for not only security enthusiastic but also for developers.  

## Reference
Title | Researcher | Link 
------|------------|-----
RPO Gadget | [@filedescriptor](https://twitter.com/filedescriptor) | https://blog.innerht.ml/rpo-gadgets/
Detecting And Exploiting PRSSI | [James Kettle](https://twitter.com/albinowax) | https://portswigger.net/research/detecting-and-exploiting-path-relative-stylesheet-import-prssi-vulnerabilities

## How to use?
```python3 rpo.py <target_domain>```

## Required Module
```pip3 install requests```
