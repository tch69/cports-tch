pkgname = "kmahjongg"
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
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "knewstuff-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "libkdegames-devel",
    "libkmahjongg-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
]

pkgdesc = "Common code, backgrounds and tile sets for games using Mahjongg tiles"
license = "GPL-2.0-or-later"
url = "https://kde.org/applications/games"
source = f"https://download.kde.org/stable/release-service/{pkgver}/src/kmahjongg-{pkgver}.tar.xz"
sha256 = "6c67b56b0823facae97b0061db2613d8d901151d26f195e87e0833057b66b795"
