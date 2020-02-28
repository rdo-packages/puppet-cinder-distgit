%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-cinder
Version:        15.4.0
Release:        1%{?dist}
Summary:        Puppet module for OpenStack Cinder
License:        ASL 2.0

URL:            https://launchpad.net/puppet-cinder

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-inifile
Requires:       puppet-keystone
Requires:       puppet-rabbitmq
Requires:       puppet-oslo
Requires:       puppet-openstacklib
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Puppet module for OpenStack Cinder

%prep
%setup -q -n openstack-cinder-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/cinder/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/cinder/



%files
%{_datadir}/openstack-puppet/modules/cinder/


%changelog
* Fri Oct 04 2019 RDO <dev@lists.rdoproject.org> 15.4.0-1
- Update to 15.4.0

