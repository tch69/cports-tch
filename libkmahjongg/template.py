pkgname = "libkmahjongg"
pkgver = "25.04.3"
pkgrel = 0
build_style = "cmake"

hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja"
]

makedepends = [
    "gettext-devel",
    "kcompletion-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel"
]

pkgdesc = "Common code, backgrounds and tile sets for games using Mahjongg tiles"
license = "GPL-2.0-or-later"
url = "https://kde.org/applications/games"
source = f"https://download.kde.org/stable/release-service/{pkgver}/src/libkmahjongg-{pkgver}.tar.xz"
sha256 = "6570b054d02b12f7c0b37d28dd8930c17cc6a4616437613448ab69cc4b08446c"

@subpackage("libkmahjongg-devel")
def _(self):
    return self.default_devel()
