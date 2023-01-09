#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3A6A4DB839EAA6D7 (aacid@kde.org)
#
Name     : libkcddb
Version  : 22.12.1
Release  : 46
URL      : https://download.kde.org/stable/release-service/22.12.1/src/libkcddb-22.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.1/src/libkcddb-22.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.1/src/libkcddb-22.12.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: libkcddb-data = %{version}-%{release}
Requires: libkcddb-lib = %{version}-%{release}
Requires: libkcddb-license = %{version}-%{release}
Requires: libkcddb-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package data
Summary: data components for the libkcddb package.
Group: Data

%description data
data components for the libkcddb package.


%package dev
Summary: dev components for the libkcddb package.
Group: Development
Requires: libkcddb-lib = %{version}-%{release}
Requires: libkcddb-data = %{version}-%{release}
Provides: libkcddb-devel = %{version}-%{release}
Requires: libkcddb = %{version}-%{release}

%description dev
dev components for the libkcddb package.


%package doc
Summary: doc components for the libkcddb package.
Group: Documentation

%description doc
doc components for the libkcddb package.


%package lib
Summary: lib components for the libkcddb package.
Group: Libraries
Requires: libkcddb-data = %{version}-%{release}
Requires: libkcddb-license = %{version}-%{release}

%description lib
lib components for the libkcddb package.


%package license
Summary: license components for the libkcddb package.
Group: Default

%description license
license components for the libkcddb package.


%package locales
Summary: locales components for the libkcddb package.
Group: Default

%description locales
locales components for the libkcddb package.


%prep
%setup -q -n libkcddb-22.12.1
cd %{_builddir}/libkcddb-22.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1673283169
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1673283169
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkcddb
cp %{_builddir}/libkcddb-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libkcddb/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libkcddb-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libkcddb/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/libkcddb-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/libkcddb/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/libkcddb-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkcddb/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/libkcddb-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkcddb/a4c60b3fefda228cd7439d3565df043192fef137 || :
pushd clr-build
%make_install
popd
%find_lang kcmcddb
%find_lang libkcddb

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/config.kcfg/libkcddb5.kcfg
/usr/share/kservices5/libkcddb.desktop
/usr/share/qlogging-categories5/libkcddb.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KCddb5/KCDDB/CDInfo
/usr/include/KCddb5/KCDDB/Categories
/usr/include/KCddb5/KCDDB/Client
/usr/include/KCddb5/KCDDB/Config
/usr/include/KCddb5/KCDDB/Genres
/usr/include/KCddb5/KCDDB/KCDDB
/usr/include/KCddb5/kcddb/categories.h
/usr/include/KCddb5/kcddb/cdinfo.h
/usr/include/KCddb5/kcddb/client.h
/usr/include/KCddb5/kcddb/config.h
/usr/include/KCddb5/kcddb/configbase.h
/usr/include/KCddb5/kcddb/genres.h
/usr/include/KCddb5/kcddb/kcddb.h
/usr/include/KCddb5/kcddb/kcddb_export.h
/usr/include/KF5/KCddb/Categories
/usr/include/KF5/KCddb/Cdinfo
/usr/include/KF5/KCddb/Client
/usr/include/KF5/KCddb/Genres
/usr/include/KF5/KCddb/Kcddb
/usr/include/KF5/KCddb/KcddbConfig
/usr/include/KF5/KCddb/categories.h
/usr/include/KF5/KCddb/cdinfo.h
/usr/include/KF5/KCddb/client.h
/usr/include/KF5/KCddb/genres.h
/usr/include/KF5/KCddb/kcddb.h
/usr/include/KF5/KCddb/kcddbconfig.h
/usr/include/KF5/kcddb_version.h
/usr/lib64/cmake/KF5Cddb/KF5CddbConfig.cmake
/usr/lib64/cmake/KF5Cddb/KF5CddbConfigVersion.cmake
/usr/lib64/cmake/KF5Cddb/KF5CddbTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Cddb/KF5CddbTargets.cmake
/usr/lib64/libKF5Cddb.so
/usr/lib64/qt5/mkspecs/modules/qt_KCddb.pri

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kcontrol/cddbretrieval5/index.cache.bz2
/usr/share/doc/HTML/ca/kcontrol/cddbretrieval5/index.docbook
/usr/share/doc/HTML/de/kcontrol/cddbretrieval5/index.cache.bz2
/usr/share/doc/HTML/de/kcontrol/cddbretrieval5/index.docbook
/usr/share/doc/HTML/de/kcontrol/cddbretrieval5/kscd14.png
/usr/share/doc/HTML/de/kcontrol/cddbretrieval5/kscd16.png
/usr/share/doc/HTML/en/kcontrol/cddbretrieval5/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol/cddbretrieval5/index.docbook
/usr/share/doc/HTML/en/kcontrol/cddbretrieval5/kscd13.png
/usr/share/doc/HTML/en/kcontrol/cddbretrieval5/kscd14.png
/usr/share/doc/HTML/en/kcontrol/cddbretrieval5/kscd16.png
/usr/share/doc/HTML/es/kcontrol/cddbretrieval5/index.cache.bz2
/usr/share/doc/HTML/es/kcontrol/cddbretrieval5/index.docbook
/usr/share/doc/HTML/fr/kcontrol/cddbretrieval5/index.cache.bz2
/usr/share/doc/HTML/fr/kcontrol/cddbretrieval5/index.docbook
/usr/share/doc/HTML/it/kcontrol/cddbretrieval5/index.cache.bz2
/usr/share/doc/HTML/it/kcontrol/cddbretrieval5/index.docbook
/usr/share/doc/HTML/nl/kcontrol/cddbretrieval5/index.cache.bz2
/usr/share/doc/HTML/nl/kcontrol/cddbretrieval5/index.docbook
/usr/share/doc/HTML/pt/kcontrol/cddbretrieval5/index.cache.bz2
/usr/share/doc/HTML/pt/kcontrol/cddbretrieval5/index.docbook
/usr/share/doc/HTML/pt_BR/kcontrol/cddbretrieval5/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kcontrol/cddbretrieval5/index.docbook
/usr/share/doc/HTML/pt_BR/kcontrol/cddbretrieval5/kscd14.png
/usr/share/doc/HTML/pt_BR/kcontrol/cddbretrieval5/kscd16.png
/usr/share/doc/HTML/ru/kcontrol/cddbretrieval5/index.cache.bz2
/usr/share/doc/HTML/ru/kcontrol/cddbretrieval5/index.docbook
/usr/share/doc/HTML/sr/kcontrol/cddbretrieval5/index.cache.bz2
/usr/share/doc/HTML/sr/kcontrol/cddbretrieval5/index.docbook
/usr/share/doc/HTML/sr@latin/kcontrol/cddbretrieval5/index.cache.bz2
/usr/share/doc/HTML/sr@latin/kcontrol/cddbretrieval5/index.docbook
/usr/share/doc/HTML/sv/kcontrol/cddbretrieval5/index.cache.bz2
/usr/share/doc/HTML/sv/kcontrol/cddbretrieval5/index.docbook
/usr/share/doc/HTML/uk/kcontrol/cddbretrieval5/index.cache.bz2
/usr/share/doc/HTML/uk/kcontrol/cddbretrieval5/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Cddb.so.5
/usr/lib64/libKF5Cddb.so.5.1.0
/usr/lib64/qt5/plugins/kcm_cddb.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkcddb/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/libkcddb/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/libkcddb/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/libkcddb/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/libkcddb/a4c60b3fefda228cd7439d3565df043192fef137

%files locales -f kcmcddb.lang -f libkcddb.lang
%defattr(-,root,root,-)

