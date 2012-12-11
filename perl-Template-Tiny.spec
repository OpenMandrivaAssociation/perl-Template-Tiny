%define upstream_name    Template-Tiny
%define upstream_version 1.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Template Toolkit reimplemented in as little code as possible
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(Test::More)

BuildArch:	noarch

%description
*WARNING: THIS MODULE IS EXPERIMENTAL AND SUBJECT TO CHANGE WITHOUT NOTICE*

*YOU HAVE BEEN WARNED!*

*Template::Tiny* is a reimplementation of a partial subset of the the
Template manpage Toolkit, in as few lines of code as possible.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Fri Jun 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.120.0-1mdv2011.0
+ Revision: 687001
- update to new version 1.12

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.110.0-2
+ Revision: 654302
- rebuild for updated spec-helper

* Tue Feb 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 510235
- adding missing buildrequires:
- update to 0.11

* Sun Jan 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.1
+ Revision: 495433
- update to 0.10

* Thu Dec 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.1
+ Revision: 482097
- import perl-Template-Tiny


* Thu Dec 24 2009 cpan2dist 0.09-1mdv
- initial mdv release, generated with cpan2dist
