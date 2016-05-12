Name:           puppet-cinder
Version:        XXX
Release:        XXX
Summary:        Puppet module for OpenStack Cinder
License:        Apache-2.0

URL:            https://launchpad.net/puppet-cinder

Source0: 	http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       puppet-qpid
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
%setup -q -n %{name}-%{version}

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

