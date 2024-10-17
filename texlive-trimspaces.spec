Name:		texlive-trimspaces
Version:	15878
Release:	2
Summary:	Trim spaces around an argument or within a macro
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/trimspaces
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trimspaces.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trimspaces.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trimspaces.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
