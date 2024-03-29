#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nbsphinx
Version  : 0.8.8
Release  : 50
URL      : https://files.pythonhosted.org/packages/7d/5c/2b8da705a79820e08bddd99b4f25ea140e5feeae080219a3351fa17b7b3d/nbsphinx-0.8.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/7d/5c/2b8da705a79820e08bddd99b4f25ea140e5feeae080219a3351fa17b7b3d/nbsphinx-0.8.8.tar.gz
Summary  : Jupyter Notebook Tools for Sphinx
Group    : Development/Tools
License  : MIT
Requires: nbsphinx-license = %{version}-%{release}
Requires: nbsphinx-python = %{version}-%{release}
Requires: nbsphinx-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(docutils)
BuildRequires : pypi(ipywidgets)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(jupyterlab)
BuildRequires : pypi(jupytext)
BuildRequires : pypi(matplotlib)
BuildRequires : pypi(nbconvert)
BuildRequires : pypi(nbformat)
BuildRequires : pypi(pandas)
BuildRequires : pypi(sphinx)
BuildRequires : pypi(traitlets)

%description
This folder contains the source files for the documentation.
See ../CONTRIBUTING.rst for how to create the HTML and LaTeX
files from these sources.

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
Requires: pypi(ipywidgets)
Requires: pypi(jinja2)
Requires: pypi(jupyterlab)
Requires: pypi(jupytext)
Requires: pypi(matplotlib)
Requires: pypi(nbconvert)
Requires: pypi(nbformat)
Requires: pypi(pandas)
Requires: pypi(sphinx)
Requires: pypi(traitlets)

%description python3
python3 components for the nbsphinx package.


%prep
%setup -q -n nbsphinx-0.8.8
cd %{_builddir}/nbsphinx-0.8.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640971708
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
cp %{_builddir}/nbsphinx-0.8.8/LICENSE %{buildroot}/usr/share/package-licenses/nbsphinx/feb1c90260a473a4ad3de6aa6bd1a216c865fa73
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nbsphinx/feb1c90260a473a4ad3de6aa6bd1a216c865fa73

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
