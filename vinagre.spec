%define name vinagre
%define version 0.4
%define release %mkrel 1

Summary: VNC Client for the GNOME Desktop
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/vinagre/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Networking/Remote access
Url: http://www.gnome.org/projects/vinagre/index.html
BuildRequires: libgtk-vnc-devel >= 0.3
BuildRequires: libglade2.0-devel
BuildRequires: libGConf2-devel
BuildRequires: libgnome-vfs2-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libavahi-ui-devel
BuildRequires: perl-XML-Parser
BuildRequires: desktop-file-utils
Requires(post):shared-mime-info
Requires(postun):shared-mime-info

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

%build
%configure2_5x --enable-avahi
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std
%find_lang %name
desktop-file-install --vendor="" \
  --add-category="RemoteAccess" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%post
%update_menus
%update_desktop_database
%update_mime_database
%update_icon_cache hicolor

%postun
%clean_menus
%clean_desktop_database
%clean_mime_database
%clean_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README
%_bindir/*
%_datadir/applications/*
%_datadir/%name
%_datadir/icons/hicolor/*/*/*.*
%_datadir/mime/packages/vinagre-mime.xml
