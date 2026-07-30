%define upstream_name 	 XML-Node
%define upstream_version 0.11
Name:		perl-%{upstream_name}
Version:	0.11
Release:	2

Summary:	Node-based XML parsing: an simplified interface to XML::Parser
License:	Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/XML-Node
Source0:	https://cpan.metacpan.org/authors/id/C/CH/CHANG-LIU/XML-Node-0.11.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildArch:	noarch

%description
Using XML::Node, you can easily ignore the parts of XML files that you
are not interested in, thus helping in simplify Perl scripts
significantly.

%prep
%setup -q  -n XML-Node-0.11

%build
perl Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix} 
make

%install
make PREFIX=%{buildroot}%{_prefix} install

%files
%doc README MANIFEST Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML/*

