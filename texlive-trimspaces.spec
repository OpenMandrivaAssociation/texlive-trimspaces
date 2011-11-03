# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/trimspaces
# catalog-date 2009-11-10 08:50:14 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-trimspaces
Version:	1.1
Release:	1
Summary:	Trim spaces around an argument or within a macro
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/trimspaces
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trimspaces.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trimspaces.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trimspaces.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A very short package that allows you to expandably remove
spaces around a token list (commands are provided to remove
spaces before, spaces after, or both); or to remove surrounding
spaces within a macro definition, or to define space-stripped
macros.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/trimspaces/trimspaces.sty
%doc %{_texmfdistdir}/doc/latex/trimspaces/README
%doc %{_texmfdistdir}/doc/latex/trimspaces/trimspaces.pdf
#- source
%doc %{_texmfdistdir}/source/latex/trimspaces/trimspaces.ins
%doc %{_texmfdistdir}/source/latex/trimspaces/trimspaces.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
