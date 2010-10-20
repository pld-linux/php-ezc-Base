%include	/usr/lib/rpm/macros.php
%define		status		stable
%define		pearname	Base
Summary:	%{pearname} - The Base package provides the basic infrastructure that all packages rely on
Name:		php-ezc-Base
Version:	1.8
Release:	1
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://components.ez.no/get/%{pearname}-%{version}.tgz
# Source0-md5:	f00eb71187ef9903bd1c2f7cdae3216a
URL:		http://components.ez.no/package/Base/
BuildRequires:	php-channel(components.ez.no)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-channel(components.ez.no)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Base package provides the basic infrastructure that all packages
rely on. Therefore every component relies on this package.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

install -d examples
mv docs/Base/docs/tutorial* examples
mv docs/Base/docs/repos examples

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# don't care for tests
rm -rf $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/Base/docs/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/ezc
%{php_pear_dir}/ezc/autoload/base_autoload.php
%{php_pear_dir}/ezc/Base
%{php_pear_dir}/data/Base
%{_examplesdir}/%{name}-%{version}
