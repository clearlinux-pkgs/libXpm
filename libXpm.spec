#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x687393EE37D128F8 (matthieu@herrb.eu)
#
Name     : libXpm
Version  : 3.5.12
Release  : 10
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXpm-3.5.12.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXpm-3.5.12.tar.bz2
Source99 : http://xorg.freedesktop.org/releases/individual/lib/libXpm-3.5.12.tar.bz2.sig
Summary  : X Pixmap Library
Group    : Development/Tools
License  : MIT
Requires: libXpm-bin
Requires: libXpm-lib
Requires: libXpm-doc
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
BuildRequires : pkgconfig(xt)

%description
libXpm - X Pixmap (XPM) image file format library
All questions regarding this software should be directed at the
Xorg mailing list:

%package bin
Summary: bin components for the libXpm package.
Group: Binaries

%description bin
bin components for the libXpm package.


%package dev
Summary: dev components for the libXpm package.
Group: Development
Requires: libXpm-lib
Requires: libXpm-bin
Provides: libXpm-devel

%description dev
dev components for the libXpm package.


%package doc
Summary: doc components for the libXpm package.
Group: Documentation

%description doc
doc components for the libXpm package.


%package lib
Summary: lib components for the libXpm package.
Group: Libraries

%description lib
lib components for the libXpm package.


%prep
%setup -q -n libXpm-3.5.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1500994170
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1500994170
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cxpm
/usr/bin/sxpm

%files dev
%defattr(-,root,root,-)
/usr/include/X11/xpm.h
/usr/lib64/libXpm.so
/usr/lib64/pkgconfig/xpm.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libXpm.so.4
/usr/lib64/libXpm.so.4.11.0
