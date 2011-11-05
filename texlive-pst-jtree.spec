# revision 20946
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-jtree
# catalog-date 2011-01-05 08:46:38 +0100
# catalog-license lppl1.3
# catalog-version 2.6
Name:		texlive-pst-jtree
Version:	2.6
Release:	1
Summary:	Typeset complex trees for linguists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-jtree
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-jtree.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-jtree.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
jTree uses PStricks to enable linguists to typeset complex
trees. The package requires use of PStricks (of course) and
xkeyval packages. jTree is a development of, and replacement
for, the jftree package, which is no longer available.

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
%{_texmfdistdir}/tex/generic/pst-jtree/pst-jtree.tex
%{_texmfdistdir}/tex/latex/pst-jtree/pst-jtree.sty
%doc %{_texmfdistdir}/doc/generic/pst-jtree/Doc-source.zip
%doc %{_texmfdistdir}/doc/generic/pst-jtree/README
%doc %{_texmfdistdir}/doc/generic/pst-jtree/pst-jtree-doc-add.pdf
%doc %{_texmfdistdir}/doc/generic/pst-jtree/pst-jtree-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-jtree/pst-jtree-examples.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
