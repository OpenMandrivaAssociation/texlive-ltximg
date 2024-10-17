Name:		texlive-ltximg
Version:	59335
Release:	2
Summary:	Split LaTeX files to sanitise a conversion process
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/ltximg
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltximg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltximg.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/scripts/ltximg
%doc %{_texmfdistdir}/doc/man/man1/*
%doc %{_texmfdistdir}/doc/support/ltximg

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/ltximg/ltximg.pl ltximg
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
