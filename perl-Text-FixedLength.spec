#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	FixedLength
Summary:	Text::FixedLength - parse and create fixed length field records
Summary(pl.UTF-8):   Text::FixedLength - analiza i tworzenie rekordów o polach stałej długości
Name:		perl-Text-FixedLength
Version:	0.12
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0d567248f2152260bbf0035dace35d31
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::FixedLength was made to be able to manipulate fixed length field
records. You can manipulate arrays of data, or files of data. This
module allows you to change between delimited and fixed length
records.

%description -l pl.UTF-8
Text::FixedLength został stworzony, by umożliwić manipulowanie
rekordami o polach stałej długości. Można obrabiać tablice lub pliki z
danymi. Ten moduł umożliwia konwersję pomiędzy rekordami z polami
ograniczonymi i polami stałej długości.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Text/FixedLength.pm
%{_mandir}/man3/*
