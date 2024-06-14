#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v12
# autospec commit: fbcebd0
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libkcddb
Version  : 24.05.1
Release  : 67
URL      : https://download.kde.org/stable/release-service/24.05.1/src/libkcddb-24.05.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.05.1/src/libkcddb-24.05.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.05.1/src/libkcddb-24.05.1.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
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
BuildRequires : gnupg
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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n libkcddb-24.05.1
cd %{_builddir}/libkcddb-24.05.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1718386231
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1718386231
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkcddb
cp %{_builddir}/libkcddb-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libkcddb/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libkcddb-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libkcddb/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/libkcddb-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/libkcddb/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/libkcddb-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkcddb/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/libkcddb-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkcddb/a4c60b3fefda228cd7439d3565df043192fef137 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kcmcddb
%find_lang libkcddb
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/applications/kcm_cddb.desktop
/usr/share/config.kcfg/libkcddb5.kcfg
/usr/share/qlogging-categories6/libkcddb.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KCddb6/KCDDB/CDInfo
/usr/include/KCddb6/KCDDB/Categories
/usr/include/KCddb6/KCDDB/Client
/usr/include/KCddb6/KCDDB/Config
/usr/include/KCddb6/KCDDB/Genres
/usr/include/KCddb6/KCDDB/KCDDB
/usr/include/KCddb6/kcddb/categories.h
/usr/include/KCddb6/kcddb/cdinfo.h
/usr/include/KCddb6/kcddb/client.h
/usr/include/KCddb6/kcddb/config.h
/usr/include/KCddb6/kcddb/configbase.h
/usr/include/KCddb6/kcddb/genres.h
/usr/include/KCddb6/kcddb/kcddb.h
/usr/include/KCddb6/kcddb/kcddb_export.h
/usr/include/KCddb6/kcddb_version.h
/usr/lib64/cmake/KCddb6/KCddb6Config.cmake
/usr/lib64/cmake/KCddb6/KCddb6ConfigVersion.cmake
/usr/lib64/cmake/KCddb6/KCddb6Targets-relwithdebinfo.cmake
/usr/lib64/cmake/KCddb6/KCddb6Targets.cmake
/usr/lib64/libKCddb6.so
/usr/lib64/qt6/mkspecs/modules/qt_KCddb.pri

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
/V3/usr/lib64/libKCddb6.so.5.1.0
/V3/usr/lib64/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_cddb.so
/usr/lib64/libKCddb6.so.5
/usr/lib64/libKCddb6.so.5.1.0
/usr/lib64/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_cddb.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkcddb/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/libkcddb/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/libkcddb/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/libkcddb/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/libkcddb/a4c60b3fefda228cd7439d3565df043192fef137

%files locales -f kcmcddb.lang -f libkcddb.lang
%defattr(-,root,root,-)

