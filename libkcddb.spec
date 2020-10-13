#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : libkcddb
Version  : 20.08.2
Release  : 22
URL      : https://download.kde.org/stable/release-service/20.08.2/src/libkcddb-20.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.08.2/src/libkcddb-20.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.08.2/src/libkcddb-20.08.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: libkcddb-data = %{version}-%{release}
Requires: libkcddb-lib = %{version}-%{release}
Requires: libkcddb-license = %{version}-%{release}
Requires: libkcddb-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n libkcddb-20.08.2
cd %{_builddir}/libkcddb-20.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602611363
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1602611363
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkcddb
cp %{_builddir}/libkcddb-20.08.2/COPYING %{buildroot}/usr/share/package-licenses/libkcddb/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/libkcddb-20.08.2/COPYING.DOC %{buildroot}/usr/share/package-licenses/libkcddb/fcbf818f92ef8679a88f3778b12b4c8b5810545b
cp %{_builddir}/libkcddb-20.08.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/libkcddb/ba8966e2473a9969bdcab3dc82274c817cfd98a1
cp %{_builddir}/libkcddb-20.08.2/cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/libkcddb/ff3ed70db4739b3c6747c7f624fe2bad70802987
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

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KCddb/Categories
/usr/include/KF5/KCddb/Cdinfo
/usr/include/KF5/KCddb/Client
/usr/include/KF5/KCddb/Genres
/usr/include/KF5/KCddb/Kcddb
/usr/include/KF5/KCddb/KcddbConfig
/usr/include/KF5/KCddb/categories.h
/usr/include/KF5/KCddb/cdinfo.h
/usr/include/KF5/KCddb/client.h
/usr/include/KF5/KCddb/configbase.h
/usr/include/KF5/KCddb/genres.h
/usr/include/KF5/KCddb/kcddb.h
/usr/include/KF5/KCddb/kcddb_export.h
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
/usr/share/doc/HTML/sr/kcontrol/cddbretrieval5/index.cache.bz2
/usr/share/doc/HTML/sr/kcontrol/cddbretrieval5/index.docbook
/usr/share/doc/HTML/sv/kcontrol/cddbretrieval5/index.cache.bz2
/usr/share/doc/HTML/sv/kcontrol/cddbretrieval5/index.docbook
/usr/share/doc/HTML/uk/kcontrol/cddbretrieval5/index.cache.bz2
/usr/share/doc/HTML/uk/kcontrol/cddbretrieval5/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Cddb.so.5
/usr/lib64/libKF5Cddb.so.5.0.0
/usr/lib64/qt5/plugins/kcm_cddb.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkcddb/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/libkcddb/ba8966e2473a9969bdcab3dc82274c817cfd98a1
/usr/share/package-licenses/libkcddb/fcbf818f92ef8679a88f3778b12b4c8b5810545b
/usr/share/package-licenses/libkcddb/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files locales -f kcmcddb.lang -f libkcddb.lang
%defattr(-,root,root,-)

