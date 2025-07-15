%define shortname vim-latex
%define snapdate 20110214.1049
%define rev 089726a
%define rel 1
Summary:	Vim plugin: LaTeX
Name:		vim-plugin-latex
Version:	1.8.23
Release:	1.%{snapdate}.%{rev}.%{rel}
License:	vim
Group:		Applications/Editors/Vim
Source0:	http://downloads.sourceforge.net/project/%{shortname}/snapshots/%{shortname}-%{version}-%{snapdate}-git%{rev}.tar.gz
# Source0-md5:	67d626cb2c1614dabf70c6a3b21f57df
Patch0:		%{name}-makefile.patch
Epoch:		1
URL:		http://vim-latex.sourceforge.net/
BuildRequires:	rpm-pythonprov
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
%setup -qn vim-latex-%{version}-%{snapdate}-git%{rev}
%patch -P0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}
%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/latextags
%attr(755,root,root) %{_bindir}/ltags
%{_vimdatadir}/compiler/*
%{_vimdatadir}/doc/*
%{_vimdatadir}/ftplugin/*
%{_vimdatadir}/indent/*
%{_vimdatadir}/plugin/*
