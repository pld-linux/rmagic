%include	/usr/lib/rpm/macros.perl
Summary:	Add-on formatting utility for Analog
Summary(pl.UTF-8):   Dodatek formatujący dla Analoga
Name:		rmagic
Version:	2.21
Release:	1
License:	Artistic
Group:		Networking/Utilities
Source0:	http://www.reportmagic.org/%{name}-%{version}.tar.gz
# Source0-md5:	23b109da43e34d2ee3b8390c20daa98a
URL:		http://www.reportmagic.org/
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Report Magic for Analog is an add-on formatting utility for Analog web
site statistics software. Report Magic uses the statistics generated
by Analog and formatting options set by you to make readable,
presentable reports of your Web site data.

%description -l pl.UTF-8
Report Magic dla Analoga to dodatek formatujący dla programu Analog
służącego do statystyk serwisów WWW. Report Magic używa statystyk
wygenerowanych przez Analoga oraz ustawionych opcji do stworzenia
czytelnych, nadających się do prezentacji raportów z danych serwisu
WWW.

%prep
%setup -q

%build
%{__perl} Install.PL \
	-no_modules \
	-only_modules

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%{__perl} Install.PL \
	-no_modules \
	$RPM_BUILD_ROOT%{_datadir}/%{name}

mv $RPM_BUILD_ROOT%{_datadir}/%{name}docs/* $RPM_BUILD_ROOT%{_datadir}/%{name}/*sample* \
	$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

ln -s %{_datadir}/%{name}/rmagic.pl $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/lang
%attr(755,root,root) %{_datadir}/%{name}/wadg
%attr(755,root,root) %{_datadir}/%{name}/*.pl
%{_datadir}/%{name}/*.png
