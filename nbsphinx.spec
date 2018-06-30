#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nbsphinx
Version  : 0.3.3
Release  : 7
URL      : https://files.pythonhosted.org/packages/c0/34/5b7513d9dc62e4827fdfc3407d68b95d265dcca5b1033d50f73dc33c3887/nbsphinx-0.3.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/c0/34/5b7513d9dc62e4827fdfc3407d68b95d265dcca5b1033d50f73dc33c3887/nbsphinx-0.3.3.tar.gz
Summary  : Jupyter Notebook Tools for Sphinx
Group    : Development/Tools
License  : MIT
Requires: nbsphinx-python3
Requires: nbsphinx-python
Requires: Jinja2
Requires: Sphinx
Requires: docutils
Requires: ipykernel
Requires: nbconvert
Requires: nbformat
Requires: nbsphinx
Requires: traitlets
BuildRequires : Jinja2
BuildRequires : Sphinx
BuildRequires : docutils
BuildRequires : nbconvert
BuildRequires : nbformat
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : traitlets

%description
=================================
        
        ``nbsphinx`` is a Sphinx_ extension that provides a source parser for
        ``*.ipynb`` files.
        Custom Sphinx directives are used to show `Jupyter Notebook`_ code cells (and of
        course their results) in both HTML and LaTeX output.
        Un-evaluated notebooks -- i.e. notebooks without stored output cells -- will be
        automatically executed during the Sphinx build process.

%package python
Summary: python components for the nbsphinx package.
Group: Default
Requires: nbsphinx-python3

%description python
python components for the nbsphinx package.


%package python3
Summary: python3 components for the nbsphinx package.
Group: Default
Requires: python3-core

%description python3
python3 components for the nbsphinx package.


%prep
%setup -q -n nbsphinx-0.3.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1524670103
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
