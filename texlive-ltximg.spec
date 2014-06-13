# revision 32346
# category Package
# catalog-ctan /support/ltximg
# catalog-date 2013-12-05 10:21:29 +0100
# catalog-license gpl2
# catalog-version 1.0
Name:		texlive-ltximg
Version:	1.0
Release:	3
Summary:	Split LaTeX files to sanitise a conversion process
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/ltximg
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltximg.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltximg.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-ltximg.bin = %{EVRD}

%description
The package provides a Perl script that extracts all TikZ and
PStricks environments for separate processing to produce images
(in eps, pdf, png or jpg format) for use by a converter or the
preview bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/ltximg
%{_texmfdistdir}/scripts/ltximg/ltximg.pl
%doc %{_texmfdistdir}/doc/support/ltximg/README
%doc %{_texmfdistdir}/doc/support/ltximg/ltximg-doc.pdf
%doc %{_texmfdistdir}/doc/support/ltximg/ltximg-doc.tex
%doc %{_texmfdistdir}/doc/support/ltximg/test.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/ltximg/ltximg.pl ltximg
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
