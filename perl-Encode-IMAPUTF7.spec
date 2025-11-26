%define module Encode-IMAPUTF7
%undefine _debugsource_packages

Name:		perl-%{module}
Version:	1.07
Release:	1
Summary:	Perl module for handling IMAP UTF-7 encoding
URL:		https://metacpan.org/pod/Encode::IMAPUTF7
Source:		https://cpan.org/modules/by-module/Encode/%{module}-%{version}.tar.gz
License:	Perl (Artistic or GPL)
Group:		Development/Perl
BuildRequires:	perl
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Perl module for handling IMAP UTF-7 encoding

%prep
%autosetup -p1 -n %{module}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install INSTALLDIRS=vendor

%files
%doc Changes MANIFEST README
%{perl_vendorlib}/*/*
%{_mandir}/man3/*.3pm*
