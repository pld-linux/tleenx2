
%define		snap 20040214

Summary:	Tlen.pl client for gtk+2
Summary(pl):	Klient Tlen.pl dla gtk+2
Name:		tleenx2
Version:	0
Release:	0.%{snap}
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/tleenx/TleenX2-%{snap}.tar.gz
# Source0-md5:	a9da1fdeb7d93ffe9a63b31aed4359ac
Source1:	http://tleenx.sourceforge.net/download/sounds/default.tar.gz
# Source1-md5:	964761f483c1a0a1421ca6ebc0a5ed22
Source2:	%{name}.desktop
Patch0:		%{name}-maninst.patch
Patch1:		%{name}-shared.patch
URL:		http://tleenx.sourceforge.net/
BuildRequires:	XFree86-libs >= 4.3.99.15
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libtlen-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TleenX is a Tlen.pl client written for Linux users. It is distributed
under GPL license.

%description -l pl
TleenX to klient tlen.pl napisany z my�l� o u�ytkownikach Linuksa.
Jest rozpowszechniany na licencji GPL.

%prep
%setup -q -n TleenX2-%{snap} -a1
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ \
	$RPM_BUILD_ROOT%{_datadir}/applnk/Network/Communications/
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applnk/Network/Communications/%{name}.desktop
install default/* $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applnk/Network/Communications/%{name}.desktop
%{_mandir}/man?/*
