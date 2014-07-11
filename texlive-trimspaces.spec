# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/trimspaces
# catalog-date 2009-11-10 08:50:14 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-trimspaces
Version:	1.1
Release:	8
Summary:	Trim spaces around an argument or within a macro
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/trimspaces
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trimspaces.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trimspaces.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trimspaces.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A very short package that allows you to expandably remove
spaces around a token list (commands are provided to remove
spaces before, spaces after, or both); or to remove surrounding
spaces within a macro definition, or to define space-stripped
macros.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/trimspaces/trimspaces.sty
%doc %{_texmfdistdir}/doc/latex/trimspaces/README
%doc %{_texmfdistdir}/doc/latex/trimspaces/trimspaces.pdf
#- source
%doc %{_texmfdistdir}/source/latex/trimspaces/trimspaces.ins
%doc %{_texmfdistdir}/source/latex/trimspaces/trimspaces.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 757112
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 719806
- texlive-trimspaces
- texlive-trimspaces
- texlive-trimspaces

