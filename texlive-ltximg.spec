%global tl_name ltximg
%global tl_revision 59335

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Extract LaTeX environments into separate image files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/ltximg
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ltximg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ltximg.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(ltximg.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
ltximg is a Perl script that automates the process of extracting and
converting environments provided by TikZ, PStricks and other packages
from input file to image formats and standalone files using ghostscript
and poppler-utils. It generates a file with only extracted environments
and another with all extracted environments converted to
\includegraphics.

