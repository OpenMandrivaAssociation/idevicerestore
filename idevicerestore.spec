%define git 20211124

Name:		idevicerestore
Version:	1.0.0
Release:	1.%{git}.0
Summary:	Restore firmware files to ios devices
Group:		System/Libraries
License:	GPLv2+
URL:		http://www.libimobiledevice.org/
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(libirecovery-1.0)
BuildRequires:	pkgconfig(libimobiledevice-1.0)
BuildRequires:	pkgconfig(libplist-2.0)
BuildRequires:	pkgconfig(libimobiledevice-glue-1.0)
BuildRequires:	pkgconfig(libzip)
BuildRequires:	pkgconfig(libcurl) 
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(openssl)

%description
A command-line application to restore firmware files to iOS devices

%prep
%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS COPYING README.md
%{_bindir}/idevicerestore
%{_mandir}/man1/*
