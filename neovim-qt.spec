Name:           neovim-qt
Version:        0.2.7
Release:        3%{?dist}
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
BuildRequires:  msgpack-devel
Requires:       neovim

Patch0001:      0001-Fix-compilation-on-F26.patch

%description
GUI for Neovim, much like a GVim for the old Vim, but written in Qt5.

%package libs
Summary: Libraries used by Neovim-Qt

%description libs
Libraries used by Neovim-Qt

%prep
%autosetup -S git

%build
%cmake .
make %{?_smp_mflags}

%install
%make_install
mkdir -p ${RPM_BUILD_ROOT}/%{_libdir}
install -m 755 lib/libneovim-qt-gui.so ${RPM_BUILD_ROOT}/%{_libdir}/libneovim-qt-gui.so

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

%files libs
%{_libdir}/libneovim-qt-gui.so

%changelog
* Mon May 22 2017 Martin Sehnoutka <msehnout@redhat.com> - 0.2.7-3
- Fix missing shared libraries

* Mon May 22 2017 Martin Sehnoutka <msehnout@redhat.com> - 0.2.7-2
- Use system msgpack (fixes compilation on f26)

* Tue May 02 2017 Martin Sehnoutka <msehnout@redhat.com> 0.2.7-1
- init 0.2.7 (msehnout@redhat.com)
