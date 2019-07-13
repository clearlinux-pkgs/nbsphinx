#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nbsphinx
Version  : 0.4.2
Release  : 23
URL      : https://files.pythonhosted.org/packages/bd/78/bea43a90c3b363587df4e0554081f39a43a45014641356dcbab44c079d29/nbsphinx-0.4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/bd/78/bea43a90c3b363587df4e0554081f39a43a45014641356dcbab44c079d29/nbsphinx-0.4.2.tar.gz
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
Patch1: nodeps.patch

%description
Jupyter Notebook Tools for Sphinx
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

%description python3
python3 components for the nbsphinx package.


%prep
%setup -q -n nbsphinx-0.4.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551034843
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nbsphinx
cp LICENSE %{buildroot}/usr/share/package-licenses/nbsphinx/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nbsphinx/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
