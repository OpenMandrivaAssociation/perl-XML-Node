%define module 	XML-Node
%define version 0.11
%define release %mkrel 7

Summary: Node-based XML parsing: an simplified interface to XML::Parser
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildArch:	noarch

%description
Using XML::Node, you can easily ignore the parts of XML files that you
are not interested in, thus helping in simplify Perl scripts
significantly.

%prep
%setup -q  -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix} 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} PREFIX=$RPM_BUILD_ROOT%{_prefix} install

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README MANIFEST Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML/*

