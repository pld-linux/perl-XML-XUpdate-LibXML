#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	XUpdate-LibXML
Summary:	XML::XUpdate::LibXML - simple implementation of XUpdate format
Summary(pl):	XML::XUpdate::LibXML - prosta implementacja formatu XUpdate
Name:		perl-XML-XUpdate-LibXML
Version:	0.5.0
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	403f424f162f71f41d41e3eaedefcf4e
%if %{with tests}
BuildRequires:	perl-XML-LibXML >= 1.54
BuildRequires:	perl-XML-LibXML-Iterator
BuildRequires:	perl-XML-LibXML-XPathContext >= 0.04
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-XML-LibXML >= 1.54
Requires:	perl-XML-LibXML-XPathContext >= 0.04
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements the XUpdate format described in XUpdate Working
Draft from 2000-09-14 (http://www.xmldb.org/xupdate/xupdate-wd.html).
The implementation is based on XML::LibXML DOM API.

%description -l pl
Ten modu³ implementuje format XUpdate opisany w XUpdate Working Draft
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
