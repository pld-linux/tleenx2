
%define		snap 20060309

Summary:	Tlen.pl client for GTK+2
Summary(pl.UTF-8):	Klient Tlen.pl dla GTK+2
Name:		tleenx2
Version:	0
Release:	0.%{snap}.1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/tleenx/TleenX2-%{snap}.tar.gz
# Source0-md5:	b9d379f5d116c69a2fbcb74069533bc3
Source1:	http://tleenx.sourceforge.net/download/sounds/default.tar.gz
# Source1-md5:	964761f483c1a0a1421ca6ebc0a5ed22
Source2:	%{name}.desktop
Patch0:		%{name}-check-for-body.diff
URL:		http://tleenx.sourceforge.net/
BuildRequires:	XFree86-libs >= 4.3.99.15
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libtlen-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TleenX is a Tlen.pl client written for Linux users. It is distributed
under GPL license.

%description -l pl.UTF-8
TleenX to klient tlen.pl napisany z myślą o użytkownikach Linuksa.
Jest rozpowszechniany na licencji GPL.

%prep
%setup -q -n TleenX2-%{snap} -a1
%patch0 -p0

%build
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

install -d $RPM_BUILD_ROOT{%{_datadir}/%{name}/sounds,%{_desktopdir}}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install default/* $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_mandir}/man?/*
%{_pixmapsdir}/%{name}.png
