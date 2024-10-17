Name:		texlive-typewriter
Version:	46641
Release:	2
Summary:	Typeset with a randomly variable monospace font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/typewriter
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typewriter.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typewriter.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The typewriter package uses the OpenType Computer Modern
Unicode Typewriter font, together with a LuaTeX virtual font
setup that introduces random variability in grey level and
angle of each character. It was originally an answer to a
question on stackexchange.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/typewriter
%doc %{_texmfdistdir}/doc/lualatex/typewriter

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
