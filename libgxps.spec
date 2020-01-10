Name:           libgxps
Version:        0.2.5
Release:        1%{?dist}
Summary:        GObject based library for handling and rendering XPS documents
Group:          System Environment/Libraries

License:        LGPLv2+
URL:            http://live.gnome.org/libgxps
Source0:        http://ftp.gnome.org/pub/gnome/sources/%{name}/0.2/%{name}-%{version}.tar.xz

Patch0:         libgxps-0.2.4-GXPSImage.patch
Patch1:         libgxps-0.2.5-private-methods.patch

BuildRequires:  gtk3-devel
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  cairo-devel
BuildRequires:  libarchive-devel
BuildRequires:  freetype-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  lcms2-devel
BuildRequires:  chrpath

%description
libgxps is a GObject based library for handling and rendering XPS
documents.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tools
Summary:        Command-line utility programs for manipulating XPS files
Group:          Applications/Text
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
The %{name}-tools contains command-line programs for manipulating XPS format
documents using the %{name} library.


%prep
%setup -q
%patch0 -p1 -b .GXPSImage
%patch1 -p1 -b .private-methods


%build
autoreconf -ivf
%configure --disable-static --enable-man
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/xpsto*


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/libgxps

%files tools
%{_bindir}/xpsto*
%{_mandir}/man1/xpsto*.1.gz


%changelog
* Tue Feb 28 2017 Marek Kasik <mkasik@redhat.com> - 0.2.5-1
- Update to newly released 0.2.5
- Preserve ABI by exporting the same set of methods as before
- Resolves: #1384959

* Fri Feb 17 2017 Marek Kasik <mkasik@redhat.com> - 0.2.4-1
- Update to 0.2.4
- Backport several important patches from current master
- Revert addition of GXPSImage (it would change ABI)
- Resolves: #1384959

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.2.2-9
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.2.2-8
- Mass rebuild 2013-12-27

* Tue Mar 26 2013 Daniel Mach <dmach@redhat.com> - 0.2.2-7.1
- Rebuild for libarchive

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.2.2-6
- rebuild due to "jpeg8-ABI" feature drop

* Thu Jan 17 2013 Tomas Bzatek <tbzatek@redhat.com> - 0.2.2-5
- Rebuilt for new libarchive

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.2.2-4
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May  6 2012 Tom Hughes <tom@compton.nu> - 0.2.2-2
- Rebuilt for new libtiff.

* Mon Mar 19 2012 Tom Hughes <tom@compton.nu> - 0.2.2-1
- Update to 0.2.2 upstream release.

* Thu Jan 26 2012 Tomas Bzatek <tbzatek@redhat.com> - 0.2.1-4
- Rebuilt for new libarchive

* Thu Jan 26 2012 Tom Hughes <tom@compton.nu> - 0.2.1-3
- Correct summary and description for tools package.

* Thu Jan 26 2012 Tom Hughes <tom@compton.nu> - 0.2.1-2
- Rebuild for libarchive soname bump.

* Sat Jan 21 2012 Tom Hughes <tom@compton.nu> - 0.2.1-1
- Update to 0.2.1 upstream release.

* Wed Jan  4 2012 Tom Hughes <tom@compton.nu> - 0.2.0-2
- Rebuilt for gcc 4.7 mass rebuild.
- Run autoreconf to update libtool.

* Thu Dec  1 2011 Tom Hughes <tom@compton.nu> - 0.2.0-1
- Update to 0.2.0 upstream release.

* Sat Nov  5 2011 Tom Hughes <tom@compton.nu> - 0.1.0-2
- Fix base package dependency in devel package.

* Fri Nov  4 2011 Tom Hughes <tom@compton.nu> - 0.1.0-1
- Initial build.
