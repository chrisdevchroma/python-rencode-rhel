# Remove private provides from .so files in the python_sitearch directory
%global __provides_exclude_from ^%{python_sitearch}/.*\\.so$

%global svn_rev 33
%global svn_date 20121209

Name:           python-rencode
Version:        1.0.2
Release:        2.%{svn_date}svn%{svn_rev}%{?dist}
Summary:        Web safe object pickling/unpickling
License:        GPLv3+ and BSD
URL:            http://code.google.com/p/rencode/

# svn export -r%%{svn_rev} http://rencode.googlecode.com/svn/trunk rencode-%%{version}-r%%{svn_rev}
# tar -Jcf rencode-%%{version}-r%%{svn_rev}.tar.xz rencode-%%{version}-r%%{svn_rev} 
Source0:        rencode-%{version}-r%{svn_rev}.tar.xz

# support the older version of Python in EL6
Patch1:        python-rencode-support-older-pythons.patch
      
BuildRequires:  python2-devel
BuildRequires:  Cython

%description
The rencode module is a modified version of bencode from the
BitTorrent project.  For complex, heterogeneous data structures with
many small elements, r-encodings take up significantly less space than
b-encodings.

%prep
%setup -qn rencode-%{version}-r%{svn_rev}
%patch1 -p1

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

#fix permissions on shared objects
chmod 0755 \
    %{buildroot}%{python_sitearch}/rencode/_rencode.so

%check
pushd tests
ln -sf %{buildroot}%{python_sitearch}/rencode rencode
%{__python} test_rencode.py
%{__python} timetest.py
popd

%files
%{python_sitearch}/rencode
%{python_sitearch}/rencode*.egg-info
%doc COPYING README

%changelog
* Mon May 06 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.2-2.20121209svn33
- use macros consistently
- fix permissions on shared objects
- drop useless setuptools copypasta
- fix License tag
- add patch to support older versions of Python

* Thu Apr 18 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.2-1.20121209svn33
- initial package
