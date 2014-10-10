%define upstream_name 	 XML-Node
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Node-based XML parsing: an simplified interface to XML::Parser
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildArch:	noarch

%description
Using XML::Node, you can easily ignore the parts of XML files that you
are not interested in, thus helping in simplify Perl scripts
significantly.

%prep
%setup -q  -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix} 
make

%install
make PREFIX=%{buildroot}%{_prefix} install

%files
%doc README MANIFEST Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML/*

%changelog
* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.0
+ Revision: 401857
- rebuild using %%perl_convert_version

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.11-10mdv2009.0
+ Revision: 258844
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.11-9mdv2009.0
+ Revision: 246764
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.11-7mdv2008.1
+ Revision: 136367
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.11-7mdv2008.0
+ Revision: 23512
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.11-6mdk
- Fix According to perl Policy
	- BuildRequires
	- Source URL
	- URL
- use mkrel

* Wed Jun 30 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.11-5mdk
- rebuild

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.11-4mdk
- rebuild for new auto{prov,req}

