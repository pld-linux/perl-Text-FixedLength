%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	FixedLength
Summary:	Text::FixedLength - Parse and create fixed length field records
Summary(pl):	Text::FixedLength - analiza i tworzenie rekordów o polach sta³ej d³ugo¶ci
Name:		perl-Text-FixedLength
Version:	0.12
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::FixedLength was made to be able to manipulate fixed length field
records. You can manipulate arrays of data, or files of data. This
module allows you to change between delimited and fixed length
records.

%description -l pl
Text::FixedLength zosta³ stworzony, by umo¿liwiæ manipulowanie
rekordami o polach sta³ej d³ugo¶ci. Mo¿na obrabiaæ tablice lub pliki z
danymi. Ten modu³ umo¿liwia konwersjê pomiêdzy rekordami z polami
ograniczonymi i polami sta³ej d³ugo¶ci.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Text/FixedLength.pm
%{_mandir}/man3/*
