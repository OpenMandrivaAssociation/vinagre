%define name vinagre
%define version 0.3
%define release %mkrel 1

Summary: VNC Client for the GNOME Desktop
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/vinagre/%{name}-%{version}.tar.bz2
Patch: vinagre-0.2-desktopfile.patch
License: GPLv2+
Group: Networking/Remote access
Url: http://www.gnome.org/projects/vinagre/index.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgtk-vnc-devel >= 0.2
BuildRequires: libglade2.0-devel
BuildRequires: libGConf2-devel
BuildRequires: libavahi-ui-devel
BuildRequires: perl-XML-Parser

%description
Vinagre is a VNC Client for the GNOME Desktop.
Features:
* You can connect to several machines at the same time, we like tabs
* You can keep track of your most used connections, we like favorites
* You can browse your network for VNC servers, we like avahi
* You don't need to supply the password on every connection, we like
  GNOME Keyring (well, this is not yet implemented)
* It's still in alpha stage (but usable), so, bugs are around

%prep
%setup -q
%patch -p1

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README
%_bindir/*
%_datadir/applications/*
%_datadir/%name
