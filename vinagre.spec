%define api 3.0

Summary: VNC Client for the GNOME Desktop
Name: vinagre
Version: 3.2.2
Release: 1
License: GPLv2+
Group: Networking/Remote access
Url: http://www.gnome.org/projects/vinagre/index.html
Source0: http://ftp.gnome.org/pub/GNOME/sources/vinagre/%{name}-%{version}.tar.xz
Patch0:	vinagre-3.1.3-modules.patch

BuildRequires:	desktop-file-utils
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(avahi-ui-gtk3)
BuildRequires:	pkgconfig(avahi-gobject)
BuildRequires:	pkgconfig(avahi-ui)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-icon-theme)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk-vnc-2.0)
BuildRequires:	pkgconfig(libpanelapplet-4.0)
BuildRequires:	pkgconfig(libpeas-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
#BuildRequires:	pkgconfig(spice-client-gtk-3.0)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(vte-2.90)

Requires(post):shared-mime-info
Requires(postun):shared-mime-info

%description
Vinagre is a VNC Client for the GNOME Desktop.

With Vinagre you can have several connections open simultaneously, bookmark
your servers thanks to the Favorites support, store the passwords in the
GNOME keyring, and browse the network to look for VNC servers.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--enable-ssh

%make

%install
rm -rf %{buildroot} %{name}.lang
%makeinstall_std
%find_lang %{name} --with-gnome

desktop-file-install --vendor="" \
	--add-category="RemoteAccess" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

rm -f %{buildroot}%{_libdir}/%{name}-%{api}/plugin*/*.la

%files -f %{name}.lang
%doc AUTHORS NEWS README
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/%{name}
%dir %{_libdir}/%{name}-%{api}/
%dir %{_libdir}/%{name}-%{api}/plugins/
%{_libdir}/%{name}-%{api}/plugins/*.so
#{_libdir}/%{name}-%{api}/plugins/vnc/
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Vinagre.service
%{_datadir}/GConf/gsettings/org.gnome.Vinagre.convert
%{_datadir}/glib-2.0/schemas/org.gnome.Vinagre.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.*
%{_datadir}/mime/packages/vinagre-mime.xml
%{_datadir}/telepathy/clients/Vinagre.client
%{_mandir}/man1/vinagre.1*

