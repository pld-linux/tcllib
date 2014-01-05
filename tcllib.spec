Summary:	Libraries for Tcl
Summary(pl.UTF-8):	Biblioteki dla Tcl-a
Name:		tcllib
Version:	1.15
Release:	1
License:	BSD-like (see license.terms)
Group:		Development/Languages/Tcl
Source0:	http://downloads.sourceforge.net/tcllib/%{name}-%{version}.tar.gz
# Source0-md5:	7a0525912e8863f8d4360ab10e5450f8
Patch0:		%{name}-man.patch
URL:		http://tcllib.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tcl >= 8.2
Requires:	tcl >= 8.2
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
%setup -q
%patch0 -p1

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

%{__mv} $RPM_BUILD_ROOT%{_mandir}/mann/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README license.terms examples
%attr(755,root,root) %{_bindir}/dtplite
%attr(755,root,root) %{_bindir}/nns
%attr(755,root,root) %{_bindir}/nnsd
%attr(755,root,root) %{_bindir}/nnslog
%attr(755,root,root) %{_bindir}/page
%attr(755,root,root) %{_bindir}/tcldocstrip
%{_prefix}/lib/%{name}%{version}
%{_mandir}/man1/dtplite.1*
%{_mandir}/man1/nns.1*
%{_mandir}/man1/nnsd.1*
%{_mandir}/man1/nnslog.1*
%{_mandir}/man1/page.1*
%{_mandir}/man1/tcldocstrip.1*
%{_mandir}/mann/*.n*
