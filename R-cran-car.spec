%define modulename car
%define version 1.2.16
%define realver 1.2-16
%define r_library %{_libdir}/R/library

Summary:	Companion to Applied Regression for R
Name:		R-cran-%{modulename}
Version:	%{version}
Release:	%mkrel 2
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:	R-base
Requires:	R-base
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The package contains mostly functions for applied regression, linear 
models, and generalized linear models, with an emphasis on regression 
diagnostics, particularly graphical diagnostic methods. There are also 
some utility functions.

%prep
%setup -q -c

%build

R CMD build %{modulename}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{r_library}

# install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# provided by R-base
rm -rf %{buildroot}/%{r_library}/R.css

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{r_library}/%{modulename}
