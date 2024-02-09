%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global srcname iso8601
%global sum Simple module to parse ISO 8601 dates
%global pkgdesc \
This module parses the most common forms of ISO 8601 date strings \
(e.g. 2007-01-14T20:34:22+00:00) into datetime objects.

%bcond_without  tests

Name:           python-%{srcname}
Version:        0.1.11
Release:        12%{?dist}
Summary:        %{sum}

License:        MIT
URL:            http://pypi.python.org/pypi/%{srcname}/
Source0:        http://pypi.python.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-srpm-macros
BuildRequires:  python3-pytest

%description %{pkgdesc}

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}
# python_provide does not exist in CBS Cloud buildroot
Provides:       python-%{srcname} = %{version}-%{release}
Obsoletes:      python-%{srcname} < 0.1.10-6

BuildRequires:  python2-devel python2-setuptools

%description -n python2-%{srcname} %{pkgdesc}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{srcname} %{pkgdesc}

%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{srcname}}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools

%description -n python%{python3_other_pkgversion}-%{srcname} %{pkgdesc}
%endif

%prep
%autosetup -n %{srcname}-%{version}

%build
export RHEL_ALLOW_PYTHON2_FOR_BUILD=1
%py2_build
%py3_build
%if 0%{?with_python3_other}
%py3_other_build
%endif

%install
export RHEL_ALLOW_PYTHON2_FOR_BUILD=1
%py2_install
%py3_install
%if 0%{?with_python3_other}
%py3_other_install
%endif

%if %{with tests}
%check
%pytest
%endif

%files -n python2-%{srcname}
%doc LICENSE README.rst
%{python2_sitelib}/*

%files -n python%{python3_pkgversion}-%{srcname}
%doc LICENSE README.rst
%{python3_sitelib}/*

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{srcname}
%doc LICENSE README.rst
%{python3_other_sitelib}/*
%endif

%changelog
* Fri Aug 19 2022 Tomas Orsava <torsava@redhat.com> - 0.1.11-12
- Modify test for RHEL 8
- Related: rhbz#2108089

* Thu Aug 18 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 0.1.11-11
- Enable tests
- Related: rhbz#2108089

* Wed Aug 10 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 0.1.11-10
- Fix BuildRequire in spec file
- Resolves: rhbz#2108089

* Mon Jun 25 2018 Petr Viktorin <pviktori@redhat.com> - 0.1.11-9
- Allow Python 2 for build
  see https://hurl.corp.redhat.com/rhel8-py2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 16 2017 Aurelien Bompard <abompard@fedoraproject.org> - 0.1.11-7
- Build for Python3 on EPEL:
  http://fedoraproject.org/wiki/PackagingDrafts:Python3EPEL
- Modernize the spec a bit (build and install macros, no explicit buildroot)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Stratakis Charalampos <cstratak@redhat.com> - 0.1.11-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1.11-1
- Upstream 0.1.11

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Nov 04 2015 Robert Kuska <rkuska@redhat.com> - 0.1.10-7
- Rebuilt for Python3.5 rebuild

* Mon Sep 07 2015 Chandan Kumar <chkumar246@gmail.com> - 0.1.10-6
- Added python2 along with python3 subpackage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Apr 23 2014 Pádraig Brady <pbrady@redhat.com> - 0.1.10-2
- Add python3 package

* Thu Mar 27 2014 Pádraig Brady <pbrady@redhat.com> - 0.1.10-1
- Latest upstream

* Tue Nov 12 2013 Pádraig Brady <pbrady@redhat.com> - 0.1.8-1
- Latest upstream

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul  9 2010 Ian Weller <iweller@redhat.com> - 0.1.4-2
- Correct python_sitelib macro

* Mon Jun 28 2010 Ian Weller <iweller@redhat.com> - 0.1.4-1
- Initial package build
