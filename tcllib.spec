Summary:	Libraries for TCL
Summary(pl):	Biblioteki dla Tcl-a
Name:		tcllib
Version:	1.4
Release:	1
License:	see license.terms
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tcllib/%{name}-%{version}.tar.gz
# Source0-md5:	9a612118c2ccd5afabc8a42b8f3d068a
Icon:		tcl.gif
URL:		http://tcllib.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tcl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is intended to be a collection of Tcl packages that
provide utility functions useful to a large collection of Tcl
programmers.

%description -l pl
Pakiet jest zestawem pakietów Tcl udostępniającym różne funkcje
użyteczne dla wielu programistów Tcl-a.

%prep
%setup  -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix},%{_mandir}/man1}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README license.terms examples
%{_libdir}/%{name}%{version}
%{_mandir}/man?/*
