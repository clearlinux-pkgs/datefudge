#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : datefudge
Version  : 1.23
Release  : 3
URL      : https://mirrors.kernel.org/debian/pool/main/d/datefudge/datefudge_1.23.tar.xz
Source0  : https://mirrors.kernel.org/debian/pool/main/d/datefudge/datefudge_1.23.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: datefudge-bin = %{version}-%{release}
Requires: datefudge-lib = %{version}-%{release}
Requires: datefudge-license = %{version}-%{release}
Requires: datefudge-man = %{version}-%{release}
Patch1: 0001-Fix-build.patch

%description
All files in this repository / Debian archive are (c) 2002-2003
by Matthias Urlichs <smurf@noris.de>. They are licensed under the Gnu
Public License, version 2, included as the file "COPYING".

%package bin
Summary: bin components for the datefudge package.
Group: Binaries
Requires: datefudge-license = %{version}-%{release}

%description bin
bin components for the datefudge package.


%package lib
Summary: lib components for the datefudge package.
Group: Libraries
Requires: datefudge-license = %{version}-%{release}

%description lib
lib components for the datefudge package.


%package license
Summary: license components for the datefudge package.
Group: Default

%description license
license components for the datefudge package.


%package man
Summary: man components for the datefudge package.
Group: Default

%description man
man components for the datefudge package.


%prep
%setup -q -n datefudge-1.23
cd %{_builddir}/datefudge-1.23
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573418270
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1573418270
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/datefudge
cp %{_builddir}/datefudge-1.23/COPYING %{buildroot}/usr/share/package-licenses/datefudge/dfac199a7539a404407098a2541b9482279f690d
cp %{_builddir}/datefudge-1.23/debian/copyright %{buildroot}/usr/share/package-licenses/datefudge/462bb477ef46df38abade60d3044466969fbf068
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/datefudge

%files lib
%defattr(-,root,root,-)
/usr/lib64/datefudge/datefudge.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/datefudge/462bb477ef46df38abade60d3044466969fbf068
/usr/share/package-licenses/datefudge/dfac199a7539a404407098a2541b9482279f690d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/datefudge.1
