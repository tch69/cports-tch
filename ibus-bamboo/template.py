pkgname = "ibus-bamboo"
pkgver = "0.8.4"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["go", "pkgconf"]
makedepends = ["gtk+3-devel", "ibus-devel", "pkgconf-devel"]
pkgdesc = "Vietnamese IME for IBus"
license = "GPL-3.0-only"
url = "https://github.com/BambooEngine/ibus-bamboo"
source = f"https://github.com/BambooEngine/{pkgname}/archive/v{pkgver}-RC1.tar.gz"
sha256 = "8ca197b5234a2a8c93ca9852376b8ba31cb29311fff26c53d6a1ffce538d1ef2"
# Program contains no tests
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
