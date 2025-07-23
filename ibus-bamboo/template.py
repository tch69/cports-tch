pkgname = "ibus-bamboo"
pkgver = "0.8.4"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["go", "pkgconf"]
makedepends = ["gtk+3-devel", "ibus-devel", "pkgconf-devel"]
pkgdesc = "Vietnamese IME for IBus"
license = "GPL-3.0-only"
url = "https://github.com/BambooEngine/ibus-bamboo"
source = f"https://github.com/BambooEngine/{pkgname}/archive/v{pkgver}-RC6.tar.gz"
sha256 = "610031553a033cde9f0c8bb08fd8578763611f24964566973997d7ae57a3c99e"
# Program contains no tests
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
