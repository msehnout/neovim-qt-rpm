Name:           neovim-qt
Version:        0.2.7
Release:        1%{?dist}
Summary:        Neovim GUI written in Qt

License:        ISC
URL:            https://github.com/equalsraf/neovim-qt
Source0:        https://github.com/equalsraf/%{name}/archive/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  gtest-devel
BuildRequires:  qt5-devel
BuildRequires:  neovim
Requires:       neovim

%description
GUI for Neovim, much like a GVim for the old Vim, but written in Qt5.

%prep
%autosetup

%build
%cmake .
make %{?_smp_mflags}

%install
%make_install

%files
%{_bindir}/nvim-qt
%{_datadir}/applications/nvim-qt.desktop
%{_datadir}/nvim-qt/runtime/README.md
%{_datadir}/nvim-qt/runtime/doc/nvim_gui_shim.txt
%{_datadir}/nvim-qt/runtime/doc/tags
%{_datadir}/nvim-qt/runtime/plugin/nvim_gui_shim.vim
%{_datadir}/pixmaps/nvim-qt.png
%license LICENSE
%doc README.md

%changelog
* Tue May 02 2017 Martin Sehnoutka <msehnout@redhat.com> 0.2.7-1
- Update to 0.2.7 (msehnout@redhat.com)

* Sat Feb 18 2017 Sehny <msehnout@users.noreply.github.com> 0.2.5-1
- new package built with tito

* Sat Feb 18 2017 Sehny <msehnout@users.noreply.github.com>
- First try of packaging neovim-qt
