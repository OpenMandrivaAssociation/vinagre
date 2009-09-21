%define name vinagre
%define version 2.28.0.1
%define release %mkrel 1

Summary: VNC Client for the GNOME Desktop
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/vinagre/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Networking/Remote access
Url: http://www.gnome.org/projects/vinagre/index.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgtk-vnc-devel >= 0.3.3
#gw still needed by libpanel-applet-2.la:
BuildRequires: libglade2.0-devel libgnome-vfs2-devel
BuildRequires: libGConf2-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libavahi-ui-devel libavahi-gobject-devel
BuildRequires: gnome-panel-devel
BuildRequires: libtelepathy-glib-devel
BuildRequires: gnome-doc-utils >= 0.3.2
BuildRequires: intltool
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

%package devel
Summary: VNC Client for the GNOME Desktop - development files
Group: Development/C
Requires: %name = %version-%release

%description devel
Vinagre is a VNC Client for the GNOME Desktop.
Features:
* You can connect to several machines at the same time, we like tabs
* You can keep track of your most used connections, we like favorites
* You can browse your network for VNC servers, we like avahi
* You don't need to supply the password on every connection, we like
  GNOME Keyring (well, this is not yet implemented)
* It's still in alpha stage (but usable), so, bugs are around

Install this package if you want to build plugins for %name.

%prep
%setup -q

%build
%configure2_5x --enable-avahi
%make LIBS="-lavahi-gobject -lavahi-ui"

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std
%find_lang %name --with-gnome
for omf in %buildroot%_datadir/omf/*/*-??*.omf;do
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed s!%buildroot!!)" >> %name.lang
done

desktop-file-install --vendor="" \
  --add-category="RemoteAccess" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

rm -f %buildroot%_libdir/%name-1/plugin*/*.a

%if %mdkversion < 200900
%post
%update_menus
%update_desktop_database
%update_mime_database
%update_icon_cache hicolor
%post_install_gconf_schemas vinagre
%endif

%preun
%preun_uninstall_gconf_schemas vinagre

%if %mdkversion < 200900
%postun
%clean_menus
%clean_desktop_database
%clean_mime_database
%clean_icon_cache hicolor
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README
%_sysconfdir/gconf/schemas/vinagre.schemas
%_bindir/*
%_datadir/applications/*
%_datadir/%name
%dir %_datadir/omf/vinagre
%_datadir/omf/vinagre/vinagre-C.omf
%_datadir/icons/hicolor/*/*/*.*
%_datadir/mime/packages/vinagre-mime.xml
%_datadir/dbus-1/services/org.gnome.Empathy.StreamTubeHandler.rfb.service
%_mandir/man1/vinagre.1*
%_libdir/bonobo/servers/GNOME_VinagreApplet.server
%_libexecdir/vinagre-applet
%_libdir/%name-1/plugin-loaders/libcloader.so
%_libdir/%name-1/plugin-loaders/libcloader.la
%_libdir/%name-1/plugins/libvnc.so
%_libdir/%name-1/plugins/libvnc.la
%_libdir/%name-1/plugins/vnc.vinagre-plugin

%files devel
%defattr(-,root,root)
%doc ChangeLog
%_includedir/%name-1.0
%_libdir/pkgconfig/%name-1.0.pc
