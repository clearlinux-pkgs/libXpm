#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0xCFDF148828C642A7 (alan.coopersmith@oracle.com)
#
Name     : libXpm
Version  : 3.5.17
Release  : 19
URL      : https://www.x.org/releases/individual/lib/libXpm-3.5.17.tar.xz
Source0  : https://www.x.org/releases/individual/lib/libXpm-3.5.17.tar.xz
Source1  : https://www.x.org/releases/individual/lib/libXpm-3.5.17.tar.xz.sig
Summary  : X Pixmap Library
Group    : Development/Tools
License  : MIT
Requires: libXpm-bin = %{version}-%{release}
Requires: libXpm-lib = %{version}-%{release}
Requires: libXpm-license = %{version}-%{release}
Requires: libXpm-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glib-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(32xextproto)
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(32xproto)
BuildRequires : pkgconfig(32xt)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
BuildRequires : pkgconfig(xt)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
libXpm - X Pixmap (XPM) image file format library
-------------------------------------------------

%package bin
Summary: bin components for the libXpm package.
Group: Binaries
Requires: libXpm-license = %{version}-%{release}

%description bin
bin components for the libXpm package.


%package dev
Summary: dev components for the libXpm package.
Group: Development
Requires: libXpm-lib = %{version}-%{release}
Requires: libXpm-bin = %{version}-%{release}
Provides: libXpm-devel = %{version}-%{release}
Requires: libXpm = %{version}-%{release}

%description dev
dev components for the libXpm package.


%package dev32
Summary: dev32 components for the libXpm package.
Group: Default
Requires: libXpm-lib32 = %{version}-%{release}
Requires: libXpm-bin = %{version}-%{release}
Requires: libXpm-dev = %{version}-%{release}

%description dev32
dev32 components for the libXpm package.


%package lib
Summary: lib components for the libXpm package.
Group: Libraries
Requires: libXpm-license = %{version}-%{release}

%description lib
lib components for the libXpm package.


%package lib32
Summary: lib32 components for the libXpm package.
Group: Default
Requires: libXpm-license = %{version}-%{release}

%description lib32
lib32 components for the libXpm package.


%package license
Summary: license components for the libXpm package.
Group: Default

%description license
license components for the libXpm package.


%package man
Summary: man components for the libXpm package.
Group: Default

%description man
man components for the libXpm package.


%prep
%setup -q -n libXpm-3.5.17
cd %{_builddir}/libXpm-3.5.17
pushd ..
cp -a libXpm-3.5.17 build32
popd
pushd ..
cp -a libXpm-3.5.17 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1696358365
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static --disable-stat-zfile --disable-open-zfile
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --disable-stat-zfile --disable-open-zfile   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
%configure --disable-static --disable-stat-zfile --disable-open-zfile
make  %{?_smp_mflags}
popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1696358365
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libXpm
cp %{_builddir}/libXpm-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libXpm/0353e2351020adff9883789359be7a5a6c688c96 || :
cp %{_builddir}/libXpm-%{version}/COPYRIGHT %{buildroot}/usr/share/package-licenses/libXpm/a4777b6caf11b08abc996727d094e2dafc16caaa || :
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/cxpm
/V3/usr/bin/sxpm
/usr/bin/cxpm
/usr/bin/sxpm

%files dev
%defattr(-,root,root,-)
/usr/include/X11/xpm.h
/usr/lib64/libXpm.so
/usr/lib64/pkgconfig/xpm.pc
/usr/share/man/man3/XpmAttributesSize.3
/usr/share/man/man3/XpmCreateBuffer.3
/usr/share/man/man3/XpmCreateBufferFromImage.3
/usr/share/man/man3/XpmCreateBufferFromPixmap.3
/usr/share/man/man3/XpmCreateBufferFromXpmImage.3
/usr/share/man/man3/XpmCreateData.3
/usr/share/man/man3/XpmCreateDataFromImage.3
/usr/share/man/man3/XpmCreateDataFromPixmap.3
/usr/share/man/man3/XpmCreateDataFromXpmImage.3
/usr/share/man/man3/XpmCreateImage.3
/usr/share/man/man3/XpmCreateImageFromBuffer.3
/usr/share/man/man3/XpmCreateImageFromData.3
/usr/share/man/man3/XpmCreateImageFromXpmImage.3
/usr/share/man/man3/XpmCreatePixmap.3
/usr/share/man/man3/XpmCreatePixmapFromBuffer.3
/usr/share/man/man3/XpmCreatePixmapFromData.3
/usr/share/man/man3/XpmCreatePixmapFromXpmImage.3
/usr/share/man/man3/XpmCreateXpmImage.3
/usr/share/man/man3/XpmCreateXpmImageFromBuffer.3
/usr/share/man/man3/XpmCreateXpmImageFromData.3
/usr/share/man/man3/XpmCreateXpmImageFromImage.3
/usr/share/man/man3/XpmCreateXpmImageFromPixmap.3
/usr/share/man/man3/XpmFree.3
/usr/share/man/man3/XpmFreeAttributes.3
/usr/share/man/man3/XpmFreeExtensions.3
/usr/share/man/man3/XpmFreeXpmImage.3
/usr/share/man/man3/XpmFreeXpmInfo.3
/usr/share/man/man3/XpmGetErrorString.3
/usr/share/man/man3/XpmLibraryVersion.3
/usr/share/man/man3/XpmMisc.3
/usr/share/man/man3/XpmRead.3
/usr/share/man/man3/XpmReadFileToBuffer.3
/usr/share/man/man3/XpmReadFileToData.3
/usr/share/man/man3/XpmReadFileToImage.3
/usr/share/man/man3/XpmReadFileToPixmap.3
/usr/share/man/man3/XpmReadFileToXpmImage.3
/usr/share/man/man3/XpmWrite.3
/usr/share/man/man3/XpmWriteFileFromBuffer.3
/usr/share/man/man3/XpmWriteFileFromImage.3
/usr/share/man/man3/XpmWriteFileFromPixmap.3
/usr/share/man/man3/XpmWriteFileFromXpmImage.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libXpm.so
/usr/lib32/pkgconfig/32xpm.pc
/usr/lib32/pkgconfig/xpm.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libXpm.so.4.11.0
/usr/lib64/libXpm.so.4
/usr/lib64/libXpm.so.4.11.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libXpm.so.4
/usr/lib32/libXpm.so.4.11.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libXpm/0353e2351020adff9883789359be7a5a6c688c96
/usr/share/package-licenses/libXpm/a4777b6caf11b08abc996727d094e2dafc16caaa

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cxpm.1
/usr/share/man/man1/sxpm.1
