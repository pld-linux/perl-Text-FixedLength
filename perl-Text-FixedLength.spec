%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	FixedLength
Summary:	Text::FixedLength - Parse and create fixed length field records
Summary(pl):	Text::FixedLength - analiza i tworzenie rekord�w o polach sta�ej d�ugo�ci
Name:		perl-Text-FixedLength
Version:	0.12
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0d567248f2152260bbf0035dace35d31
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::FixedLength was made to be able to manipulate fixed length field
records. You can manipulate arrays of data, or files of data. This
module allows you to change between delimited and fixed length
records.

%description -l pl
Text::FixedLength zosta� stworzony, by umo�liwi� manipulowanie
rekordami o polach sta�ej d�ugo�ci. Mo�na obrabia� tablice lub pliki z
danymi. Ten modu� umo�liwia konwersj� pomi�dzy rekordami z polami
ograniczonymi i polami sta�ej d�ugo�ci.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Text/FixedLength.pm
%{_mandir}/man3/*
