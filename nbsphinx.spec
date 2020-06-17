#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nbsphinx
Version  : 0.7.1
Release  : 33
URL      : https://files.pythonhosted.org/packages/78/b1/02aeb1c0acfdcd8252afedf74168a3e41d8c6708f9b836cc59552b41d0c3/nbsphinx-0.7.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/78/b1/02aeb1c0acfdcd8252afedf74168a3e41d8c6708f9b836cc59552b41d0c3/nbsphinx-0.7.1.tar.gz
Summary  : Jupyter Notebook Tools for Sphinx
Group    : Development/Tools
License  : MIT
Requires: nbsphinx-license = %{version}-%{release}
Requires: nbsphinx-python = %{version}-%{release}
Requires: nbsphinx-python3 = %{version}-%{release}
Requires: Jinja2
Requires: Sphinx
Requires: docutils
Requires: nbconvert
Requires: nbformat
Requires: traitlets
BuildRequires : Jinja2
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : docutils
BuildRequires : nbconvert
BuildRequires : nbformat
BuildRequires : traitlets

%description
=================================
        
        ``nbsphinx`` is a Sphinx_ extension that provides a source parser for
        ``*.ipynb`` files.
        Custom Sphinx directives are used to show `Jupyter Notebook`_ code cells (and of
        course their results) in both HTML and LaTeX output.
        Un-evaluated notebooks -- i.e. notebooks without stored output cells -- will be
        automatically executed during the Sphinx build process.

%package license
Summary: license components for the nbsphinx package.
Group: Default

%description license
license components for the nbsphinx package.


%package python
Summary: python components for the nbsphinx package.
Group: Default
Requires: nbsphinx-python3 = %{version}-%{release}

%description python
python components for the nbsphinx package.


%package python3
Summary: python3 components for the nbsphinx package.
Group: Default
Requires: python3-core
Provides: pypi(nbsphinx)
Requires: pypi(docutils)
Requires: pypi(jinja2)
Requires: pypi(nbconvert)
Requires: pypi(nbformat)
Requires: pypi(sphinx)
Requires: pypi(traitlets)

%description python3
python3 components for the nbsphinx package.


%prep
%setup -q -n nbsphinx-0.7.1
cd %{_builddir}/nbsphinx-0.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592409714
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nbsphinx
cp %{_builddir}/nbsphinx-0.7.1/LICENSE %{buildroot}/usr/share/package-licenses/nbsphinx/a7274a3964b0b88c034fede0151a757ef9548415
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nbsphinx/a7274a3964b0b88c034fede0151a757ef9548415

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
