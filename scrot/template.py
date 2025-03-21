pkgname = "scrot"
pkgver = "1.11.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
        "--docdir=/usr/share/doc/scrot",
]
configure_gen = []
hostmakedepends = [
        "pkgconf",
        ]
makedepends = [
               "imlib2-devel",
               "libx11-devel",
               "libxcomposite-devel",
               "libxfixes-devel",
               "libxinerama-devel",
               "musl-bsd-headers",
               "pkgconf-devel",
               ]
pkgdesc = "Simple screenshot utility for X"
license = "MIT"
url = "https://github.com/resurrecting-open-source-projects/scrot"
source = f"{url}/releases/download/{pkgver}/scrot-{pkgver}.tar.gz"
sha256 = "c8ceda53b4ff76df4b9e51e9397acb4bcf12a51418895bf80c41f2a890e44738"
# There are no tests
options = ["!check"]

def post_install(self):
    self.install_license("COPYING")
