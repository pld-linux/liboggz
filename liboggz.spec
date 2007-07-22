# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	A library for reading and writing Ogg encapsulated data
Summary(pl.UTF-8):	Biblioteka do odczytu i zapisu danych w opakowaniu Ogg
Name:		liboggz
Version:	0.9.5
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://annodex.net/software/liboggz/download/%{name}-%{version}.tar.gz
# Source0-md5:	781fab29dea3c5e9d39ecbd1d007fb98
URL:		http://annodex.net/software/liboggz/index.html
BuildRequires:	docbook-to-man
BuildRequires:	libogg-devel >= 2:1.0
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

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/liboggz

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/oggz*
%attr(755,root,root) %{_libdir}/liboggz.so.*.*.*
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
