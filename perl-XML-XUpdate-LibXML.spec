#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	XML
%define		pnam	XUpdate-LibXML
Summary:	XML::XUpdate::LibXML - simple implementation of XUpdate format
Summary(pl.UTF-8):	XML::XUpdate::LibXML - prosta implementacja formatu XUpdate
Name:		perl-XML-XUpdate-LibXML
Version:	0.6.0
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	feee3db4ab0a0520d9b1f17b50f74693
URL:		http://search.cpan.org/dist/XML-XUpdate-LibXML/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-LibXML >= 1.54
BuildRequires:	perl-XML-LibXML-Iterator
BuildRequires:	perl-XML-LibXML-XPathContext >= 0.04
%endif
Requires:	perl-XML-LibXML >= 1.54
Requires:	perl-XML-LibXML-XPathContext >= 0.04
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements the XUpdate format described in XUpdate Working
Draft from 2000-09-14 (http://www.xmldb.org/xupdate/xupdate-wd.html).
The implementation is based on XML::LibXML DOM API.

%description -l pl.UTF-8
Ten moduł implementuje format XUpdate opisany w XUpdate Working Draft
z 14.09.2000 (http://www.xmldb.org/xupdate/xupdate-wd.html).
Implementacja jest oparta na API DOM z XML::LibXML.

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
%doc Changes
%attr(755,root,root) %{_bindir}/xupdate
%{perl_vendorlib}/XML/Normalize
%{perl_vendorlib}/XML/XUpdate
%{_mandir}/man[13]/*
