# Remove private provides from .so files in the python_sitearch directory
%global __provides_exclude_from ^%{python_sitearch}/.*\\.so$

Name:           python-rencode
Version:        1.0.3
Release:        4%{?dist}
Summary:        Web safe object pickling/unpickling
License:        GPLv3+ and BSD
URL:            https://github.com/aresch/rencode

Source0:        https://github.com/aresch/rencode/archive/v%{version}.tar.gz
      
BuildRequires:  python2-devel python3-devel
BuildRequires:  Cython python3-Cython

%description
The rencode module is a modified version of bencode from the
BitTorrent project.  For complex, heterogeneous data structures with
many small elements, r-encodings take up significantly less space than
b-encodings.

%package -n python3-rencode
Summary:    Web safe object pickling/unpickling

%description -n python3-rencode
The rencode module is a modified version of bencode from the
BitTorrent project.  For complex, heterogeneous data structures with
many small elements, r-encodings take up significantly less space than
b-encodings.

%prep
%setup -q -n rencode-%{version}

rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

%build
CFLAGS="%{optflags}" %{__python} setup.py build

pushd %{py3dir}
CFLAGS="%{optflags}" %{__python3} setup.py build
popd

%install
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

#fix permissions on shared objects
chmod 0755 \
    %{buildroot}%{python_sitearch}/rencode/_rencode.so \
    %{buildroot}%{python3_sitearch}/rencode/_rencode.cpython-*.so

%check
pushd tests
ln -sf %{buildroot}%{python_sitearch}/rencode rencode
%{__python} test_rencode.py
%{__python} timetest.py
popd

pushd %{py3dir}/tests
ln -sf %{buildroot}%{python3_sitearch}/rencode rencode
%{__python3} test_rencode.py
%{__python3} timetest.py
popd

%files
%{python_sitearch}/rencode
%{python_sitearch}/rencode*.egg-info
%doc COPYING README.md

%files -n python3-rencode
%{python3_sitearch}/rencode
%{python3_sitearch}/rencode*.egg-info
%doc COPYING README.md

%changelog
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
