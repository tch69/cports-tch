pkgname = "unclutter-xfixes"
pkgver = "1.6"
pkgrel = 2
build_style = "makefile"
makedepends = [ "asciidoc",
               "libev-devel",
               "libxfixes-devel",
               "libxi-devel",
               ]
pkgdesc = "Hide the cursors on inactivity"
license = "MIT"
url = "https://github.com/Airblader/unclutter-xfixes"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "6f7f248f16b7d4ec7cb144b6bc5a66bd49078130513a184f4dc16c498d457db9"
# No tests
options = ["!check"]

def build(self):
    self.do(
        "make",
        "CC=clang",
        "LDFLAGS=-lev -lX11 -lXi -lXfixes -L/usr/lib",
    )

def install(self):
    self.install_file(f"unclutter", "usr/bin", name = "unclutter-xfixes")
    self.install_file(f"man/unclutter-xfixes.1", "usr/share/man/man1")
    self.install_license("LICENSE")
