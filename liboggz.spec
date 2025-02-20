#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	A library for reading and writing Ogg encapsulated data
Summary(pl.UTF-8):	Biblioteka do odczytu i zapisu danych w opakowaniu Ogg
Name:		liboggz
Version:	1.1.1
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/liboggz/%{name}-%{version}.tar.gz
# Source0-md5:	3649a657f8e368b881ba8b1b57381ff7
Patch0:		%{name}-destdir.patch
URL:		http://www.xiph.org/oggz/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	docbook-to-man
BuildRequires:	libogg-devel >= 2:1.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libogg >= 2:1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
liboggz is a library that provides simple parsing and seeking of files
and streams based on the Ogg file format. liboggz requires libogg to
work.

liboggz knows about Ogg Speex, Ogg Vorbis, Ogg Theora, and the Ogg
based Annodex formats, thus allows parsing (though not decoding) of
these files. For getting decoding and encoding functionality you will
require in addition libspeex, libvorbis, libtheora, and libannodex
respectively.

%description -l pl.UTF-8
liboggz to biblioteka umożliwiająca prostą analizę i przeszukiwanie
plików i strumieni opartych na formacie Ogg. liboggz wymaga do
działania biblioteki libogg.

liboggz wie o formatach Ogg Speex, Ogg Vorbis, Ogg Theora oraz
opartych na Ogg formatach Annodex, co pozwala analizować (ale nie
dekodować) pliki w tych formatach. Kodowanie i dekodowanie ich
wymaga dodatkowych bibliotek - odpowiednio: libspeex, libvorbis,
libtheora, libannodex.

%package devel
Summary:	Header files for liboggz library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki liboggz
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libogg-devel >= 2:1.0

%description devel
Header files for liboggz library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki liboggz.

%package static
Summary:	Static liboggz library
Summary(pl.UTF-8):	Statyczna biblioteka liboggz
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liboggz library.

%description static -l pl.UTF-8
Statyczna biblioteka liboggz.

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -rf $RPM_BUILD_ROOT%{_docdir}/liboggz

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/oggz*
%attr(755,root,root) %{_libdir}/liboggz.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboggz.so.2
%{_mandir}/man1/oggz*.1*

%files devel
%defattr(644,root,root,755)
%doc doc/liboggz/html/*
%attr(755,root,root) %{_libdir}/liboggz.so
%{_libdir}/liboggz.la
%{_includedir}/oggz
%{_pkgconfigdir}/oggz.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/liboggz.a
%endif
