Name:           python-rencode
Version:        1.0.6
Release:        1%{?dist}
Summary:        Web safe object pickling/unpickling
License:        GPLv3+ and BSD
URL:            https://github.com/aresch/rencode

Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
      
BuildRequires:  gcc
BuildRequires:  python2-devel python3-devel
BuildRequires:  python2-Cython python3-Cython


%description
The rencode module is a modified version of bencode from the
BitTorrent project.  For complex, heterogeneous data structures with
many small elements, r-encodings take up significantly less space than
b-encodings.


%package -n python2-rencode
Summary:    Web safe object pickling/unpickling
%{?python_provide:%python_provide python2-rencode}


%description -n python2-rencode
The rencode module is a modified version of bencode from the
BitTorrent project.  For complex, heterogeneous data structures with
many small elements, r-encodings take up significantly less space than
b-encodings.


%package -n python%{python3_pkgversion}-rencode
Summary:    Web safe object pickling/unpickling
%{?python_provide:%python_provide python%{python3_pkgversion}-rencode}


%description -n python%{python3_pkgversion}-rencode
The rencode module is a modified version of bencode from the
BitTorrent project.  For complex, heterogeneous data structures with
many small elements, r-encodings take up significantly less space than
b-encodings.


%prep
%autosetup -n rencode-%{version}


%build
%py2_build
%py3_build


%install
%py2_install
%py3_install


%check
pushd tests
PYTHONPATH=$RPM_BUILD_ROOT%{python2_sitearch} %{__python2} test_rencode.py
PYTHONPATH=$RPM_BUILD_ROOT%{python2_sitearch} %{__python2} timetest.py
PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitearch} %{__python3} test_rencode.py
PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitearch} %{__python3} timetest.py
popd


%files -n python2-rencode
%{python2_sitearch}/rencode
%{python2_sitearch}/rencode*.egg-info
%doc README.md
%license COPYING


%files -n python%{python3_pkgversion}-rencode
%{python3_sitearch}/rencode
%{python3_sitearch}/rencode*.egg-info
%doc README.md
%license COPYING


%changelog
* Sun Nov  4 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.6-1
- Update to version 1.0.6
- Switch URL to point to PyPi
- Cleanup old macros in spec file

* Sun Jul 22 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.5-12
- Fix usage of macros for file list

* Sun Jul 22 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.5-11
- Fix running of tests (BZ #1605871)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-4
- Rebuild for Python 3.6

* Tue Nov 8 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.5-3
- Enable builds on EPEL7

* Sat Oct  1 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.5-2
- Revert to using github tarballs as PyPi tarballs omit tests

* Sat Oct  1 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.5-1
- Update to 1.0.5
- Update source URL

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-1
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Feb 27 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.4-0
- Update to 1.0.4
- Split out python2-rencode subpackage, and leave main package empty
- Add use of python_provide macros according to guidelines
- Clean up spec file, remove redundant code
- Use python build and install macros
- Build and test both python2 and python3 packages in same directory

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 14 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.3-1
- Update to version 1.0.3
- Update upstream location (now on github)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6.20121209svn33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5.20121209svn33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.0.2-4.20121209svn33
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3.20121209svn33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 06 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.2-2.20121209svn33
- use macros consistently
- fix permissions on shared objects
- drop useless setuptools copypasta
- fix License tag

* Thu Apr 18 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.2-1.20121209svn33
- initial package
