%{?scl:%scl_package nodejs-fs-write-stream-atomic}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-fs-write-stream-atomic

%global npm_name fs-write-stream-atomic
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-fs-write-stream-atomic
Version:	1.0.3
Release:	3%{?dist}
Summary:	Like `fs.createWriteStream(...)`, but atomic
Url:		https://github.com/npm/fs-write-stream-atomic
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ISC

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(tap)
%endif

BuildRequires:	%{?scl_prefix}npm(graceful-fs)

Requires:	%{?scl_prefix}npm(graceful-fs)

%description
Like `fs.createWriteStream(...)`, but atomic

%prep
%setup -q -n package

%{nodejs_fixdep} graceful-fs

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check
tap test/*.js
%endif

%files
%{nodejs_sitelib}/fs-write-stream-atomic

%doc README.md
%doc LICENSE

%changelog
* Fri Nov 27 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.3-3
- Enable SCL macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.3-1
- New upstream release

* Wed May 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-1
- Initial build
