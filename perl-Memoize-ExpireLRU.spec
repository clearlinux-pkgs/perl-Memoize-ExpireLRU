#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Memoize-ExpireLRU
Version  : 0.56
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Memoize-ExpireLRU-0.56.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Memoize-ExpireLRU-0.56.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmemoize-expirelru-perl/libmemoize-expirelru-perl_0.56-1.debian.tar.xz
Summary  : 'Expiry plug-in for Memoize that adds LRU cache expiration'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Memoize-ExpireLRU-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Memoize::ExpireLRU is a module that implements LRU expiration for
Memoize.
You can read a nicely formatted version of the documentation for
this module online:

%package dev
Summary: dev components for the perl-Memoize-ExpireLRU package.
Group: Development
Provides: perl-Memoize-ExpireLRU-devel = %{version}-%{release}

%description dev
dev components for the perl-Memoize-ExpireLRU package.


%package license
Summary: license components for the perl-Memoize-ExpireLRU package.
Group: Default

%description license
license components for the perl-Memoize-ExpireLRU package.


%prep
%setup -q -n Memoize-ExpireLRU-0.56
cd ..
%setup -q -T -D -n Memoize-ExpireLRU-0.56 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Memoize-ExpireLRU-0.56/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Memoize-ExpireLRU
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Memoize-ExpireLRU/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Memoize/ExpireLRU.pm
/usr/lib/perl5/vendor_perl/5.28.1/auto/Memoize/ExpireLRU/DumpCache.al
/usr/lib/perl5/vendor_perl/5.28.1/auto/Memoize/ExpireLRU/ShowStats.al
/usr/lib/perl5/vendor_perl/5.28.1/auto/Memoize/ExpireLRU/autosplit.ix

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Memoize::ExpireLRU.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Memoize-ExpireLRU/LICENSE
