%define	pdir	Text
%define	pnam	FixedLength
%include	/usr/lib/rpm/macros.perl
Summary:	Text-FixedLength perl module
Summary(pl):	Modu� perla Text-FixedLength
Name:		perl-Text-FixedLength
Version:	0.12
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-FixedLength perl module.

%description -l pl
Modu� perla Text-FixedLength.

%prep
%setup -q -n Text-FixedLength-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Text/FixedLength.pm
%{_mandir}/man3/*
