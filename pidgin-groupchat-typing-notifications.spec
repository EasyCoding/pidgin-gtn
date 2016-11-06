%global commit0 33a75f928894a8f47da24d35ccff4c69d303f44e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: pidgin-groupchat-typing-notifications
Version: 0
Release: 1.git%{shortcommit0}%{?dist}
Summary: Adds typing notifications for group chats in Pidgin 

License: GPLv3+
URL: https://github.com/EionRobb/pidgin-groupchat-typing-notifications
Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(pidgin)
BuildRequires: gcc

%description
Adds typing notifications for multi-user group chats in Pidgin.
Currently only tested as working with the Hangouts plugin, but
support for other protocols will come later.

%prep
%setup -qn %{name}-%{commit0}

# fix W: wrong-file-end-of-line-encoding
sed -i -e "s,\r,," README.md

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build

%install
# Executing base install from makefile...
%make_install

# Setting correct chmod...
chmod 755 %{buildroot}%{_libdir}/pidgin/grouptyping.so

%files
%{_libdir}/pidgin/grouptyping.so
%license LICENSE
%doc README.md

%changelog
* Sun Nov 06 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.git33a75f9
- Initial commit.
