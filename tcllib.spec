Summary:	Libraries for TCL
Summary(pl):	Biblioteki dla Tcl-a
Name:		tcllib
Version:	1.3
Release:	1
License:	see license.terms
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tcllib/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Icon:		tcl.gif
URL:		http://tcllib.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is intended to be a collection of Tcl packages that
provide utility functions useful to a large collection of Tcl
programmers.

%description -l pl
Pakiet jest zestawem pakietów Tcl udostêpniaj±cym ró¿ne funkcje
u¿yteczne dla wielu programistów Tcl-a.

%prep
%setup  -q
%patch0 -p0

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
