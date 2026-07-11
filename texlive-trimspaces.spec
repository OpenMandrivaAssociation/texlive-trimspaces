%global tl_name trimspaces
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Trim spaces around an argument or within a macro
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/trimspaces
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/trimspaces.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/trimspaces.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/trimspaces.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A very short package that allows you to expandably remove spaces around
a token list (commands are provided to remove spaces before, spaces
after, or both); or to remove surrounding spaces within a macro
definition, or to define space-stripped macros.

