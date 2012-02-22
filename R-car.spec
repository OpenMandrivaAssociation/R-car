%bcond_with bootstrap
%global packname  car
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.0_12
Release:          2
Summary:          Companion to Applied Regression
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-12.tar.gz
BuildArch:        noarch
Requires:         R-core R-stats R-graphics R-MASS R-nnet
Requires:         R-leaps R-lme4 R-nlme R-mgcv R-rgl R-survival
%if %{without bootstrap}
Requires:         R-alr3 R-lmtest R-sandwich R-survey
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats
BuildRequires:    R-graphics R-MASS R-nnet
BuildRequires:    R-leaps R-lme4 R-nlme R-mgcv R-rgl R-survival
%if %{with bootstrap}
BuildRequires:    R-alr3 R-lmtest R-nlme R-sandwich R-survey
%endif
%rename R-cran-car

%description
This package accompanies J. Fox and S. Weisberg, An R Companion to Applied
Regression, Second Edition, Sage, 2011.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
