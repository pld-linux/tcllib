Summary:	Libraries for Tcl
Summary(pl.UTF-8):	Biblioteki dla Tcl-a
Name:		tcllib
Version:	1.9
Release:	2
License:	see license.terms
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tcllib/%{name}-%{version}.tar.gz
# Source0-md5:	17d9ae35b1c6fde1d79c5b1423416cd2
URL:		http://tcllib.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tcl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is intended to be a collection of Tcl packages that
provide utility functions useful to a large collection of Tcl
programmers.

%description -l pl.UTF-8
Pakiet jest zestawem pakietów Tcl udostępniającym różne funkcje
użyteczne dla wielu programistów Tcl-a.

%prep
%setup  -q

%build
%{__aclocal}
%{__autoconf}
%configure \
	--libdir=%{_prefix}/lib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README license.terms examples
%attr(755,root,root) %{_bindir}/*
%{_prefix}/lib/%{name}%{version}
%{_mandir}/man?/*
