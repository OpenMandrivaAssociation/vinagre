%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	VNC Client for the GNOME Desktop
Name:		vinagre
Version:	3.6.2
Release:	1
License:	GPLv2+
Group:		Networking/Remote access
Url:		http://www.gnome.org/projects/vinagre/index.html
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	pkgconfig(avahi-ui-gtk3) >= 0.6.26
BuildRequires:	pkgconfig(avahi-gobject) >= 0.6.26
BuildRequires:	pkgconfig(avahi-ui)
BuildRequires:	pkgconfig(glib-2.0) >= 2.25.11
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.3
BuildRequires:	pkgconfig(gtk-vnc-2.0) >= 0.4.3
BuildRequires:	pkgconfig(libpeas-1.0) >= 0.7.2
BuildRequires:	pkgconfig(libpanelapplet-4.0) >= 2.91.91
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(libxml-2.0) >= 2.6.31
BuildRequires:	pkgconfig(spice-client-gtk-3.0) >= 0.5
BuildRequires:	pkgconfig(telepathy-glib) >= 0.11.6
BuildRequires:	pkgconfig(vte-2.90) >= 0.20

Requires:	gnome-icon-theme >= 2.30

%description
Vinagre is a VNC Client for the GNOME Desktop.

With Vinagre you can have several connections open simultaneously, bookmark
your servers thanks to the Favorites support, store the passwords in the
GNOME keyring, and browse the network to look for VNC servers.

%prep
%setup -q

%build
%configure2_5x --enable-ssh
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

desktop-file-install --vendor="" \
	--add-category="RemoteAccess;Network" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%files -f %{name}.lang
%doc AUTHORS NEWS README
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/*/*.*
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Vinagre.service
%{_datadir}/GConf/gsettings/org.gnome.Vinagre.convert
%{_datadir}/glib-2.0/schemas/org.gnome.Vinagre.gschema.xml
%{_datadir}/mime/packages/vinagre-mime.xml
%{_datadir}/telepathy/clients/Vinagre.client
%{_mandir}/man1/vinagre.1*

