%define upstream_name    Template-Tiny
%define upstream_version 1.16
Name:		perl-%{upstream_name}
Version:	1.16
Release:	2

Summary:	Template Toolkit reimplemented in as little code as possible
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/karenetheridge/Template-Tiny
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/Template-Tiny-1.16.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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

