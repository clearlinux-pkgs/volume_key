#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : volume_key
Version  : 0.3.12
Release  : 17
URL      : https://github.com/felixonmars/volume_key/archive/volume_key-0.3.12.tar.gz
Source0  : https://github.com/felixonmars/volume_key/archive/volume_key-0.3.12.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: volume_key-bin = %{version}-%{release}
Requires: volume_key-lib = %{version}-%{release}
Requires: volume_key-license = %{version}-%{release}
Requires: volume_key-locales = %{version}-%{release}
Requires: volume_key-man = %{version}-%{release}
Requires: volume_key-python = %{version}-%{release}
Requires: volume_key-python3 = %{version}-%{release}
BuildRequires : gettext
BuildRequires : gnupg
BuildRequires : gpgme-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libcryptsetup)
BuildRequires : pkgconfig(nss)
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : swig

%description
About
=====
The volume_key project provides a libvolume_key, a library for manipulating
storage volume encryption keys and storing them separately from volumes, and an
associated command-line tool, named volume_key.

%package bin
Summary: bin components for the volume_key package.
Group: Binaries
Requires: volume_key-license = %{version}-%{release}
Requires: volume_key-man = %{version}-%{release}

%description bin
bin components for the volume_key package.


%package dev
Summary: dev components for the volume_key package.
Group: Development
Requires: volume_key-lib = %{version}-%{release}
Requires: volume_key-bin = %{version}-%{release}
Provides: volume_key-devel = %{version}-%{release}

%description dev
dev components for the volume_key package.


%package legacypython
Summary: legacypython components for the volume_key package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the volume_key package.


%package lib
Summary: lib components for the volume_key package.
Group: Libraries
Requires: volume_key-license = %{version}-%{release}

%description lib
lib components for the volume_key package.


%package license
Summary: license components for the volume_key package.
Group: Default

%description license
license components for the volume_key package.


%package locales
Summary: locales components for the volume_key package.
Group: Default

%description locales
locales components for the volume_key package.


%package man
Summary: man components for the volume_key package.
Group: Default

%description man
man components for the volume_key package.


%package python
Summary: python components for the volume_key package.
Group: Default
Requires: volume_key-python3 = %{version}-%{release}

%description python
python components for the volume_key package.


%package python3
Summary: python3 components for the volume_key package.
Group: Default
Requires: python3-core

%description python3
python3 components for the volume_key package.


%prep
%setup -q -n volume_key-volume_key-0.3.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539035066
%reconfigure --disable-static --with-python3
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check ||:

%install
export SOURCE_DATE_EPOCH=1539035066
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/volume_key
cp COPYING %{buildroot}/usr/share/package-licenses/volume_key/COPYING
%make_install
%find_lang volume_key
## install_append content
sed -i '/#include <config.h>/d' %{buildroot}/usr/include/volume_key/libvolume_key.h
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/volume_key

%files dev
%defattr(-,root,root,-)
/usr/include/volume_key/libvolume_key.h
/usr/lib64/libvolume_key.so

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvolume_key.so.1
/usr/lib64/libvolume_key.so.1.2.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/volume_key/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/volume_key.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f volume_key.lang
%defattr(-,root,root,-)

