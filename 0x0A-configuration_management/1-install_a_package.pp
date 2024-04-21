# This is a Puppet manifest file (1-install_a_package.pp) to install Flask using Puppet.
# It ensures that Flask version 2.1.0 is installed.

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}


