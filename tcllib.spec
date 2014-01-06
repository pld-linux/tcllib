Summary:	Libraries for Tcl
Summary(pl.UTF-8):	Biblioteki dla Tcl-a
Name:		tcllib
Version:	1.15
Release:	2
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

# move manuals to proper namespaces, consistent with where they are exported,
# also avoiding conflicts with the same names in other namespaces
%{__mv} modules/base32/base32{,::}core.man
%{__mv} modules/base32/base32{,::}hex.man
%{__mv} modules/bench/bench{_read,::in}.man
%{__mv} modules/bench/bench{_wcsv,::out::csv}.man
%{__mv} modules/bench/bench{_wtext,::out::text}.man
%{__mv} modules/cache/{,cache::}async.man
%{__mv} modules/clock/{,clock::}iso8601.man
%{__mv} modules/clock/{,clock::}rfc2822.man
%{__mv} modules/coroutine/{coro_auto,coroutine::auto}.man
%{__mv} modules/crc/{,crc::}cksum.man
%{__mv} modules/crc/{,crc::}crc16.man
%{__mv} modules/crc/{,crc::}crc32.man
%{__mv} modules/crc/{,crc::}sum.man
%{__mv} modules/docstrip/docstrip{_,::}util.man
%{__mv} modules/doctools/{,doctools::}changelog.man
%{__mv} modules/doctools/{,doctools::}cvs.man
%{__mv} modules/doctools/{docidx,docutils::idx}.man
%{__mv} modules/doctools/{doctoc,docutils::toc}.man
%{__mv} modules/doctools2base/{html_,doctools::html::}cssdefaults.man
%{__mv} modules/doctools2base/{nroff_manmacros,doctools::nroff::man_macros}.man
%{__mv} modules/doctools2base/{tcl_parse,doctools::tcl::parse}.man
%{__mv} modules/doctools2base/{tcllib_msgcat,doctools::msgcat}.man
%{__mv} modules/doctools2idx/{,doctools2idx_}container.man
%{__mv} modules/doctools2idx/{,doctools::idx::}export.man
%{__mv} modules/doctools2idx/{export_,doctools::idx::export::}docidx.man
%{__mv} modules/doctools2idx/{export_,doctools::idx::export::}html.man
%{__mv} modules/doctools2idx/{export_,doctools::idx::export::}json.man
%{__mv} modules/doctools2idx/{export_,doctools::idx::export::}nroff.man
%{__mv} modules/doctools2idx/{export_,doctools::idx::export::}text.man
%{__mv} modules/doctools2idx/{export_,doctools::idx::export::}wiki.man
%{__mv} modules/doctools2idx/{,doctools::idx::}import.man
%{__mv} modules/doctools2idx/{import_,doctools::idx::import::}docidx.man
%{__mv} modules/doctools2idx/{import_,doctools::idx::import::}json.man
%{__mv} modules/doctools2idx/{,doctools2idx_}introduction.man
%{__mv} modules/doctools2idx/{msgcat_,doctools::msgcat::idx::}c.man
%{__mv} modules/doctools2idx/{msgcat_,doctools::msgcat::idx::}de.man
%{__mv} modules/doctools2idx/{msgcat_,doctools::msgcat::idx::}en.man
%{__mv} modules/doctools2idx/{msgcat_,doctools::msgcat::idx::}fr.man
%{__mv} modules/doctools2idx/{,doctools::idx::}parse.man
%{__mv} modules/doctools2idx/{,doctools::idx::}structure.man
%{__mv} modules/doctools2toc/{,doctools2toc_}container.man
%{__mv} modules/doctools2toc/{,doctools::toc::}export.man
%{__mv} modules/doctools2toc/{export_,doctools::toc::export::}doctoc.man
%{__mv} modules/doctools2toc/{export_,doctools::toc::export::}html.man
%{__mv} modules/doctools2toc/{export_,doctools::toc::export::}json.man
%{__mv} modules/doctools2toc/{export_,doctools::toc::export::}nroff.man
%{__mv} modules/doctools2toc/{export_,doctools::toc::export::}text.man
%{__mv} modules/doctools2toc/{export_,doctools::toc::export::}wiki.man
%{__mv} modules/doctools2toc/{,doctools::toc::}import.man
%{__mv} modules/doctools2toc/{import_,doctools::toc::import::}doctoc.man
%{__mv} modules/doctools2toc/{import_,doctools::toc::import::}json.man
%{__mv} modules/doctools2toc/{,doctools2toc_}introduction.man
%{__mv} modules/doctools2toc/{msgcat_,doctools::msgcat::toc::}c.man
%{__mv} modules/doctools2toc/{msgcat_,doctools::msgcat::toc::}de.man
%{__mv} modules/doctools2toc/{msgcat_,doctools::msgcat::toc::}en.man
%{__mv} modules/doctools2toc/{msgcat_,doctools::msgcat::toc::}fr.man
%{__mv} modules/doctools2toc/{,doctools::toc::}parse.man
%{__mv} modules/doctools2toc/{,doctools::toc::}structure.man
%{__mv} modules/fileutil/{,fileutil::}multi.man
%{__mv} modules/fileutil/{multiop,fileutil::multi::op}.man
%{__mv} modules/fileutil/{,fileutil::}traverse.man
%{__mv} modules/ftp/{ftp_,ftp::}geturl.man
%{__mv} modules/fumagic/{,fileutil::magic::}cfront.man
%{__mv} modules/fumagic/{,fileutil::magic::}cgen.man
%{__mv} modules/fumagic/{filetypes,fileutil::magic::filetype}.man
%{__mv} modules/fumagic/{mimetypes,fileutil::magic::mimetype}.man
%{__mv} modules/fumagic/{rtcore,fileutil::magic::rt}.man
%{__mv} modules/grammar_aycock/{,grammar::}aycock.man
%{__mv} modules/grammar_fa/{,grammar::fa::}dacceptor.man
%{__mv} modules/grammar_fa/{,grammar::fa::}dexec.man
%{__mv} modules/grammar_fa/{,grammar::}fa.man
%{__mv} modules/grammar_fa/{faop,grammar::fa::op}.man
%{__mv} modules/grammar_me/{,grammar::me::cpu::}gasm.man
%{__mv} modules/grammar_me/{,grammar::}me_ast.man
%{__mv} modules/grammar_me/{me_,grammar::me::}cpu.man
%{__mv} modules/grammar_me/{me_cpu,grammar::me::cpu::}core.man
%{__mv} modules/grammar_me/{,grammar::}me_intro.man
%{__mv} modules/grammar_me/{me_,grammar::me::}tcl.man
%{__mv} modules/grammar_me/{me_,grammar::me::}util.man
%{__mv} modules/grammar_me/{,grammar::}me_vm.man
%{__mv} modules/grammar_peg/{,grammar::}peg.man
%{__mv} modules/grammar_peg/{peg_,grammar::peg::}interp.man
%{__mv} modules/inifile/{ini,inifile}.man
%{__mv} modules/interp/{deleg_,interp::delegate::}method.man
%{__mv} modules/interp/{deleg_,interp::delegate::}proc.man
%{__mv} modules/json/{json_,json::}write.man
%{__mv} modules/log/{loggerAppender,logger::appender}.man
%{__mv} modules/log/{loggerUtils,logger::utils}.man
%{__mv} modules/map/{map_geocode_,map::geocode::}nominatim.man
%{__mv} modules/map/{map_,map::}slippy.man
%{__mv} modules/map/{map_slippy_,map::slippy::}cache.man
%{__mv} modules/map/{map_slippy_,map::slippy::}fetcher.man
%{__mv} modules/math/{,math::}bigfloat.man
%{__mv} modules/math/{,math::}bignum.man
%{__mv} modules/math/{,math::}calculus.man
%{__mv} modules/math/{,math::}constants.man
%{__mv} modules/math/{,math::}decimal.man
%{__mv} modules/math/{,math::}fourier.man
%{__mv} modules/math/{,math::}fuzzy.man
%{__mv} modules/math/{,math::}interpolate.man
%{__mv} modules/math/{linalg,math::linearalgebra}.man
%{__mv} modules/math/{,math::}machineparameters.man
%{__mv} modules/math/{,math::}optimize.man
%{__mv} modules/math/{,math::}polynomials.man
%{__mv} modules/math/{qcomplex,math::complexnumbers}.man
%{__mv} modules/math/{rational_funcs,math::rationalfunctions}.man
%{__mv} modules/math/{,math::}roman.man
%{__mv} modules/math/{,math::calculus::}romberg.man
%{__mv} modules/math/{,math::}special.man
%{__mv} modules/math/{,math::}statistics.man
%{__mv} modules/math/{,math::}combinatorics.man
%{__mv} modules/math/{math_,math::}geometry.man
%{__mv} modules/math/{,math::}numtheory.man
%{__mv} modules/math/{,math::calculus::}symdiff.man
%{__mv} modules/nns/{nns_,nameserv::}auto.man
%{__mv} modules/nns/{nns_,nameserv::}common.man
%{__mv} modules/nns/{nns_,nameserv::}protocol.man
%{__mv} modules/nns/{nns_,nameserv::}server.man
%{__mv} modules/page/{page_,page::}pluginmgr.man
%{__mv} modules/page/{page_util_,page::util::}flow.man
%{__mv} modules/page/{page_util_norm_,page::util::norm::}lemon.man
%{__mv} modules/page/{page_util_norm_,page::util::norm::}peg.man
%{__mv} modules/page/{page_util_,page::util::}peg.man
%{__mv} modules/page/{page_util_,page::util::}quote.man
%{__mv} modules/pop3d/{pop3d_,pop3d::}dbox.man
%{__mv} modules/pop3d/{pop3d_,pop3d::}udb.man
%{__mv} modules/pt/{pt_astree,pt::ast}.man
%{__mv} modules/pt/{pt_cparam_config_critcl,pt::cparam::configuration::critcl}.man
%{__mv} modules/pt/{pt_,pt::}param.man
%{__mv} modules/pt/{pt_peg_,pt::peg::}container.man
%{__mv} modules/pt/{pt_peg_container_,pt::peg::container::}peg.man
%{__mv} modules/pt/{pt_peg_,pt::peg::}export.man
%{__mv} modules/pt/{pt_peg_export_,pt::peg::export::}container.man
%{__mv} modules/pt/{pt_peg_export_,pt::peg::export::}json.man
%{__mv} modules/pt/{pt_peg_export_,pt::peg::export::}peg.man
%{__mv} modules/pt/{pt_peg_from_,pt::peg::from::}json.man
%{__mv} modules/pt/{pt_peg_from_,pt::peg::from::}peg.man
%{__mv} modules/pt/{pt_peg_,pt::peg::}import.man
%{__mv} modules/pt/{pt_peg_import_,pt::peg::import::}json.man
%{__mv} modules/pt/{pt_peg_import_,pt::peg::import::}peg.man
%{__mv} modules/pt/{pt_peg_,pt::peg::}interp.man
%{__mv} modules/pt/{pt_peg_to_,pt::peg::to::}container.man
%{__mv} modules/pt/{pt_peg_to_,pt::peg::to::}cparam.man
%{__mv} modules/pt/{pt_peg_to_,pt::peg::to::}json.man
%{__mv} modules/pt/{pt_peg_to_,pt::peg::to::}param.man
%{__mv} modules/pt/{pt_peg_to_,pt::peg::to::}peg.man
%{__mv} modules/pt/{pt_peg_to_,pt::peg::to::}tclparam.man
%{__mv} modules/pt/{pt_pegrammar,pt::peg}.man
%{__mv} modules/pt/{pt_pexpr_op,pt::pe::op}.man
%{__mv} modules/pt/{pt_pexpression,pt::pe}.man
%{__mv} modules/pt/{pt_,pt::}pgen.man
%{__mv} modules/pt/{pt_rdengine,pt::rde}.man
%{__mv} modules/pt/{pt_tclparam_config_,pt::tclparam::configuration::}snit.man
%{__mv} modules/pt/{pt_tclparam_config_,pt::tclparam::configuration::}tcloo.man
%{__mv} modules/ripemd/{,ripemd::}ripemd128.man
%{__mv} modules/ripemd/{,ripemd::}ripemd160.man
%{__mv} modules/simulation/{,simulation::}annealing.man
%{__mv} modules/simulation/{,simulation::}montecarlo.man
%{__mv} modules/simulation/{simulation_,simulation::}random.man
%{__mv} modules/stringprep/{stringprep_,stringprep::}data.man
%{__mv} modules/stringprep/{unicode_,unicode::}data.man
%{__mv} modules/struct/{,struct::}disjointset.man
%{__mv} modules/struct/{,struct::}graph.man
%{__mv} modules/struct/{graph1,struct::graph_v1}.man
%{__mv} modules/struct/{graphops,struct::graph::op}.man
%{__mv} modules/struct/{,struct::}matrix.man
%{__mv} modules/struct/{matrix1,struct::matrix_v1}.man
%{__mv} modules/struct/{,struct::}pool.man
%{__mv} modules/struct/{,struct::}prioqueue.man
%{__mv} modules/struct/{,struct::}queue.man
%{__mv} modules/struct/{,struct::}record.man
%{__mv} modules/struct/{,struct::}skiplist.man
%{__mv} modules/struct/{,struct::}stack.man
%{__mv} modules/struct/{struct_,struct::}list.man
%{__mv} modules/struct/{struct_,struct::}set.man
%{__mv} modules/struct/{struct_,struct::}tree.man
%{__mv} modules/struct/{struct_tree1,struct::tree_v1}.man
%{__mv} modules/term/{ansi_cattr,term::ansi::code:attr}.man
%{__mv} modules/term/{ansi_cctrl,term::ansi::code:ctrl}.man
%{__mv} modules/term/{ansi_cmacros,term::ansi::code:macros}.man
%{__mv} modules/term/{ansi_,term::ansi::}code.man
%{__mv} modules/term/{ansi_ctrlu,term::ansi::ctrl::unix}.man
%{__mv} modules/term/{ansi_,term::ansi::}send.man
%{__mv} modules/term/{imenu,term::interact::menu}.man
%{__mv} modules/term/{ipager,term::interact::pager}.man
%{__mv} modules/term/{,term::}receive.man
%{__mv} modules/term/{term_,term::receive::}bind.man
%{__mv} modules/term/{term_,term::}send.man
%{__mv} modules/textutil/{,textutil::}adjust.man
%{__mv} modules/textutil/{,textutil::}expander.man
%{__mv} modules/textutil/{,textutil::}repeat.man
%{__mv} modules/textutil/{,textutil::}tabify.man
%{__mv} modules/textutil/{textutil_,textutil::}split.man
%{__mv} modules/textutil/{textutil_,textutil::}string.man
%{__mv} modules/textutil/{,textutil::}trim.man
%{__mv} modules/tie/{tie_,tie::}std.man
%{__mv} modules/transfer/{,transfer::}connect.man
%{__mv} modules/transfer/{copyops,transfer::copy}.man
%{__mv} modules/transfer/{ddest,transfer::data::destination}.man
%{__mv} modules/transfer/{dsource,transfer::data::source}.man
%{__mv} modules/transfer/{,transfer::}receiver.man
%{__mv} modules/transfer/{tqueue,transfer::copy::queue}.man
%{__mv} modules/transfer/{,transfer::}transmitter.man
%{__mv} modules/uev/{uevent_,uevent::}onidle.man
%{__mv} modules/uri/{urn-scheme,uri::urn}.man
%{__mv} modules/valtype/{cc_,valtype::creditcard::}amex.man
%{__mv} modules/valtype/{cc_,valtype::creditcard::}discover.man
%{__mv} modules/valtype/{cc_,valtype::creditcard::}mastercard.man
%{__mv} modules/valtype/{cc_,valtype::creditcard::}visa.man
%{__mv} modules/valtype/{,valtype::gs1::}ean13.man
%{__mv} modules/valtype/{,valtype::}iban.man
%{__mv} modules/valtype/{,valtype::}imei.man
%{__mv} modules/valtype/{,valtype::}isbn.man
%{__mv} modules/valtype/{,valtype::}luhn.man
%{__mv} modules/valtype/{,valtype::}luhn5.man
%{__mv} modules/valtype/{,valtype::}usnpi.man
%{__mv} modules/valtype/{valtype_,valtype::}common.man
%{__mv} modules/valtype/{,valtype::}verhoeff.man
%{__mv} modules/virtchannel_base/{,tcl::chan::}cat.man
%{__mv} modules/virtchannel_base/{,tcl::chan::}facade.man
%{__mv} modules/virtchannel_base/{,tcl::chan::}fifo.man
%{__mv} modules/virtchannel_base/{,tcl::chan::}fifo2.man
%{__mv} modules/virtchannel_base/{,tcl::chan::}halfpipe.man
%{__mv} modules/virtchannel_base/{,tcl::chan::}memchan.man
%{__mv} modules/virtchannel_base/{,tcl::chan::}null.man
%{__mv} modules/virtchannel_base/{,tcl::chan::}nullzero.man
%{__mv} modules/virtchannel_base/{,tcl::chan::}random.man
%{__mv} modules/virtchannel_base/{,tcl::chan::}randseed.man
%{__mv} modules/virtchannel_base/{,tcl::chan::}std.man
%{__mv} modules/virtchannel_base/{,tcl::chan::}string.man
%{__mv} modules/virtchannel_base/{,tcl::chan::}textwindow.man
%{__mv} modules/virtchannel_base/{,tcl::chan::}variable.man
%{__mv} modules/virtchannel_base/{,tcl::chan::}zero.man
%{__mv} modules/virtchannel_core/{,tcl::chan::}core.man
%{__mv} modules/virtchannel_core/{,tcl::chan::}events.man
%{__mv} modules/virtchannel_core/{transformcore,tcl::transform::core}.man
%{__mv} modules/virtchannel_transform/{,tcl::transform::}adler32.man
%{__mv} modules/virtchannel_transform/{,tcl::transform::}base64.man
%{__mv} modules/virtchannel_transform/{,tcl::transform::}counter.man
%{__mv} modules/virtchannel_transform/{,tcl::transform::}crc32.man
%{__mv} modules/virtchannel_transform/{,tcl::transform::}hex.man
%{__mv} modules/virtchannel_transform/{,tcl::transform::}identity.man
%{__mv} modules/virtchannel_transform/{,tcl::transform::}limitsize.man
%{__mv} modules/virtchannel_transform/{,tcl::transform::}observe.man
%{__mv} modules/virtchannel_transform/{,tcl::transform::}otp.man
%{__mv} modules/virtchannel_transform/{,tcl::transform::}rot.man
%{__mv} modules/virtchannel_transform/{,tcl::transform::}spacer.man
%{__mv} modules/virtchannel_transform/{,tcl::transform::}zlib.man

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
