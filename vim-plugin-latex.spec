Summary:	Vim plugin: LaTeX
Name:		vim-plugin-latex
Version:	20060325
Release:	1
License:	vim
Group:		Applications/Editors/Vim
Source0:	http://vim-latex.sourceforge.net/download/latexSuite%{version}.tar.gz
# Source0-md5:	f7bdb270508a8a88339ff857a52986ff
URL:		http://vim-latex.sourceforge.net/
# for _vimdatadir existence
Requires:	vim-rt >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
Vim is undoubtedly one of the best editors ever made. LaTeX is an
extremely powerful, intelligent typesetter. Vim-LaTeX aims at bringing
together the best of both these worlds.

We attempt to provide a comprehensive set of tools to view, edit and
compile LaTeX documents without needing to ever quit Vim. Together,
they provide tools starting from macros to speed up editing LaTeX
documents to compiling tex files to forward searching .dvi documents.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}
cp -a . $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/*
