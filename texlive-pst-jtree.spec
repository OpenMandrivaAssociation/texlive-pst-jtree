Name:		texlive-pst-jtree
Version:	20946
Release:	1
Summary:	Typeset complex trees for linguists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-jtree
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-jtree.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-jtree.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
jTree uses PStricks to enable linguists to typeset complex
trees. The package requires use of PStricks (of course) and
xkeyval packages. jTree is a development of, and replacement
for, the jftree package, which is no longer available.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-jtree/pst-jtree.tex
%{_texmfdistdir}/tex/latex/pst-jtree/pst-jtree.sty
%doc %{_texmfdistdir}/doc/generic/pst-jtree/Doc-source.zip
%doc %{_texmfdistdir}/doc/generic/pst-jtree/README
%doc %{_texmfdistdir}/doc/generic/pst-jtree/pst-jtree-doc-add.pdf
%doc %{_texmfdistdir}/doc/generic/pst-jtree/pst-jtree-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-jtree/pst-jtree-examples.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
