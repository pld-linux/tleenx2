%define		snap 20021118
Summary:	Tlen.pl client for gtk+2
Summary(pl):	Klient Tlen.pl dla gtk+2
Name:		tleenx2
Version:	0
Release:	0.%{snap}
License:	GPL
Group:		Applications/Communications
#ftp://ftp.sourceforge.net/pub/sourceforge/tleenx/TleenX2-%{snap}.tar.gz
Source0:	%{name}-%{snap}.tar.bz2
URL:		http://tleenx.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libtlen 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
TleenX is a Tlen.pl client written for Linux users. It is distributed
under GPL license.

%description -l pl
TleenX to klient tlen.pl napisany z my¶l± o u¿ytkownikach Linuksa.
Jest rozpowszechniany na licencji GPL.

%prep
%setup -q -n %{name}-%{snap}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
